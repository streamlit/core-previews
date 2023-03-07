import streamlit as st

st.title("📋 State Tester")
st.write("Testing state management.")

checkbox_value = st.checkbox("Checkbox Value linked to state", key="checkbox")

if "checkbox" not in st.session_state:
    st.session_state.checkbox = checkbox_value

st.write("**Session State:**")
st.write(st.session_state)


st.title("🎮 Control Tester")
st.write("Testing all control elements in one place.")

st.write("**Basic Form:**")
with st.form(key="tester"):
    st.write("This form just prints out the text input!")
    checkbox_input = st.checkbox("Boolean to Print")
    st.form_submit_button("Submit", type="primary")
st.caption("Basic Form Answer:")
st.write(checkbox_input)

st.write("**Clear on Submit Form:**")
with st.form(key="other", clear_on_submit=True):
    st.write("This form just prints out the text input!")
    slider_input = st.slider("Form Slider", 0, 10)
    st.form_submit_button("Submit", use_container_width=True)
st.caption("Clear on Submit Form Answer:")
st.write(slider_input)

st.write("**Experimental Rerun:**")
clicked = st.button("Trigger Rerun")
if clicked:
    st.experimental_rerun()

st.stop()
st.write("🚧 :red[if you see this, st.stop does not work!]")
