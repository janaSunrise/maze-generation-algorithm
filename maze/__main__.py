import pygame

from .generation import make_maze
from .utils import draw


class Game:
    SIDE = 700  # The side of the GUI, Keeping it to be a square.
    GAP = 12  # The distance between 2 rows.

    def __init__(self):
        self.window = pygame.display.set_mode((self.SIDE, self.SIDE))
        pygame.display.set_caption("Maze generation visualization")

    def make_and_draw_maze(self):
        grid = make_maze(self.window, self.SIDE, self.GAP)
        draw(self.window, grid, self.GAP, self.SIDE)

    def update_screen(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.make_and_draw_maze()


if __name__ == '__main__':
    game = Game()
    game.update_screen()
