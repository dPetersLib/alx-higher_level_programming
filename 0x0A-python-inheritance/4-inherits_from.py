#!/usr/bin/python3
"""
Module for inherits_from(obj, a_class): function that returns True if the
object is an instance of a class that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function that determine if a class is an inherited class.
    Args:
        obj (object any type): The object to analyze.
        a_class (object any type): The reference object.
    Returns:
         Returns True if the object is an instance of a class that
         inherited (directly or indirectly) from the specified class ;
         otherwise False.
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
