from google import genai
from dotenv import load_dotenv
import os


# Load the Gemini API Key
load_dotenv(override=True)
api_key = os.getenv('GEMINI_API_KEY')

# Create a client
client = genai.Client(api_key=api_key)

# Test Query
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Whats the capital of Turkey",
)

print(response.text)