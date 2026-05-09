import re

def parse_github_repo(url: str) -> tuple[str, str]:
    url = url.strip().rstrip('/')
    
    # Strip .git suffix
    if url.endswith('.git'):
        url = url[:-4]
    
    # Match both https://github.com/owner/repo and github.com/owner/repo
    match = re.search(r'github\.com[/:]([^/]+)/([^/]+)', url)
    
    if not match:
        raise ValueError(f"Can't parse GitHub URL: {url}")
    
    return match.group(1), match.group(2)

def extract_file_paths(selector_output: str) -> list[str]:
    match = re.search(r'```paths\n(.*?)```', selector_output, re.DOTALL)
    if not match:
        return []
    return [line.strip() for line in match.group(1).strip().splitlines() if line.strip()]


def prompt_maker(files,selector_output):
    prompt = ""
    def build_file_block(path: str, code: str) -> str:
        return f'<file path="{path}">\n{code}\n</file>'

    all_files = "\n\n".join(build_file_block(p, c) for p, c in files.items())
    payload = f"""
    [selector AI full output]
    {selector_output}

    [file blocks]
    {all_files}
    
    """
    return payload