import pandas as pd
import streamlit as st

st.title("This is Cars24 Dataset")

df = pd.read_csv("Cars24 data.csv")
st.write(df)
