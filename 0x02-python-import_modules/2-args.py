#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:
        print("{} argument:".format(len(argv)-1))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} argument.".format(len(argv) - 1))
