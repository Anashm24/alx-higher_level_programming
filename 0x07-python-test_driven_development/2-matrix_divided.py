#!/usr/bin/python3
"""define a matrix division function"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
             : Each row of the matrix must have the same size
             : div must be a number
    ZeroDivisionError : division by zero
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all((isinstance(row, list) for row in matrix)) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            new_matrix[row][element] = round(matrix[row][element] / div, 2)
    return new_matrix
