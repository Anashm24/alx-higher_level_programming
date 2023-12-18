#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        index = 0
        for i, value in enumerate(my_list, start=1):
            if i <= x:
                print(value, end="")
                index = i
        print()
        return index

except ValueError:
    print("error")
