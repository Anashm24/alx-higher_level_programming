#!/usr/bin/python3
import json
"""defines a function to_json_string()"""


def to_json_string(my_obj):
    """Return: the JSON representation of an object (string)"""

    json_str = json.dumps(my_obj)
    return json_str
