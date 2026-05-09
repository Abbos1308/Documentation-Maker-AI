from .groq import call_groq
from .prompts import system_prompt_scouter as system_prompt
def scouter(info, ai_token,readme="None"):
    resp = call_groq([{"role": "user", "content": info}], system_prompt=system_prompt)
    return resp["choices"][0]["message"]["content"]


info = "{'name': 'Aiogram3Template', 'languages': {'Python': 23033}, 'tree': ['README.md', 'bot', 'bot/config', 'bot/config/__pycache__', 'bot/config/__pycache__/settings.cpython-311.pyc', 'bot/config/settings.py', 'bot/database', 'bot/database/__pycache__', 'bot/database/__pycache__/models.cpython-311.pyc', 'bot/database/__pycache__/queries.cpython-311.pyc', 'bot/database/models.py', 'bot/database/queries.py', 'bot/handlers', 'bot/handlers/__pycache__', 'bot/handlers/__pycache__/admin.cpython-311.pyc', 'bot/handlers/__pycache__/user.cpython-311.pyc', 'bot/handlers/admin.py', 'bot/handlers/user.py', 'bot/keyboards', 'bot/keyboards/__pycache__', 'bot/keyboards/__pycache__/admin.cpython-311.pyc', 'bot/keyboards/__pycache__/user.cpython-311.pyc', 'bot/keyboards/admin.py', 'bot/keyboards/user.py', 'bot/middlewares', 'bot/middlewares/__pycache__', 'bot/middlewares/__pycache__/admin.cpython-311.pyc', 'bot/middlewares/admin.py', 'bot/utils', 'bot/utils/__pycache__', 'bot/utils/__pycache__/helpers.cpython-311.pyc', 'bot/utils/helpers.py', 'main.py', 'requirements.txt']}"


