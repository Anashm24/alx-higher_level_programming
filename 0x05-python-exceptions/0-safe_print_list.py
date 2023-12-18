#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for i, value in enumerate(my_list, start=1):
        try:
            if i <= x:
                print(value, end="")
                index = i
        except IndexError:
            break
    print()
    return index
