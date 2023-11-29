#!/usr/bin/python3
"""perimeter of island"""


def island_perimeter(grid):
    """function to return the perimeter of island described in grid"""
    if not grid or not grid[0]:
        return 0

    prmt = 0
    rows, clms = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(clms):
            if grid[i][j] == 1:
                prmt += 4

            if i > 0 and grid[i - 1][j] == 1:
                prmt -= 1
            if i < rows - 1 and grid[i + 1][j] == 1:
                prmt -= 1
            if j > 0 and grid[i][j - 1] == 1:
                prmt -= 1
            if j < clms - 1 and grid[i][j + 1] == 1:
                prmt -= 1
    return prmt
