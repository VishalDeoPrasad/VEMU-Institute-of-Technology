import pandas as pd
import streamlit as st

st.title("This is Cars24 Dataset Chart")

df = pd.read_csv("Cars24 data.csv")

st.line_chart(df['selling_price'])
st.area_chart(df['selling_price'])
st.bar_chart(df['km_driven'])
