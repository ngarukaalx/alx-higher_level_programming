#!/usr/bin/python3
"""This module contains a  function that writes an
Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation

    args: my_obj(object) - Object to be written using JSON representation
          filename - Text file to be wrritten to
    Returns:
            None
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        json_text = json.dumps(my_obj)
        my_file.write(json_text)
