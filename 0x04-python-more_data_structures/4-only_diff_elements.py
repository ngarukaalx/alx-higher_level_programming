#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first = set(set_1)
    second = set(set_2)

    return first ^ second
