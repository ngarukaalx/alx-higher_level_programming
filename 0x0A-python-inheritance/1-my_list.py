#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """base class that inherits form list"""

    def print_sorted(self):
        """public instance method that prints
        the list but sorted(ascendind sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
