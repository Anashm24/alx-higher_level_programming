#!/usr/bin/python3
"""defines a function pascal_triangle()"""


def pascal_triangle(n):
    """Return: list of lists of integers representing Pascal's triangle of n"""
    # Return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row in the triangle
    for i in range(1, n):
        # Start and end each row with 1
        row = [1]
        # Each interior value is the sum of two values in the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
