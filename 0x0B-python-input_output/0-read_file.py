#!/usr/bin/python3
"""
Module for the def read_file(filename="")
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end="")
