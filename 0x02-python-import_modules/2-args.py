#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print("{} argument:".format(len(sys.argv)-1))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} argument.".format(len(sys.argv) - 1))
