#!/usr/bin/python3
"""This module contains class Rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """class rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        args:
             width - width
             height - height
             x - x
             y - y
             id(int) - id
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """public getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """public setter for width
        args:
                value - value to set
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """public getter for height"""
        return self.__height

    @property
    def height(self):
        """public getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """public setter for height
        args:
            value - value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """public getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """public setter for x
        args:
            value - value for x
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        args:
            value - value of y
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle instance with # representation"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns rectangle str representation of rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
