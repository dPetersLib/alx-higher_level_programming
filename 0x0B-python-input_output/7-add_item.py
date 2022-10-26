#!/usr/bin/python3
"""
Module to write a script that adds all arguments to a Python list, and then
save them to a file.
"""

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

ctrl = 0
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = list()
for i in sys.argv:
    if ctrl == 0:
        ctrl = 1
    else:
        my_list.append(i)

save_to_json_file(my_list, "add_item.json")
