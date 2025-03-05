# Import the required libraries
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI


# Fetch API keys & instantiate 
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# Avoid issues with fetching sites
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Class to capture web content
class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

def summarize (url):

    # Lets grab info for Rpi, one of my favorite products
    website = Website(url)

    # Prompts for AI
    system_prompt = "Analyse this content from a website and give me a summary of its products in markdown"
    user_prompt = website.text

    # Compile a message for the API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # Send request to AI
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

    return response

# Print Summary of Website 
summary = summarize("http://www.raspberrypi.org")
print(summary.choices[0].message.content)
