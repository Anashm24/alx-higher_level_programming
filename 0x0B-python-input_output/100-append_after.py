#!/usr/bin/python3
"""defines a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string"""
    # Read the file
    with open(filename, "r") as file:
        lines = file.readlines()

    # Modify the lines
    for i in range(len(lines)):
        if search_string in lines[i]:
            lines[i] = lines[i] + new_string

    # Write the modified lines back to the file
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
