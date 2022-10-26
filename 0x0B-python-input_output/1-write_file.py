#!/usr/bin/python3
"""
Module for the write_file(filename="", text="") that writes a string to a text
file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns the number
    of characters written.
    Args:
        filename (str): The file name
        text (str): String to write
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
