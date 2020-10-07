#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    def __ne__(self, number):
        return super().__eq__(number)

    def __eq__(self, number):
        return super().__ne__(number)
