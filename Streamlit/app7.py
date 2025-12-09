import streamlit as st

age = st.slider("Age", 0, 100, 18)

if age >= 18:
    st.write("You are Eligible to Vote!")
else:
    st.write("You are not Eligible to Vote!")
