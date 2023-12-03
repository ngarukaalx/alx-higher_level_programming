#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
"""

import requests
import sys

if __name__ == "__main__":
    """Execute only when when run directly"""

    repo = sys.argv[1]
    user = sys.argv[2]

    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            name = commit['commit']['author']['name']
            print(f"{sha}: {name}")
