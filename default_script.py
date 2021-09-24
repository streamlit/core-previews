import streamlit as st
import pandas as pd

df = pd.DataFrame(["foo", "bar"])
st.dataframe(df.dtypes)
