#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    i = float('-inf')
    bestkey = None

    for k, v in a_dictionary.items():
        if v > i:
            i = v
            bestkey = k

    return bestkey
