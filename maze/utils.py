import pygame

from .colors import Colors
from .spot import Spot


def make_grid(gap, width):
    rows = width // gap

    grid = [[Spot(i, j, gap, rows) for j in range(rows)] for i in range(rows)]
    return grid


def draw_grid(window, gap, width):
    for i in range(0, width, gap):
        pygame.draw.line(window, Colors.BLACK, (0, i), (width, i))
        pygame.draw.line(window, Colors.BLACK, (i, 0), (i, width))


def draw(window, grid, gap, width):
    for row in grid:
        for spot in row:
            spot.draw(window)

    draw_grid(window, gap, width)
    pygame.display.update()


def remove_wall(a, b, grid):
    x = (a.row + b.row) // 2
    y = (a.col + b.col) // 2

    grid[x][y].reset()
    return grid
