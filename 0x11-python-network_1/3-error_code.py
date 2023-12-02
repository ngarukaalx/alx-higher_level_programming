#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    """execute only when run directly"""

    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            if response.getcode() == 200:
                the_page = response.read().decode('utf-8')
                print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
