#!/usr/bin/python3
"""Defines a rectacle"""


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height

        args: width (int): the rectangles width
              height (int): the height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def height(self):
        """fuction to retrive height"""

        return self.__height

    @height.setter
    def height(self, value):
        """fuction to set height"""

        if value < 0:
            raise ValueError("height must be >= 0")
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """fuction to retrive height"""

        return self.__width

    @width.setter
    def width(self, value):
        """fuction to set witdth"""

        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
