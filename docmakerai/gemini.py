import os
import requests


BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = "gemini-2.5-flash"

def call_gemini(messages,API_KEY,resp_type=None, system_prompt=None):
    url = f"{BASE_URL}/{MODEL}:generateContent?key={API_KEY}"

    body = {"contents": messages}

    if system_prompt:
        body["systemInstruction"] = {
            "parts": [{"text": system_prompt}]
        }


    response = requests.post(url, json=body)
    response.raise_for_status()
    return response.json()

