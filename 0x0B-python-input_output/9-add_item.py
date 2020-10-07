#!/usr/bin/python3
"""9-add_item module"""

import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"


def main(args):
    """Saves the list contaning the args into a file"""
    prev_content = load_from_json_file(filename)

    new_cont = prev_content + args
    save_to_json_file(new_cont, filename)

if __name__ == "__main__":
    main(sys.argv[1:])
