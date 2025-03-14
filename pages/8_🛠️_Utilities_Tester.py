import pandas
import streamlit as st

st.set_page_config(
    page_title="Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": "# This is a header. This is an *extremely* cool app!"},
)

st.title("🛠️ Utilities Tester")
st.write("Testing all utilities in one place.")

st.write("**Page Config:**")
st.caption(":blue[Check the following page config items worked:]")
st.caption(":blue[1) sidebar collapsed]")
st.caption(":blue[2) wide layout]")
st.caption(":blue[3) page title & icon changed in the tab]")
st.caption(":blue[4) hamburger menu **About** link generates custom modal]")

st.write("**Set Query Params:**")
st.query_params.from_dict({"show_map": True, "selected": ["asia"]})
st.write(
    ":violet[Check the url above to confirm it includes `show_map`=True and `selected`= asia]"
)


st.write("**Get Query Params:**")
st.write(st.query_params)

st.write("**Echo:**")


def get_user_name():
    return "John"


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return "!!!"

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(":green[Result:]", greeting, value, punctuation)

st.write("**Help:**")
st.help(pandas.DataFrame)
