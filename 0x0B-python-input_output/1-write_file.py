#!/usr/bin/python3
"""defines a function write_file(filename="", text="")"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        wr_file = file.write(text)
    return wr_file
