#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        big = my_list[0]
        for pos in range(1, len(my_list)):
            if my_list[pos] > big:
                big = my_list[pos]
        return big
    else:
        return None
