#!/usr/bin/python3
"""defines a function from_json_string()"""
import json


def from_json_string(my_str):
    """Returns: an object (Python data structure)
    represented by a JSON string"""

    json_str = json.loads(my_str)
    return json_str
