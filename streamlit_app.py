import streamlit as st
from execbox import execbox

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
