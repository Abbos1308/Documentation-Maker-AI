from .gemini import call_gemini
from .git_pull import get_repo_info , code_extractor
from .regex import parse_github_repo, extract_file_paths, prompt_maker
from .scouter import scouter
from .doc_writer import doc_writer
import json



def generate(link:str):
    try:
        owner , repo = parse_github_repo(link)
        info = json.dumps(get_repo_info(owner,repo))
    except:
        return "ERROR: Failed to fetch repository. Could be deleted or private. Please check and retry"
    try:
        tree = scouter(info)
        files_to_read = extract_file_paths(tree)
        codes = code_extractor(owner,repo,*files_to_read)
        payload = prompt_maker(codes,tree)
        doc = doc_writer(payload)
    except:
        return "ERROR: Failed to connect with AI. Pleade try again in few minutes"
    return doc


