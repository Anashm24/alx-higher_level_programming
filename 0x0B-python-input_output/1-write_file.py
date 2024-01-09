#!/usr/bin/python3
"""defines a function write_file(filename="", text="")"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Returns: the number of characters written"""
    
    with open(filename, "w", encoding="utf-8") as file:
        wr_file = file.write(text)
    return wr_file
