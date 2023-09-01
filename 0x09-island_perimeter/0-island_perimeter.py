#!/usr/bin/python3
"""Island Perimeter function"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    grid is a list of list of integers:
      0 represents water
      1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and
    height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn' have "lakes"
    (water inside that isn't connected to
    the water surrounding the island).
    """

    rows = len(grid)
    cols = len(grid[0])

    def is_land(row, col):
        """Function for land"""
        return grid[row][col] == 1

    def get_neighbors(row, col):
        """Function for neigbour"""
        return [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if is_land(row, col):
                for neighbor_row, neighbor_col in get_neighbors(row, col):
                    if not is_land(neighbor_row, neighbor_col):
                        perimeter += 1

    return perimeter
