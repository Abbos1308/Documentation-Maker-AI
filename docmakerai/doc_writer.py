from .groq import call_groq
from .prompts import system_prompt_writer as system_prompt

def doc_writer(info):
    resp = call_groq([{"role": "user", "content": info}], system_prompt=system_prompt)
    return resp["choices"][0]["message"]["content"]



