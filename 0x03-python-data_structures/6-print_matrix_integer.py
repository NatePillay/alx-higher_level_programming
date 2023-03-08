#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for number in element:
            if number == element[-1]:
                print("{:d}".format(number), end="")
            else:
                print("{:d}".format(number), end=" ")
        print('')
