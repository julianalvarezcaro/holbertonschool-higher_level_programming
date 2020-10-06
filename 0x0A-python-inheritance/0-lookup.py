#!/usr/bin/python3
"""
0-lookup module

Contains a function ha returns a list of methos and attributes of an object
"""


def lookup(obj):
    """Returns a list of all the methos and attributes of a given object"""
    return dir(obj)
