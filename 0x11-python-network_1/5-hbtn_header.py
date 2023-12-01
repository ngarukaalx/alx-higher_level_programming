#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    """not execute if run directly"""

    url = sys.argv[1]

    r = requests.get(url)
    x_value = r.headers.get('X-Request-Id')
    print(x_value)
