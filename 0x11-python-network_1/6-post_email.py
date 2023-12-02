#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and
finally displays the body of the
"""

import sys
import requests

if __name__ == "__main__":
    """only if run direct"""

    url = sys.argv[1]
    r = requests.post(url, data={sys.argv[2]})
    text_body = f"Your email is: {r.text}"
    print(text_body)
