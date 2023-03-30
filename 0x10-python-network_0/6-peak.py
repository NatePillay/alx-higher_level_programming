#!/usr/bin/python3
def find_peak(list_of_integers):
    max  = list_of_integers[0]
    for i in list_of_integers:
        if list_of_integers[1] > max:
            max = list_of_integers[1]
    return max
