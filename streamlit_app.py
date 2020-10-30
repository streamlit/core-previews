import streamlit as st
from execbox import execbox
from e2e_loader import select_script, get_script

with open('requirements.txt') as requirements:
    s3_url = requirements.read().split('\n')[-2]
import re

col1, padding, col2 = st.beta_columns([3, .1, 1])

match = re.search('/pr-(\\d+)/', s3_url)
if match:
    pr_number = match.group(1)

    col2.write(f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})")
    col2.write(f"🎡 [Download wheel]({s3_url})")

with col1:
    selected_script = select_script()

if selected_script:
    script = get_script(selected_script["download_url"])
    # st.write("placeholder", script)
else:
    script = """
import streamlit as st

st.header("Results")
if st.button("Press me!"):
    st.balloons()
    """

st.header("Edit my source 👇")
execbox(script,
    autorun=True,
    line_numbers=True,
    height=300,
)
