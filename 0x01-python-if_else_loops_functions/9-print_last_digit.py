#!/usr/bin/python3
def print_last_digit(number):
    lastd = number % 10
    if number < 0 and lastd != 0:
        lastd = (lastd - 10) * -1
    print("{}".format(lastd), end='')
    return lastd
