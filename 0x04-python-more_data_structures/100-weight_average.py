#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_t = 0

    weight_t = 0

    for score, weight in my_list:
        score_t += score * weight

        weight_t += weight
    if weight_t == 0:
        return 0
    return score_t/weight_t
