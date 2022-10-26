#!/usr/bin/python3
"""
Module for the from_json_string(my_str) function that returns an object (Python
data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a
    JSON string.
    Args:
        my_str (str): String with the JSON
    Returns:
        A python object
    """
    return json.loads(my_str)
