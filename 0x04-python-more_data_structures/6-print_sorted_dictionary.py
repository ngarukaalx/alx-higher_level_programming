#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor = sorted(a_dictionary.keys())
    for k in sor:
        v = a_dictionary[k]
        print("{}: {}".format(k, v))
