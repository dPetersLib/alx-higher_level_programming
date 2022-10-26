#!/usr/bin/python3
"""
Module for the function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    Args:
        obj: The object
    Returns:
        The dictionary description
    """
    return obj.__dict__
