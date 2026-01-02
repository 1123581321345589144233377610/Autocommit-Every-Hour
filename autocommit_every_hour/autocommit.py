from datetime import datetime
import requests

USERNAME = 'YOUR_GITHUB_USERNAME'
REPOSITORY = 'YOUR_GITHUB_REPOSITORY_NAME'
TOKEN = 'YOUR_GITHUB_TOKEN'

def create_empty_commit() -> None:
    branch_info = requests.get(f'https://api.github.com/repos/{USERNAME}/{REPOSITORY}/branches/main', auth = (USERNAME, TOKEN)).json()
    parent_sha = branch_info['commit']['sha']
    tree_sha = branch_info['commit']['commit']['tree']['sha']
    commit_data = {
        'message': f"Autocommit  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        'tree': tree_sha,
        'parents': [parent_sha]
    }
    new_commit = requests.post(f'https://api.github.com/repos/{USERNAME}/{REPOSITORY}/git/commits', 
                               auth = (USERNAME, TOKEN), 
                               json = commit_data).json()
    reference_update = {
        'sha': new_commit['sha'],
        'force': True
    }
    requests.patch(f'https://api.github.com/repos/{USERNAME}/{REPOSITORY}/git/refs/heads/main',
                   auth = (USERNAME, TOKEN),
                   json = reference_update)