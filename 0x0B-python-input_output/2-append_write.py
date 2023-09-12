#!/usr/bin/python3
"""This module contains a fuction that appends a string at
the end of a text file  and returns the number of characters added
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file

    args: filename (str) - The file to append a text to
        : text (str) - The text to append

    Returns: 
        int: Returns the number of characters added:
    """

    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
