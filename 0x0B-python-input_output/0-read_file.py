#!/usr/bin/python3
"""defines a function read_file(filename="")"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        read_fl = file.read()
        print(read_fl, end="")
