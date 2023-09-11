#!/usr/bin/python3
"""This module contains ('4-inherits_from') fuction"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    args: obj - object
          a_class - class

    returns: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
