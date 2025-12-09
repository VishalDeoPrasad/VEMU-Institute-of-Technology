import streamlit as st
import pandas as pd

st.title("This is my First Web Application!")
st.write("Welcome to 45 Days of Machine Learning!")

data = {
    'Name':['Rahul', 'Ravi', 'Ruhi', 'Pooja', 'Vishal'],
    'Age':[15, 20, 25, 28, 31],
    'Marks': [89, 45, 78, 90, 99],
}

df = pd.DataFrame(data)

st.write(df)