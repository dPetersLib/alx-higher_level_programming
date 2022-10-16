#!/usr/bin/python3
"""Say my name Module
"""


def say_my_name(first_name, last_name=""):
    """Function to print users name

    It takes the name as argument and prints it to the user.

    Args:
        first_name (string): The user's first name
        last_name (string): The User's last name

    Note:
        first_name and last_name must be strings.
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("{} {}".format(first_name, last_name))
