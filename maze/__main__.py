import pygame

from .generation import make_maze
from .utils import draw

SIDE = 700  # The side of the GUI, Keeping it to be a square.
GAP = 12  # The distance between 2 rows.
WINDOW = pygame.display.set_mode((SIDE, SIDE))

pygame.display.set_caption("Maze generation visualization")

if __name__ == '__main__':
    grid = make_maze(WINDOW, SIDE, GAP)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(WINDOW, grid, GAP, SIDE)
