#!/usr/bin/python3
"""
Lookup modul for listing of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Function that returns the list of available attributes and methods of an
    object.
    Args:
        obj (object any type): The object to analyze.
    Returns:
        A list object of available attributes and methods of an object.
    """
    return dir(obj)
