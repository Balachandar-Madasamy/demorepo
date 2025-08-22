import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-pro')

response = model.generate_content('Hii I am Bala')
out = response.text

def calling(prompt):
    response = model.generate_content(prompt)
    return response.text