#!/usr/bin/python3
"""3-is_of_class module"""


def is_kind_of_class(obj, a_class):
    """Returns wether the class is an instance of subclass of a_class"""
    return issubclass(type(obj), a_class)
