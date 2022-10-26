#!/usr/bin/python3
"""
Module for is_kind_of_class(obj, a_class): function that returns True if the
object is an instance of, or if the object is an instance of a class that
inherited from, the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that determine if a class is a specific class or an inherited
    class.
    Args:
        obj (object any type): The object to analyze.
        a_class (object any type): The reference object.
    Returns:
         Returns True if the obj is exactly an instance of the specified
         a_class ; otherwise False.
    """
    if type(obj) is a_class:
        return True
    return isinstance(obj, a_class)
