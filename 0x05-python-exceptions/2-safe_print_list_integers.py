#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for i, value in enumerate(my_list, start=1):
        if i <= x:
            try:
                print("{:d}".format(value), end="")
                index = i
            except (TypeError, ValueError):
                continue
    print()
    return index
