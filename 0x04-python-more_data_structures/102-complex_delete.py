#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    nd = {k: v for k, v in a_dictionary.items() if v == value}
    for i in nd:
        del a_dictionary[i]
    return a_dictionary
