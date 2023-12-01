#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
 The body of the response must be displayed like the following example
 (tabulation before -)
"""

import urllib.request

if __name__ == "__main__":
    """Execute only when run directly"""

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        output_formated = (
                f"Body response:\n"
                f"\t- type: {type(the_page)}\n"
                f"\t- content: {the_page}\n"
                f"\t- utf8 content: {the_page.decode('utf-8')}"
                )
        print(output_formated)
