import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = "gemini-2.5-flash"

def call_gemini(messages,resp_type=None, system_prompt=None):
    url = f"{BASE_URL}/{MODEL}:generateContent?key={API_KEY}"

    body = {"contents": messages}

    if system_prompt:
        body["systemInstruction"] = {
            "parts": [{"text": system_prompt}]
        }


    response = requests.post(url, json=body)
    response.raise_for_status()
    return response.json()

