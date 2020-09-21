#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pos = 0
    while (pos < x):
        try:
            print("{}".format(my_list[pos]), end='');
        except IndexError:
            print()
            return pos
        pos += 1
    print()
    return pos
