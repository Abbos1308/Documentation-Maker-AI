# 📄 Codereviewer

> AI-powered documentation generator for GitHub repositories — fetch, extract, and document any repo in seconds.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini-orange?logo=google&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq-purple?logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 🔍 Fetches repository information directly from GitHub
- 📂 Extracts and filters relevant source files
- 🤖 Uses AI (Gemini + Groq) to generate human-readable documentation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.12+ |
| AI Providers | Gemini, Groq |
| Core Deps | `gemini`, `git_pull`, `regex`, `scouter`, `doc_writer`, `groq` |

---

## ⚙️ Requirements

- Python 3.12+
- `GEMINI_API_KEY` — [Get it here](https://aistudio.google.com/)
- `GROQ_API_KEY` — [Get it here](https://console.groq.com/)
- `TOKEN` — Personal GitHub access token

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Abbos1308/Documentation-Maker-AI.git
cd codereviewer

# 2. Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate        # Linux/Mac
# myenv\Scripts\activate         # Windows

# 3. Install the package
pip install .


# 4. Set environment variables
export GEMINI_API_KEY=your_gemini_key
export GROQ_API_KEY=your_groq_key
export TOKEN=your_github_token
```

---

## Or you can install the package directly from PyPi:
```bash
pip install docmakerai
```

## ⚡ Quickstart

```bash
python main.py https://github.com/owner/repo.git
```

Or use it programmatically:

```python
from docmakerai.generator import generate

print(generate("https://github.com/owner/repo.git","your_git_token_here","your_ai_api_key_here"))
```

---

## 🔧 Configuration

All configuration is done via environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Gemini API Key | ✅ Yes |
| `GROQ_API_KEY` | Groq API Key | ✅ Yes |
| `TOKEN` | Personal GitHub access token | ✅ Yes |

---

## 📁 Project Structure

```
codereviewer/
├── main.py          # Entry point — run from CLI
├── doc_writer.py    # Core documentation generation logic
└── pyproject.toml   # Project metadata & dependencies
```

---

## 📖 API Reference

### `generate(link: str,git_token,ai_token) -> str`

Generates documentation for a given GitHub repository.

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `link` | `str` | Full URL of the GitHub repository |

**Returns:** `str` — The generated documentation.

**Example:**

```python
from docmakerai.generator import generate 

docs = generate("https://github.com/owner/repo.git","your_git_token_here","your_ai_api_key_here")
print(docs)
```

---

## ❗ Error Reference

| Error Message | Cause |
|---------------|-------|
| `ERROR: Failed to fetch repository. Could be deleted or private. Please check and retry` | Repo is private, deleted, or the token is invalid |
| `ERROR: Failed to connect with AI. Please try again in few minutes` | AI service is unreachable or rate-limited |
