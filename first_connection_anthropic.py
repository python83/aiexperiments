import anthropic
from dotenv import load_dotenv
import os


# Load the Gemini API Key
load_dotenv(override=True)
api_key = os.getenv('ANTHROPICS_API_KEY')

client = anthropic.Anthropic(api_key=api_key )

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    temperature=1,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why are you better than Open AI ?"
                }
            ]
        }
    ]
)
print(message.content)