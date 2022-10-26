#!/usr/bin/python3
"""
Module for the append_write(filename="", text="") function that appends a
string at the end of a text file (UTF8) and returns the number of characters
added.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8) and returns
    the number of characters added.
    Args:
        filename (str): The file name
        text (str): String to write
    Returns:
        The number of characters written
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
