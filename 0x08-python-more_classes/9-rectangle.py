#!/usr/bin/python3
"""
Rectangle Class module
"""


class Rectangle:
    """
    Class for rectangles
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialized a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            printing += (str(self.print_symbol) * width)
            if line != height - 1:
                printing += '\n'
        return printing

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area2 > area1:
            return rect_2
        else:
            return

    @classmethod
    def square(cls, size=0):
        new_rec = Rectangle(size, size)
        return new_rec
