import time
import streamlit as st

st.title("📦 Layout Tester")
st.write("Testing all layout & container elements in one place.")
st.write("⬅️ :blue[Don't forget to test out the Multi-Page App navigation, and the resizeable sidebar behavior]")

st.sidebar.subheader(":test_tube: **Sidebar Test:**")
with st.sidebar:
    st.write("**Layout Items:**")
    with st.expander("An **expander**.. with surprises ~~widgets~~ inside :cyclone:"):
        st.write("Expanded!")
    tab1, tab2, tab3 = st.tabs(["**Cat** :cat:", "*Dog* :dog:", "~~Owl~~ :owl:"])
    with tab1:
       st.write("This is the first tab!")
    with tab2:
       st.write("This is the second tab!")
    with tab3:
       st.write("This is the third tab!")
    
    st.write("**Widgets:**")
    st.text_input('Random thought ~~or your credit card number~~:', 'Donations welcome')
    st.checkbox("Agree to the thing :thumbsup::skin-tone-3:")
    st.button("**Go** Button :white_check_mark:")
    st.color_picker('Instructions: **Pick** a *Color*: :rainbow:', '#BB0329')
    slider_input = st.slider("Slider")
    st.selectbox("How would you like to be [contacted](https://dictionary.cambridge.org/us/dictionary/english/contacted)?",
        ("Corgi Stampede", "Email", "Mobile phone"))
    st.radio( "What's your favorite `code` language? :computer:",
    ('Python', 'Javascript', 'Ruby'))
    st.multiselect(
    'I need to highlight these **very** important words',
    ['Coffee', 'Puppies', 'Sushi'])
    st.number_input("Number Input")
    st.date_input("Date Input")
    st.time_input("Time Input")

st.write("**Columns:**")
a, b = st.columns(2)
with b:
    st.write("This is the second column!")
with a:
    st.write("This is the first column!")

st.write("**Tabs:**")
tab_a, tab_b = st.tabs(["Tab A", "Tab B"])
tab_b.write("Here is some text in tab b")
tab_a.write("Some random content in tab a")

st.write("**Expander:**")
with st.expander("Click to open expander"):
    st.write("Inside the expander!")

st.write("**Container:**")
c = st.container()
c.write("this writes to a container!")

st.write("**Empty:**")
a = st.empty()
a.write("this writes to a previously empty block!")


st.title("⏳ Status Tester")
st.write("Testing all status elements in one place.")

st.write("**Progress Bar:**")
my_bar = st.progress(0)
for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)

st.write("**Spinner:**")
spinner_test = st.button("Trigger Spinner 🌀")
if spinner_test:
    with st.spinner("Wait!"):
        time.sleep(3)
        st.write("spinner works if you saw it!")

st.write("**Balloons:**")
test = st.button("Trigger Balloons 🎈")
if test:
    st.balloons()

st.write("**Snow:**")
test_2 = st.button("Trigger Snow ❄️")
if test_2:
    st.snow()

st.write("**Error:**")
st.error("st error")

st.write("**Warning:**")
st.warning("st warning")

st.write("**Info:**")
st.info("st info")

st.write("**Success:**")
st.success("st success")

st.write("**Exception:**")
st.exception(RuntimeError("example of error"))
