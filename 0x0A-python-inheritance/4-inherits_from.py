#!/usr/bin/python3
"""defines a function inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """Returns:
        True: if the object is an instance of a class that inherited
        False: if not
        """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
