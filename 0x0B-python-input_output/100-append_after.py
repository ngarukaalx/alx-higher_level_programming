#!/usr/bin/python3
"""This module contains fuction that nserts a line of text
to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file, after each
    line containing a specific string

    args: filename(str) - name of file
          search_string(str) - string to search
          new_string - string to insert
    Returns:
            returns nothing
    """
    new_text = []
    with open(filename, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            new_text.append(line)
            if search_string in line:
                new_text.append(new_string)
    with open(filename, 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_text)
