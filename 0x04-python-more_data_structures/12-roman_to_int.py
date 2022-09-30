#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    odd = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    vl = list(map(lambda x: roman_dict[x], list(roman_string)))
    if len(vl) > 1:
        for h in range(len(vl)):
            for i in range(len(vl)):
                if i != len(vl) - 1:
                    if vl[i + 1] > vl[i]:
                        vl[i], vl[i + 1] = vl[i + 1] - vl[i], 0
    return reduce(lambda x, y: x + y, vl)
