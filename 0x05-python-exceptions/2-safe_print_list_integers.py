#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    printed = 0
    while (pos < x):
        try:
            print("{:d}".format(my_list[pos]), end='')
            printed += 1
        except (TypeError, ValueError):
            pass
        pos += 1
    print()
    return printed
