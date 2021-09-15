#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = 0
    y = 0
    if isinstance(tuple_a, tuple):
        if len(tuple_a) >= 1:
            x += tuple_a[0]
            if len(tuple_a) >= 2:
                y += tuple_a[1]
    if isinstance(tuple_b, tuple):
        if len(tuple_b) >= 1:
            x += tuple_b[0]
            if len(tuple_b) >= 2:
                y += tuple_b[1]
    res = (x, y)
    return res
