#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    string = dir(hidden_4)
    sorted_str = sorted(string)
    for i in sorted_str:
        print("{}".format(i))
