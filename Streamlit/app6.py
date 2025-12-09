import streamlit as st

st.title("Student Percentage Calculator!")

python = st.number_input("Enter Python Marks: ")
maths = st.number_input("Enter Maths Marks: ")
ml = st.number_input("Enter ML Marks: ")
ds = st.number_input("Enter DS Marks: ")
ai = st.number_input("Enter AI Marks: ")
nlp = st.number_input("Enter NLP Marks: ")
cv = st.number_input("Enter CV Marks: ")
dl = st.number_input("Enter DL Marks: ")

if st.button("Calculate percentage"):
    total_marks = python+maths+ml+ds+ai+nlp+cv+dl
    percentage = (total_marks/800)*100

    st.write("Total Marks: ", total_marks)
    st.write("Percentage: ", percentage)