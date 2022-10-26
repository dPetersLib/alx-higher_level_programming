#!/usr/bin/python3
"""
Module for class MyList that inherits from list.
"""


class MyList(list):
    """
    Class MyList inherits from list and let print ordered lists.
    """
    def print_sorted(self):
        """
        Method that that prints the list, but sorted (ascending sort).
        """
        new = list()
        for i in self:
            new.append(i)
        new.sort()
        print(new)
