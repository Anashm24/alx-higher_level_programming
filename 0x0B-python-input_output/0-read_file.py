#!/usr/bin/python3
"""defines a function read_file(filename="")"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r") as file:
        read_file = file.read()
        print(read_file)
