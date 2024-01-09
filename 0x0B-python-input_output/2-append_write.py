#!/usr/bin/python3
"""defines a function append_write()"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Return: the number of characters added:"""

    with open(filename, "a", encoding="utf-8") as file:
        append_file = file.write(text)
    return append_file
