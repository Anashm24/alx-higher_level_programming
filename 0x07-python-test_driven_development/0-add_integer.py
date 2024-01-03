#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return int(a) + int(b)
    except TypeError:
        print("a must be an integer")
