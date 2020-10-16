import streamlit as st
from execbox import execbox

with open('requirements.txt') as requirements:
    s3_url = requirements.read().split('\n')[2]
import re
match = re.search('/pr-(\\d+)/', s3_url)
if match: 
    pr_number = match.group(1)
    
    col1, col2 = st.beta_columns(2)
    col1.write(f"🔭 [View PR on Github](https://github.com/streamlit/streamlit/pull/{pr_number})")
    col2.write(f"🎡 [Download wheel file]({s3_url})")

st.header("Edit my source 👇")
execbox(
    """
import streamlit as st

st.header("Results")
if st.button("Press me!"):
    st.balloons()
""",
    autorun=True,
    line_numbers=True,
    height=300,
)
