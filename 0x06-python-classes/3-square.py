#!/usr/bin/python3
"""3-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Class constructor"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size
