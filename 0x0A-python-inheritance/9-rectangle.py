#!/usr/bin/python3
"""8-rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherites from BaseGeometry"""

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
