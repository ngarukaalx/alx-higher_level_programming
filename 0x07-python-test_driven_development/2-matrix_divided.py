#!/usr/bin/python3
"""This module contains a fuction that divides
each element of a matrix with a number"""


def matrix_divided(matrix, div):
    """Fuction to divide a matrix by a number.

    Args:
        matrix:Made of lists, values in list(int, float)
        div:(int, float) number to divided with

    Returns:
        list: Each number in list divided by div

    Raises:
        TypeError: matrix must be a matrix (list of lists)
        of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) and
               all(isinstance(val, (int, float)) for val in row)
               for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    size_row = len(matrix[0])

    if not all(len(row) == size_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(div / 3, 2) for div in row] for row in matrix]
    return new_matrix
