#!/usr/bin/python3
"""This module contains a fuction that
returns the list of available attributes
"""


def lookup(obj):
    """returns the list of available
    attributes and methods of an object:

    args: obj

    returns: he list of available attributes
    and methods of an object
    """
    return dir(obj)
