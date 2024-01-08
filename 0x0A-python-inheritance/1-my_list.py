#!/usr/bin/python3
"""defines a  class MyList that inherits from list"""


class MyList(list):
    """ MyList class """

    def __init__(self):
        pass

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
