#!/usr/bin/python3
"""defines a function prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    raises:
        TypeError: if either of first name or last name is a non-string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
