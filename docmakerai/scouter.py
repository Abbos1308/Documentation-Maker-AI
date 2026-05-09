from .groq import call_groq
from .prompts import system_prompt_scouter as system_prompt
def scouter(info, ai_token,readme="None"):
    resp = call_groq([{"role": "user", "content": info}], API_KEY=ai_token,system_prompt=system_prompt)
    return resp["choices"][0]["message"]["content"]

