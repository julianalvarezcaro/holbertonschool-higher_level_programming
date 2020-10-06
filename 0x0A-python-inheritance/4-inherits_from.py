#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if an object is and instance of a class that
    inherited from a_class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
