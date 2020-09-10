def square_matrix_simple(matrix=[]):
    copy = [row[:] for row in matrix]
    for fil in range(len(copy)):
        for col in range(len(copy[fil])):
            copy[fil][col] = copy[fil][col]**2
    return copy
