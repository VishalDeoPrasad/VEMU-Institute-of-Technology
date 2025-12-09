import streamlit as st
import google.generativeai as genai

key = "AIzaSyAtZ_u2ernbJCwhgMo3TVC6aKe8kGm9NvA"
genai.configure(api_key = key)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")
chat = model.start_chat()

st.title("Vishal AI Chatbot")
input = st.text_area("Enter Your Quesiton:")

if st.button("Ask"):
    response = chat.send_message(input)
    st.subheader("Response")
    st.write(response.text)