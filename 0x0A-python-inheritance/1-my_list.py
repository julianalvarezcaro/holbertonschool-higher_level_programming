#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """
    MyList class which inherits from list
    """

    def print_sorted(self):
        """Prints a list in ascending order without altering it"""
       print(sorted(self))
