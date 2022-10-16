#!/usr/bin/python3
"""Matrix Division
This module handles matrix division by a dividen.
"""


def matrix_divided(matrix, div):
    """This is the division function

    Args:
        matrix (list): Matrix (list of lists)
        div (int): the dividen

    Returns:
        A new matrix with is the previous matrix divided by div.

    Note:
        div must be a number integer or float
        div cannot be zero
        matrix must be a list of lists of integer/float
    """

    # div is number
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    # div cannot be zero
    if div == 0:
        raise TypeError("division by zero")

    if len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    lengths = []
    """This is to hold the unique values of the length of each row"""

    for row in range(len(matrix)):
        # i must be list
        if type(matrix[row]) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        # a list of integer or float
        for col in matrix[row]:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

        # len i's must be same
        if len(matrix[row]) not in lengths:
            lengths.append(len(matrix[row]))

    if len(lengths) > 1:
        raise TypeError("Each matrix[row] of the matrix must \
have the same size")

    return [[round((i / div), 2) for i in matrix[row]]
            for row in range(len(matrix))]
