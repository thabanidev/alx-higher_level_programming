#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    for row in matrix:
        for n in row:
            print("{:d}".format(n), end="")
        print()
