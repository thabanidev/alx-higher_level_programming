#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return []
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
