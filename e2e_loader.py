import requests
import streamlit as st


@st.cache_data(ttl=2 * 60 * 60)  # 2 hours
def get_scripts(fork=None, branch=None, headers={}):
    if fork is None:
        fork = "streamlit"
    if branch is None:
        branch = "develop"

    response = requests.get(
        f"https://api.github.com/repos/{fork}/streamlit/contents/e2e_playwright?ref={branch}",
        headers=headers,
    )
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get scripts", response.status_code, response.text)
        return []


@st.cache_data(ttl=2 * 60 * 60)  # 2 hours
def get_script(url: str) -> str:
    response = requests.get(url)
    e2e_script = response.text
    return e2e_script


def set_auth():
    if gh_token := st.text_input("Enter your GH token", key="key"):
        return {"Authorization": "token %s" % gh_token}


@st.cache_data
def get_pr_info(pr_number):
    r = requests.get(
        f"https://api.github.com/repos/streamlit/streamlit/pulls/{pr_number}"
    )
    try:
        body = r.json()
        fork = body["head"]["user"]["login"]
        branch = body["head"]["ref"]
        return fork, branch
    except Exception:
        return None, None


def select_script(branch, pr_number, auth={}, default_script=None):
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
        print("scripts", scripts)
    except Exception as e:
        print("Failed to get scripts", e)
        auth_headers = set_auth()
        if auth_headers:
            scripts = get_scripts(fork=fork, branch=branch, headers=auth_headers)

    if scripts:
        return render_script_selector(scripts, default_script)


def render_script_selector(scripts, default_script=None):
    default_script_option = [{"name": "Default script", "path": "./default_script.py"}]
    # Filter out all python scripts but ignore the test scripts (ending with _test.py)
    scripts = [
        script
        for script in scripts
        if script["name"].endswith(".py")
        and not script["name"].endswith("_test.py")
        and not script["name"].endswith("__.py")
    ]

    options = default_script_option + scripts

    # Find the index of the default script if provided
    default_index = 0
    if default_script:
        for i, script in enumerate(options):
            if script["name"] == default_script:
                default_index = i
                break

    return st.selectbox(
        "Select e2e script",
        options=options,
        format_func=lambda x: x["name"],
        index=default_index,
    )
