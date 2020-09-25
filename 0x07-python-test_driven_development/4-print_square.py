#!/usr/bin/python3
"""
The 4-print-square module

Has a function that prints a square
"""


def print_square(size):
    """
    Prints a square of 'size' size with the caracter '#'
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for row in range(size):
        for col in range(size):
            print("#", end='')
        print()
