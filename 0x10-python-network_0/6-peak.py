#!/usr/bin/python3
"""this module's fuction returns a peak in a list"""


def find_peak(list_of_integers):
    """Returns a peak in list_of_integers
    args:
        list_of_integers - list of intergers
        Return: peak
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    for i in range(1, size - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and \
                list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[size - 1] >= list_of_integers[size - 2]:
        return list_of_integers[size - 1]
    return None
