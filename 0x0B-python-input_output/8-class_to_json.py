#!/usr/bin/python3
"""This module contains a fuction ('8-class_to_json')"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    args: obj - Is an instance of a Class

    Returns:
            returns a dictionary
    """
    dict_result = {}

    objec_dict = vars(obj)

    for name, value in objec_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dict_result[name] = value
    return dict_result
