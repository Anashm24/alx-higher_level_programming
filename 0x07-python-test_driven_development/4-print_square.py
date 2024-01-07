#!/usr/bin/python3
"""defines a function that prints a square with the character #"""


def print_square(size):
    """Prints a square with the character #

    size:  is the size length of the square
    Raises:
        TypeError: if size is not an integer
                   or size is a float and is less than 0
        ValueError: if size is a float and is less than 0
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
