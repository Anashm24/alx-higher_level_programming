#!/usr/bin/python3
"""defines a function class_to_json()"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""

    to_json = obj.__dict__
    return to_json