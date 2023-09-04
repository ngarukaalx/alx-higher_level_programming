#!/usr/bin/python3
"""This module defines a rectangle class"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        if isinstance(width, int) and width >= 0:
            self.__width = width
        else:
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
        if isinstance(height, int) and height >= 0:
            self.__height = height
        else:
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Retrives width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""

        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Retrives height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""

        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Gets the area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returs perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ print the rectangle with the character #"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for _ in range(self.__height):
            for _ in range(self.__width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        return f"Rectangle({self.__width}, {self.__height})"
