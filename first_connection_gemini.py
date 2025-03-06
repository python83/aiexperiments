# Import the required libraries
import ollama 

MODEL = "llama3.2"

message = "What hardware specs do you need to run well"

stream = ollama.chat(
  model= MODEL,
  messages=[{'role': 'user', 'content': message}],
  stream=True
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)


