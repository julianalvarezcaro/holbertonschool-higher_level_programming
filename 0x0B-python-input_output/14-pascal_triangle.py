#!/usr/bin/python3
"""14-pascal_triangle module"""


def pascal_triangle(n):
    """Returns a matrix representing a pascal triangle"""
    tri = []
    if n <= 0:
        return tri
    if n >= 1:
        tri.append([1])
    if n >= 2:
        tri.append([1, 1])
    i = 1
    while (i <= n - 2):
        cp_prev = tri[i][:]
        cp_prev.append(1)
        pos = 1
        while(pos <= i):
            cp_prev[pos] = tri[i][pos - 1] + tri[i][pos]
            pos += 1
        tri.append(cp_prev)
        i += 1
    return tri
