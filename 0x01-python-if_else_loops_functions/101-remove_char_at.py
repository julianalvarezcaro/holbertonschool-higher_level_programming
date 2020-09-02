#!/usr/bin/python3
def remove_char_at(str, n):
    posn = 0
    new = ''
    for pos in range(0, len(str)):
        if pos == n:
            continue
        new = new + str[pos]
    return new
