#!/usr/bin/python3
"""
2-matrix_divided module

Has a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    # First we validate the data received
    if not matrix:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for row in matrix:
        if type(row) is not list or not row:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        else:
            for x in row:
                if type(x) is not int and type(x) is not float:
                    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    length = len(matrix[0])
    if any(len(row) is not length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    # Now copy the array and continue the procedure
    copy_matrix = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for x in range(length):
            copy_matrix[row][x] = round(matrix[row][x]/div, 2)
    return copy_matrix
