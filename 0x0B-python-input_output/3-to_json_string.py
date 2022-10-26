#!/usr/bin/python3
"""
Module for the function to_json_string(my_obj) that returns the JSON
representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object.
    Args:
        my_obj (str): Surce object
    Returns:
        JSON representation.
    """
    return json.dumps(my_obj)
