#!/usr/bin/python3
"""
Module for the load_from_json_file(filename) that creates an Object from a JSON
file.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file.
    Args:
        filename (str): The file name
    Returns:
        Python object representation.
    """
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)
