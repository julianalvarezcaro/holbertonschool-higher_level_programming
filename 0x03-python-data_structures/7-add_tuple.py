#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_ca = (0, 0)
    elif len(tuple_a) == 1:
        tuple_ca == (tuple_a[0], 0)
    else:
        tuple_ca = tuple_a
    if len(tuple_b) == 0:
        tuple_cb = (0, 0)
    elif len(tuple_b) == 1:
        tuple_cb = (tuple_b[0], 0)
    else:
        tuple_cb = tuple_b
    tuple_res = (tuple_ca[0] + tuple_cb[0], tuple_ca[1] + tuple_cb[1])
    return tuple_res
