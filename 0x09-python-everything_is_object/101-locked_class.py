#!/usr/bin/python3
"""This module contains a class that
prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """ class LockedClass"""
    __slots__ = ('first_name',)
