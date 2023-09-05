#!/usr/bin/python3
"""This module contains a fuction that prints a text with 2 new lines
    after each these characters: ., ? and :
"""


def text_indentation(text):
    """Fuction to perform the printing

    args: text(string) text to be printed

    raises: TypeError if text not string
    """
    is_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text) and text[char] == " ":
        char += 1
    while char < len(text):
        if is_space and text[char] == " ":
            continue
        print(text[char], end="")
        if text[char] in [".", "?", ":"]:
            print("\n\n", end="")
            is_space = True
            char += 1
        else:
            is_space = False
        char += 1
