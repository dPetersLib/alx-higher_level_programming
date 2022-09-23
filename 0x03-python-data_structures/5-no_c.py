#!/usr/bin/python3
def no_c(my_string):
    c = ['c', 'C']
    new_string = ''
    for char in my_string:
        if char not in c:
            new_string += char
    return new_string
