#!/usr/bin/python3
"""This module contains a fuction that reads tesxt files
and prints it to stdout
"""


def read_file(filename=""):
    """fuction that read text files and print to stdout
    args: filename (str): The name of the file to be read.

    Returns:
            None
    """
    with open(filename, encoding='utf-8') as my_file:
        for line in my_file:
            print("{}".format(line), end="")
