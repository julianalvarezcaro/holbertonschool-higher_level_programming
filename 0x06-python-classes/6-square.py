#!/usr/bin/python3
"""6-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Class constructor"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """Prints a square of __size size with caracter #"""
        if self.__size == 0:
            print()
        for fil in range(self.__size):
            for col in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(type(val) is not int for val in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(val < 0 for val in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
