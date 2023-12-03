#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    """Not to be executed when imported"""

    r = requests.get('https://alx-intranet.hbtn.io/status')

    responses = (
            f"Body response:\n"
            f"\t- type: {type(r.text)}\n"
            f"\t- content: {r.text}\n"
            )
    print(responses, end="")
