#!/usr/bin/python3
"""4-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Class constructor"""
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter for the attribute 'size'"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for the attribute 'size'"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
