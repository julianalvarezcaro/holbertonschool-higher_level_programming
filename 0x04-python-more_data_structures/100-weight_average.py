#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_score = 0
        total_w = 0
        for tup in my_list:
            sum_score += tup[0] * tup[1]
            total_w += tup[1]
        return sum_score / total_w
    else:
        return 0
