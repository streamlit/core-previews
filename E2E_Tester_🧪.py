from urllib.parse import urlparse

import streamlit as st
from execbox import execbox

from e2e_loader import get_script, select_script

with open("requirements.txt") as requirements:
    s3_url = requirements.read().split("\n")[-2]
import re

col1, padding, col2 = st.columns([3, 0.1, 1])


def get_first_match(regex, s):
    match = re.search(regex, s)
    return match.group(1) if match else None


def get_branch_info():
    path = urlparse(s3_url).path
    path_parts = list(filter(None, path.split("/")))
    core_preview_branch = "/".join(path_parts[:-1])

    branch = get_first_match("(.*)-preview", core_preview_branch)
    # There's no nightly branch, so default to develop
    branch = "develop" if branch == "nightly" else branch
    pr = get_first_match("pr-(\\d+)", core_preview_branch)

    return branch, pr


def strip_license_header(script_content):
    """Remove license header comments from the beginning of the script."""
    lines = script_content.split("\n")
    first_non_comment_line = 0

    # Find the first non-comment line
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("#") and stripped:
            first_non_comment_line = i
            break

    # Return script without the header comments
    return "\n".join(lines[first_non_comment_line:])


def remove_page_config(script_content):
    """Remove st.set_page_config(...) calls from the script."""
    # This regex matches st.set_page_config with any arguments and across multiple lines
    pattern = re.compile(r"st\.set_page_config\s*\([^)]*\)", re.DOTALL)
    return pattern.sub("", script_content)


branch, pr_number = get_branch_info()
if pr_number is not None:
    col2.write(
        f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})"
    )
col2.write(f"🎡 [Download wheel]({s3_url})")

# Get script name from query parameter if available
query_params = st.query_params.to_dict()
script_from_query = query_params.get("script", None)

with col1:
    selected_script = select_script(branch, pr_number, default_script=script_from_query)

    # If we have a script from query params, update the URL to match the selection
    if selected_script and script_from_query != selected_script.get("name"):
        st.query_params["script"] = selected_script.get("name", "")

# fallback if things fail
script = "import streamlit as st"

if selected_script:
    if "download_url" in selected_script:
        script = get_script(selected_script["download_url"])
        # Strip license header from downloaded scripts
        script = strip_license_header(script)
        # Remove st.set_page_config calls
        script = remove_page_config(script)
    else:
        with open(selected_script["path"], "r", encoding="utf-8") as f:
            script = f.read()

st.subheader("Edit my source :material/edit_square:")
execbox(
    script,
    autorun=True,
    line_numbers=True,
    height=300,
)
