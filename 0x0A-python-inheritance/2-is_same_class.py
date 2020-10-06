#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """Returns true if obj is an instance of a_class"""
    return type(obj) is a_class
