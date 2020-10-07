#!/usr/bin/python3
"""7-save_to_json_file module"""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object into a text file"""
    with open(filename, mode='w', encoding="utf-8") as file:
        json.dump(my_obj, file)
