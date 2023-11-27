#!/usr/bin/python3
"""rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """function to rotate 2D matrix 90 degrees clockwise"""
    mx = len(matrix)

    for i in range(mx):
        for j in range(i, mx):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
