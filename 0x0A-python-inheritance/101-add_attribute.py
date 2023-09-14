#!/usr/bin/python3
"""This module contains a fuction  that adds
a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr_name, attr_val):
    """adds a new attribute to an object if it’s possible

    args:
         obj (object): The object to add to
         attr_name (str) The name of attribute
         attr_val: The value of attribute

    Raises:
          TypeError: if the object can’t have new attribute

    Returns:
            None
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_val)
    else:
        raise TypeError("can't add new attribute")
