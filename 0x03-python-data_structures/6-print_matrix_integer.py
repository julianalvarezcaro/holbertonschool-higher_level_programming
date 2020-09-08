#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lst in range(len(matrix)):
            for pos in range(len(matrix[lst])):
                print("{:d}".format(matrix[lst][pos]), end='')
                if pos != len(matrix[lst]) - 1:
                    print(" ", end='')
            print()
    else:
        print()
