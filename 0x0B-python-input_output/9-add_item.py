#!/usr/bin/python3
"""
9-add_item module
Saves the list contaning the args into a file
"""

import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

prev_content = []
if os.path.exists("./add_item.json"):
    prev_content = load_from_json_file(filename)

new_cont = prev_content + args
save_to_json_file(new_cont, filename)
