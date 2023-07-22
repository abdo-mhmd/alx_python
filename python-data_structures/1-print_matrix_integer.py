#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        for x in matrix[i]:
            print("{} ".format(x), end="")
        print("")
        i += 1
