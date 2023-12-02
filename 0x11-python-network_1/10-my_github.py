#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    """Only when run directly"""

    user_name = sys.argv[1]
    pass_wd = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(user_name, pass_wd))
    user_data = r.json()
    user_id = user_data['id']
    print(user_id)
