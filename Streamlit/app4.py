import streamlit as st

st.title("Enter Your Name: ")
name = st.text_input("Name")

if name:
    st.write("Welcome to class: ", name)
