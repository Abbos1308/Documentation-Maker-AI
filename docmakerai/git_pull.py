import requests
import os

def get_repo_info(owner, repo,token):
    h = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    base = f"https://api.github.com/repos/{owner}/{repo}"

    info  = requests.get(base, headers=h).json()
    langs = requests.get(f"{base}/languages", headers=h).json()
    tree  = requests.get(f"{base}/git/trees/HEAD", headers=h, params={"recursive":"1"}).json()
    return {
        "name":      info["name"],
        "languages": langs,
        "tree":      [i["path"] for i in tree["tree"]]
    }


def code_extractor(owner, repo, *files, branch="main"):
    results = {}
    for file in files:
        try:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/{branch}/{file}"
            res = requests.get(url)  # no auth header for public repos
            results[file] = res.text
        except:
            pass
    return results

