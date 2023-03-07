import streamlit as st
import pandas as pd
import numpy as np

st.title("💾 Data Display Tester")
st.write("Testing all data display elements in one place.")

st.write("**Metric:**")
a, b = st.columns(2)
with b:
    st.metric("Metric Label", 42, 2)
with a:
    st.metric(label="Temperature = **Cold** :snowflake:", value="30 °F", delta="-5 °F")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.write("**Dataframe:**")
st.dataframe(chart_data, width=500)

st.write("**Table:**")
st.table(chart_data)

st.write("**Json:**")
st.json(chart_data.head().to_dict())