#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    ag = [int(arg) for arg in sys.argv[1:]]
    total = sum(ag)
    print("{}".format(total))
