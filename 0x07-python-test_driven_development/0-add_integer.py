#!/usr/bin/python3
"""THIS module contains a fuction that adds 2 numbers in int of float format"""


def add_integer(a, b=98):
    """Fuction to add two intergers

    args:
        a(int or float): The first number.
        b(int or float, optipnal): The second number.

    Returns:
        int: The sum of 'a' and 'b'.

    Raises:
            TypeError: If `a` or `b` is not an integer or float.
    """
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if isinstance(b, float):
            b = int(b)
        if isinstance(a, float):
            a = int(a)
        return a + b
    else:
        if (not isinstance(a, (int, float))):
            raise TypeError("a must be an integer")
        if (not isinstance(b, (int, float))):
            raise TypeError("b must be an integer")
