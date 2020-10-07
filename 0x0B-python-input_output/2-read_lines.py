#!/usr/bin/python3
"""2-read_lines module"""


def read_lines(filename="", nb_lines=0):
    """Read nb_lines lines of a file and prints them"""
    curr_line = 0
    with open(filename, encoding="utf-8") as file:
        while (nb_lines <= 0 or curr_line < nb_lines):
            line = file.readline()
            if not line:
                break
            print(line, end="")
            curr_line += 1
