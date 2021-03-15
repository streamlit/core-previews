import streamlit as st
from execbox import execbox
from e2e_loader import select_script, get_script
from urllib.parse import urlparse

with open("requirements.txt") as requirements:
    s3_url = requirements.read().split("\n")[-2]
import re

col1, padding, col2 = st.beta_columns([3, 0.1, 1])


def get_first_match(regex, s):
    match = re.search(regex, s)
    return match.group(1) if match else None


def get_branch_info():
    path = urlparse(s3_url).path
    path_parts = list(filter(None, path.split("/")))
    core_preview_branch = "/".join(path_parts[:-1])

    branch = get_first_match("(.*)-preview", core_preview_branch)
    pr = get_first_match("pr-(\\d+)", core_preview_branch)

    return branch, pr


branch, pr_number = get_branch_info()
if pr_number is not None:
    col2.write(
        f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})"
    )
col2.write(f"🎡 [Download wheel]({s3_url})")

with col1:
    selected_script = select_script(branch, pr_number)

# fallback if things fail
script = "import streamlit as st"

if selected_script:
    if 'download_url' in selected_script:
        script = get_script(selected_script["download_url"])
    else:
        with open(selected_script['path'], 'r', encoding='utf-8') as f:
            script = f.read()

st.header("Edit my source 👇")
execbox(
    script,
    autorun=True,
    line_numbers=True,
    height=300,
)
