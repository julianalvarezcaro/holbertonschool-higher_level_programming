#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """Read a file and prints it to the stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
