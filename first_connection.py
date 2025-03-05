# Import the required libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Fetch API keys & instantiate 
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

message = "How are Open AI sales since the arrival of deepseek?"
response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)