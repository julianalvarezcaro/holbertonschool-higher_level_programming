#!/usr/bin/python3
"""1-number_of_lines module"""


def number_of_lines(filename=""):
    """Returns the number of lines in a file"""
    lines = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            lines += 1
    return lines
