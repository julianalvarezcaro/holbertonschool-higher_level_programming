#!/usr/bin/python3
"""Peak module
"""


def find_peak(list_of_integers):
    """Finds a peak of a list
    """
    if not list_of_integers:
        return None
    # I'll check first and last element separately
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    first = list_of_integers[0]
    last = list_of_integers[-1]
    if first > list_of_integers[1]:
        return abs(first)
    if last > list_of_integers[-2]:
        return abs(last)

    # Now the rest of the elements
    npos = 2
    for n in list_of_integers[1:-1]:
        if max(n, first, list_of_integers[npos]) == n:
            return abs(n)
        npos = npos + 1
    return None
