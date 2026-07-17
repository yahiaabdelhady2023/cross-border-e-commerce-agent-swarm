
import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

res = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
      "Authorization":f"Bearer {OPENROUTER_API_KEY}"
  },
  data=json.dumps({
      "model":"openrouter/free",
      "messages":[{
          "role":"user",
          "content":"what is 1+1?"
      }]
  })
)

print("res is ",res)
print("res is ",res.text)