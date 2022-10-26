#!/usr/bin/python3
"""
Module for the save_to_json_file(my_obj, filename) that writes an Object to a
text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (object): Surce object
        filename (str): The file name
    Returns:
        JSON representation.
    """
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(my_obj, f)
