import jsn

import requests

def get_github_users(users):
    results = []
    for user in users:
        status, user_data = get_user_info(user)
        if not status:
            continue

        status, repositories = get_user_repos(user)
        if not status:
            continue

        result = {
            'login': user_data['login'],
            'public_repos': user_data['public_repos'],
            'repositories': repositories
        }
        results.append(result)
    return json.dumps(results)

def get_user_info(user: str) -> tuple[bool, dict]:
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    if response.status_code != 200:
        return False, {}
    return True, response.json()

def get_user_repos(user: str) -> tuple[bool, list]:
    repo_url = f"https://api.github.com/users/{user}/repos"
    repo_response = requests.get(repo_url)
    if repo_response.status_code != 200:
        return False, []
    return True, [repo['name'] for repo in repo_response.json()]
