#!/usr/bin/python3
"""a script that adds all arguments to a Python
list, and then save them to a file
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        python_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        python_list = []

    arguments = sys.argv[1:]

    for arg in arguments:
        python_list.append(arg)
    save_to_json_file(python_list, "add_item.json")
