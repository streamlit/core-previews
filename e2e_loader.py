import requests
import streamlit as st


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def get_scripts(fork=None, branch=None, headers={}):
    if fork is None:
        fork = "streamlit"
    if branch is None:
        branch = "develop"

    response = requests.get(
        f"https://api.github.com/repos/{fork}/streamlit/contents/e2e/scripts?ref={branch}",
        headers=headers,
    )
    if response.status_code == 200:
        return response.json()


@st.cache(suppress_st_warning=True)
def get_script(url):
    response = requests.get(url)
    e2e_script = response.text
    return e2e_script


def set_auth():
    gh_token = st.text_input("Enter your GH token", key="key")
    if gh_token:
        return {"Authorization": "token %s" % gh_token}


@st.cache(suppress_st_warning=True)
def get_pr_info(pr_number):
    r = requests.get(
        f"https://api.github.com/repos/streamlit/streamlit/pulls/{pr_number}"
    )
    try:
        body = r.json()
        fork = body["head"]["user"]["login"]
        branch = body["head"]["ref"]
        return fork, branch
    except:
        return None, None


def select_script(branch, pr_number, auth={}):
    # From the S3 url, we can be passed either a branch ("<branch>-preview")
    # or a PR ("pr-<pr>"). (See get_branch_info() in streamlit_app.py.)
    #
    # If we have a branch, use streamlit's fork (default).
    # If we have a PR, use Github's API to get the fork and branch.
    if pr_number is not None:
        fork, branch = get_pr_info(pr_number)
    else:
        fork = None

    scripts = None
    try:
        scripts = get_scripts(fork=fork, branch=branch, headers=auth)
    except Exception as e:
        auth_headers = set_auth()
        if auth_headers:
            scripts = get_scripts(fork=fork, branch=branch, headers=auth_headers)

    if scripts:
        return render_script_selector(scripts)


def render_script_selector(scripts):
    placeholder_option = [{"name": "Please select a script"}]
    options = placeholder_option + scripts
    selected_script = st.selectbox(
        "Select E2E script", options=options, format_func=lambda x: x["name"]
    )
    if selected_script and "download_url" in selected_script:
        return selected_script
