#!/usr/bin/python3
"""This module contains a function that creates
an Object from a “JSON file”
"""


import json
def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    args: filename (str) - JSON file

    Returns:
            Object created
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        created_oject = json.load(my_file)
    return created_oject
