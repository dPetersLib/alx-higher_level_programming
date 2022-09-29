#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = ""
        max_score = 0
        for key, value in a_dictionary.items():
            if value > max_score:
                max = key
                max_score = value
        return max
    return None
