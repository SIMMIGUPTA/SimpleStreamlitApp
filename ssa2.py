import streamlit as st
st.title("Hello World")

st.title('Simple Streamlit App')

s = st.text_input('Type a name in the box below')

st.write(f'Hello {s}')
