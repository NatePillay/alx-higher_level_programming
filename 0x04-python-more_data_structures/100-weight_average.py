#!/usr/bin/python3
""" calculate the weighted average of a tuple of numbers"""

def weight_average(my_list=[]):
    if my_list:
        weight = 0
        denom = 0
        for i in range(len(my_list)):
            weight += my_list[i][0] * my_list[i][1]
            denom += my_list[i][1]
        avg = weight/denom
        return avg
    return 0
