#!/usr/bin/python3
"""using map function to find the square val of all ints in this matrix"""


def square_matrix_map(matrix=[]):
    squared_matrix = list(map(lambda row: [val ** 2 if isinstance(val, int) \
            else val for val in row], matrix))
    return squared_matrix
