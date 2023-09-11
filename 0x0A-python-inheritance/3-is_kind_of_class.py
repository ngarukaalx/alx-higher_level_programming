#!/usr/bin/python3
"""This module contains ('is_kind_of_class') fuction"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or
    if the object is an instance of a class that inherited from, the
    specified class ; otherwise False.

    args: obj - object to be checked
          a_class - class to compare with

    returns: True or False
    """
    return isinstance(obj, a_class)
