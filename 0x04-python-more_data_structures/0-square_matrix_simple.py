#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_new = [[a ** 2 for a in row]for row in matrix]
    return matrix_new
