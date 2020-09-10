#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list[:]
    for pos in range(len(my_list)):
        if my_list[pos] == search:
            copy[pos] = replace
    return copy
