import google.generativeai as genai

key = "AIzaSyAtZ_u2ernbJCwhgMo3TVC6aKe8kGm9NvA"
genai.configure(api_key=key)

model = genai.GenerativeModel(model_name='gemini-2.5-flash')

chat = model.start_chat()

response = chat.send_message("give me python code for find factorial.")
print(response.text)