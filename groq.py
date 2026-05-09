import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.environ.get("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

def call_groq(messages, system_prompt=None, max_retries=5):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    all_messages = []
    if system_prompt:
        all_messages.append({"role": "system", "content": system_prompt})
    all_messages.extend(messages)

    body = {"model": MODEL, "messages": all_messages}

    for attempt in range(max_retries):
        response = requests.post(BASE_URL, json=body, headers=headers)

        if response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 2 ** attempt))
            time.sleep(wait)
            continue

        response.raise_for_status()
        return response.json()

    raise Exception(f"Failed after {max_retries} attempts — still rate limited.")
