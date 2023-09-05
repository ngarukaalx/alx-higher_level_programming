#!/usr/bin/python3
"""This module prints your first and second name"""


def say_my_name(first_name, last_name=""):
    """This fuction prints your first and second name

    args:first_name(string) first argument
        :last_name(string) second argument

    raises: TypeError if argument provided not a string
    """

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))

    else:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
