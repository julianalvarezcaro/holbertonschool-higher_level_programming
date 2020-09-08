#!/usr/bin/python3
def no_c(my_string):
    new = ""
    if len(my_string) == 0:
        return new
    for pos in range(len(my_string)):
        if my_string[pos] != 'c' and my_string[pos] != 'C':
            new += my_string[pos]
    return new

