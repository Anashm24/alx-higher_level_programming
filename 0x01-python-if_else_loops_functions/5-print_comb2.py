#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i + 1, 10):
        if i == 8 and n == 9:
            print(f"{i}{n}")
        else:
            print(f"{i}{n}", end=", ")
    