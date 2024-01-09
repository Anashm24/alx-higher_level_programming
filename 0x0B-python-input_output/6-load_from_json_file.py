#!/usr/bin/python3
"""defines a function load_from_json_file()"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename, "r") as file:
        from_json = json.load(file)
        print(from_json, end="")
