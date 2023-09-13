#!/usr/bin/python3
"""This module contains fuction ('pascal_triangle') that returns
a list of intergers representing the pascal's triangle
"""


def pascal_triangle(n):
    """Fuction that returns a list of lists of integers representing
    the Pascal’s triangle of n

    args: n(int) - tringle size

    Returns:
            returns a list of lists of integers representing
            the Pascal’s triangle of n
    """

    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = [1]
        for j in range(1, i):
            data = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(data)
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
