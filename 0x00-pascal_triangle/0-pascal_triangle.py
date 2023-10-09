#!/usr/bin/python3
"""Pascal Triangle Script"""


def pascal_triangle(n):
    """Pascal triangle function"""

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
