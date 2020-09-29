#!/usr/bin/python3
"""
Empty rectangle Class
"""


class Rectangle:
    """
    Class for rectangles
    """

    def __init__(self, width=0, height=0):
        """Initialized a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for __height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
