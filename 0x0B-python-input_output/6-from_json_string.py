#!/usr/bin/python3
"""6-from_json_string module"""

import json


def from_json_string(my_str):
    """Returns an object out of a json represetation"""
    return json.loads(my_str)
