#!/usr/bin/python3
"""
Module for the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after each line containing
    a specific string.
    Args:
        filename (str): The file name
        search_string (str): The searching string
        new_string (str): The new line string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        content = "".join(lines)
        f.write(content)
