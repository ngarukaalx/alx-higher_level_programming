#!/usr/bin/python3
"""This module contains fuction is_same_class that
returns True if the object is exactly an instance of the
specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    args: obj - object to be checked
          a_class - specified class

    return: True if exactly instance False if otherwise
    """
    return type(obj) is a_class
