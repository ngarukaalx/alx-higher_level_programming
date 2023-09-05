#!/usr/bin/python3
"""This module contains a fuction that prints a spuare with character #"""


def print_square(size):
    """This fuction prints a spuare with char #

    args: size(int) - size of square

    raises: TypeError - if size not an interger
                        or if size is a float and is less than 0
            ValueError - if size is less than zero
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
