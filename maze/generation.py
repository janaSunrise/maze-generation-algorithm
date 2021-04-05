import random

import pygame

from .utils import draw, make_grid, remove_wall


def make_maze(window, width, gap):
    rows = width // gap
    grid = make_grid(gap, width)

    for i in range(0, rows, 2):
        for j in range(rows):
            grid[i][j].make_barrier()
            grid[j][i].make_barrier()

    current = grid[1][1]
    stack = [current]

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        neighbors = current.check_neighbors(grid)

        if neighbors:
            choosen_one = random.choice(neighbors)
            choosen_one.reset()

            grid = remove_wall(current, choosen_one, grid)
            current.reset()

            current = choosen_one
            if choosen_one not in stack:
                stack.append(choosen_one)
        else:
            current.reset()
            current = stack.pop(-1)

        current.make_current()
        draw(window, grid, gap, width)

    current.reset()
    return grid
