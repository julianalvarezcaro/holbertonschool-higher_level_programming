#!/usr/bin/python3
"""3-write_file module"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of lines written"""
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(text)
        return file.tell()
