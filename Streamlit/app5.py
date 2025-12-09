import streamlit as st

st.title("Student Details Form:")

name = st.text_input("Enter Your Name: ")
age = st.number_input("Enter Your Age: ")
roll = st.text_input("Enter Your Roll Number: ")

tech = st.selectbox("Select Technology:", 
            ["Python", "C", "C++", "Java", "Machine Learning", "AI", "Data Science"])

branch = st.selectbox("Select Your Branch:",
            ["CSE", "CS AI", "CS ML", "CS DS", "CS IT"])

if st.button("Submit"):
    st.write("Name: ", name)
    st.write("Age: ", age)
    st.write("Roll Number: ", roll)
    st.write("Techology: ", tech)
    st.write("Branch: ", branch)