#!/usr/bin/python3
"""defines a class LockedClass"""


class LockedClass:
    """a class with no class or object attribute
    """
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
