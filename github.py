import requests


def get_github_repos(username: str) -> list[str]:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        data_repos = [i['full_name'] for i in response.json()]
    else:
        data_repos = []

    return data_repos




if __name__ == "__main__":
    repos = get_github_repos('octocat')
    print(repos)