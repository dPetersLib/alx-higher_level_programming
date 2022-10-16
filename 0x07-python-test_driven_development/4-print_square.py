#!/usr/bin/python3
""" Print Square Module

The main function of this module is to
function that prints a square with the character #
"""


def print_square(size):
    """The function that does the magic

    Args:
        size (int): the size length of the square.
            It denotes how many times the character #
            is to be printed.

    Note:
        size must be a positive integer.
    """

    # validations

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    # printing if all validations pass

    for i in range(size):
        print("#" * size)
