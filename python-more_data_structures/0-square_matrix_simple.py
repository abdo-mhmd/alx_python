#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        row_list = map(lambda num: num * num, row)
        new_list.append(list(row_list))
    return (new_list)
