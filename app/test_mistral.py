# test_mistral.py
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mistral-medium",
    "messages": [{"role": "user", "content": "Say hello"}],
    "temperature": 0.2
}

response = httpx.post(os.getenv("MISTRAL_ENDPOINT"), headers=headers, json=payload)
print(response.status_code)
print(response.text)
