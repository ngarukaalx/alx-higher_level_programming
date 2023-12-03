#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    """run only when run directly"""

    letter = sys.argv[1]

    q = {'q': sys.argv[1]} if sys.argv[1] else {'q': ""}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=q)
        respond = r.json()
        if r.status_code == 204:
            # no result
            print("No result")
        elif respond:
            for item in respond:
                if 'id' in item and 'name' in item:
                    print("[{}] {}".format(item['id'], item['name']))
    except json.JSONDecodeError:
        print("Not a valid JSON")
