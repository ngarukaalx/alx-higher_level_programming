#!/usr/bin/python3
"""This module contains  a function that writes a string to a text file
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """fuction to write a string to a text file

    args: filename (str): The name of the text file to be written to
          text: The text to be written to the file.

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
