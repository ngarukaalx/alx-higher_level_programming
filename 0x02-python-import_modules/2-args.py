#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengt = len(sys.argv[1:])
    if lengt == 0:
        print("{} arguments.".format(lengt))
    elif lengt == 1:
        print("{} argument:".format(lengt))
        for i, ar in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, ar))
    else:
        print("{} arguments:".format(lengt))
        for index, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(index, arg))
