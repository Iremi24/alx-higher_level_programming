#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
