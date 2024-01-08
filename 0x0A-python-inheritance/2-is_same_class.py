#!/usr/bin/python3
"""defines a function is_same_class(obj, a_class)"""


def is_same_class(obj, a_class):
    """returns: True: if the object is an instance of the specified class
              : False: if not"""

    return isinstance(obj, a_class)
