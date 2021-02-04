import streamlit as st

image_url = "https://i.guim.co.uk/img/media/86c3481516dce247943ac2978b4f48d16a3ac265/0_170_5120_3074/master/5120.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=637dc5731d52754675ef36344a6af3c8"


col1, col2 = st.beta_columns(2)

with col1:
    for _ in range(3):
        st.image(image_url)

with col2:
    st.image(image_url)
    st.markdown("# Some header 1")
    st.markdown("## Some header 2")
    st.markdown("### Some header 3")
