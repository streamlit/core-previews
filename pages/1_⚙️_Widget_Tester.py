import streamlit as st

st.title("⚙️ Widget Tester")
st.write("Testing all widgets in one place.")

st.subheader("Input Widgets")
st.write("**Button:**")
button_input = st.button("Button Label")
if button_input:
    st.write("You pressed the button!")

st.write("**Download Button:**")
text_contents = """This is some text"""
st.download_button("Download Text", text_contents)

st.write("**Checkbox:**")
checkbox_input = st.checkbox("Checkbox")
st.write(f"Your checkbox input is {checkbox_input}!")

st.write("**Radio:**")
radio_input = st.radio("Radio", ["cat", "dog"])
st.write(f"Your radio input is {radio_input}!")

st.write("**Selectbox:**")
selectbox_input = st.selectbox("Selectbox", ["cat", "dog"])
st.write(f"Your selectbox input is {selectbox_input}!")

st.write("**Multi-Select:**")
multiselectbox_input = st.multiselect("Multiselect", ["cat", "dog"])
st.write(f"Your multiselectbox input is {multiselectbox_input}!")

st.write("**Slider:**")
slider_input = st.slider("Slider")
st.write(f"Your slider input is {slider_input}!")

st.write("**Select Slider:**")
select_slider_input = st.select_slider("Select Slider", ["cat", "dog"])
st.write(f"Your select_slider input is {select_slider_input}!")

st.write("**Text Input:**")
text_input = st.text_input("Text Input")
st.write(f"Your text input is {text_input}!")

st.write("**Number Input:**")
number_input = st.number_input("Number Input")
st.write(f"Your number input is {number_input}!")

st.write("**Text Area:**")
text_area_input = st.text_area("Text Area")
st.write(f"Your text_area input is {text_area_input}!")

st.write("**Date Input:**")
date_input = st.date_input("Date Input")
st.write(f"Your date input is {date_input}!")

st.write("**Time Input:**")
time_input = st.time_input("Time Input")
st.write(f"Your time input is {time_input}!")

st.write("**File Uploader:**")
file_input = st.file_uploader("File Uploader")
st.write(f"Your file input is {file_input}!")

st.write("**Camera Input:**")
st.caption("Below is the camera input, give camera access to the app to test it out!")
cam_input = st.camera_input("Camera Input")
st.write(f"Your cam input is {cam_input}!")

st.write("**Color Picker:**")
color_input = st.color_picker("Color Picker")
st.write(f"Your color input hex {color_input}!")
