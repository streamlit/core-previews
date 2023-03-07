import streamlit as st

st.title("📝 Text Element Tester")
st.write("Testing all text elements in one place.")

st.write("**Markdown:**")
st.markdown("This is an example of **Streamlit** *Markdown* :green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.write("**Title:**")
st.title('Title with _italics_, :blue[colors], & :sunglasses:')

st.write("**Header:**")
st.header("Header with _italics_, :violet[colors], & :dog:")

st.write("**Subheader:**")
st.subheader("Subheader with _italics_, :red[colors], & :tada:")

st.write("**Caption:**")
st.caption("This is an example of a caption with _italics_ :orange[colors] and emojis 💻")

st.write("**Code:**")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.write("**Text:**")
st.text("This is an example of text")

st.write("**Latex:**")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write("**Magic:**")
"""
hello magic
"""