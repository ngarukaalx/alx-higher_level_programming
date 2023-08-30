#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        else:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
