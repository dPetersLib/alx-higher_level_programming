#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(0, 2):
        if i > len(tuple_a) - 1 and i > len(tuple_b) - 1:
            res.append(0)
        elif i > len(tuple_b) - 1:
            res.append(tuple_a[i] + 0)
        elif i > len(tuple_a) - 1:
            res.append(0 + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    return tuple(res)
