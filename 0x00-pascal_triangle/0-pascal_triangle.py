#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers to give the Pascal’s triangle"""

    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        r = [1]
        for j in range(1, i):
            r.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        if i > 0:
            r.append(1)
        pascal.append(r)
    return pascal
