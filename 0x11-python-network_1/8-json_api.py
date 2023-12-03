#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    """run only when run directly"""

    q = {'q': sys.argv[1]} if sys.argv[1:] else {'q': ""}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=q)
        respond = r.json()
        if r.status_code == 204:
            # no result
            print("No result")
        elif respond:
            for key, value in respond.items():
                if key == 'id':
                    print("[{}] ".format(value), end="")
                elif key == 'name':
                    print("{}".format(value))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
