#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_into_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i > 0 and roman_into_dict[i] > roman_into_dict[i - 1]:
            result += roman_into_dict[roman_string[i]] - 2 * roman_into_dict[roman_string[i - 1]]
        else:
            result += roman_into_dict[roman_string[i]]
    return result
