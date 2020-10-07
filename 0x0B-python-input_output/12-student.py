#!/usr/bin/python3
"""11-student module"""


class Student():
    """
    Student class

    Public attributes:
        first_name
        last_name
        age

    Public methods:
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dic = {}
        for at in attrs:
            if at in self.__dict__:
                new_dic[at] = self.__dict__[at]
        return new_dic
