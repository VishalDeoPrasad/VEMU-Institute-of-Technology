import streamlit as st

option = ['Python', 'Machine Leaning', 'Data Science', 'Deep Learning', 'AI']
choice = st.selectbox("Select Your Choice", option)

if choice:
    st.write("You Selected: ", choice)