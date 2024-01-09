#!/usr/bin/python3
"""defines a function to_json_string()"""
import json


def to_json_string(my_obj):
    """Return: the JSON representation of an object (string)"""

    json_str = json.dumps(my_obj)
    return json_str
