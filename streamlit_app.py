import streamlit as st
import time

st.title("Demo of cache replay")
number = st.slider("Number")
st.button("Rerun")


@st.experimental_memo()
def func(number):
    time.sleep(2)
    st.write("this is a cached Number:", number)


func(number)
