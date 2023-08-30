#!/usr/bin/python3
"""Defines class square"""


class Square:
    """Defines class square"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        else:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        if isinstance(position, tuple) and len(position) == 2 and \
                all(isinstance(va, int) and va >= 0 for va in position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 \
                and all(isinstance(va, int) and va >= 0 for va in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
