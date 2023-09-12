#!/usr/bin/python3
"""This module contains a fuction that returns an object
(Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string

    args: my_str(str) - JSON string

    Returns:
        Returns an object (Python data structure)
    """
    return json.loads(my_str)
