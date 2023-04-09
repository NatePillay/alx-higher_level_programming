#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [val ** 2 if isinstance(val, int) else val for val in row], matrix))
