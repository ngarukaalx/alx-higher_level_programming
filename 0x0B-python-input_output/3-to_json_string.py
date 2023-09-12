#!/usr/bin/python3
"""This module contains a fuction hat returns the JSON
representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """Fuction that returns the JSON representation
    of an object (string)

    args:
        my_obj (str)  - object (string)

    Returns:
          str: JSON representation of an object (string)
    """
    return json.dumps(my_obj)
