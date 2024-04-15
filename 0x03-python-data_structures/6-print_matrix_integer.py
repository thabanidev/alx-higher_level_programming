#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return
    for row in matrix:
        for n in row:
            print("{:d}".format(n), end="")
            if n != row[-1]:
                print(" ", end="")
        print()
