#!/usr/bin/python3
"""defines a function is_kind_of_class(obj, a_class):"""


def is_kind_of_class(obj, a_class):
    """Return
        True: if the object is an instance of
        False: if not"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
