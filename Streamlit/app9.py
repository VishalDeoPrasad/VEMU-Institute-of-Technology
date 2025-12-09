import streamlit as st
import pandas as pd

file = st.file_uploader("Choose a file", type='csv')

if file:
    df = pd.read_csv(file)
    st.write(df)