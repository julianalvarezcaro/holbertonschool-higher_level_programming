#!/usr/bin/python3
"""
Rectangle Class module
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

    def area(self):
        return self.height * self.width

    def perimeter(self):
        height = self.height
        width = self.width
        if height == 0 or width == 0:
            return 0
        return (2 * height) + (2 * width)

    def __str__(self):
        height = self.height
        width = self.width
        printing = ""
        if height == 0 or width == 0:
            return printing
        for line in range(height):
            printing += '#' * width
            if line != height - 1:
                printing += '\n'
        return printing

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
