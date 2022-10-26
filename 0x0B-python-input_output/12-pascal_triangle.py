#!/usr/bin/python3
"""
Module for the function: pascal_triangle(n)
"""


def pascal_triangle(n):

    """
    function that returns a list of lists of integers representing the Pascals
    triangle of size n
    Args:
        n (int): How many lists
    Returns:
        List of lists with the integer values according to the Pascal Triangle.
    """
    t_angle = list()
    if n <= 0:
        return t_angle
    t_angle.append([1])
    if n == 1:
        return t_angle
    for i in range(1, n):
        t_angle.append(list())
        t_angle[i].append(1)
        for j in range(1, i):
            t_angle[i].append(t_angle[i-1][j-1] + t_angle[i-1][j])
        t_angle[i].append(1)
    return t_angle
