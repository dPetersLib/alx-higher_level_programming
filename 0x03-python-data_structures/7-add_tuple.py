#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(0, 2):
        if len(tuple_a) > len(tuple_b):
            if i > len(tuple_b) - 1:
                res.append(tuple_a[i] + 0)
            else:
                res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    return tuple(res)
