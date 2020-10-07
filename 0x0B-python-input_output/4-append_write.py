#!/usr/bin/python3
"""4-append_write module"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a file and returns the number of
    characters written
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
