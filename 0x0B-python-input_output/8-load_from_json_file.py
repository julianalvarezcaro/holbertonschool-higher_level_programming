#!/usr/bin/python3
"""8-load_from_json_file module"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
