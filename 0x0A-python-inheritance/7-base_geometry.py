#!/usr/bin/python3
"""7-base_geometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception when called"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value argument

        name: name of the variable
        value: value that must be validated
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
