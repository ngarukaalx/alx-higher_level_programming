#!/usr/bin/python3
"""This module contains a classMyInt that inherits from int"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __init__(self, value):
        """instanization with value"""
        self.value = value

    def __eq__(self, element):
        """inverts the behaviour of =="""
        return super().__ne__(element)

    def __ne__(self, element):
        """Inverts the behaviour of !="""
        return super().__eq__(element)
