#!/usr/bin/python3
"""
Module for is_same_class(obj, a_class) function that returns True if the object
is exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that determine the type of class.
    Args:
        obj (object any type): The object to analyze.
        a_class (object any type): The reference object.
    Returns:
         Returns True if the obj is exactly an instance of the specified
         a_class ; otherwise False.
    """
    return type(obj) is a_class
