import pygame

from .colors import Colors


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows

        self.x = row * width
        self.y = col * width

        self.color = Colors.TURQUOISE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_barrier(self):
        return self.color == Colors.BLACK

    def is_visited(self):
        return self.color == Colors.WHITE

    def reset(self):
        self.color = Colors.WHITE

    def make_barrier(self):
        self.color = Colors.BLACK

    def make_current(self):
        self.color = Colors.ORANGE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def check_neighbors(self, grid):
        self.neighbors = []

        if (
            self.row < self.total_rows - 2
            and not grid[self.row + 2][self.col].is_visited()
        ):
            self.neighbors.append(grid[self.row + 2][self.col])

        if self.row > 1 and not grid[self.row - 2][self.col].is_visited():
            self.neighbors.append(grid[self.row - 2][self.col])

        if (
            self.col < self.total_rows - 2
            and not grid[self.row][self.col + 2].is_visited()
        ):
            self.neighbors.append(grid[self.row][self.col + 2])

        if self.col > 1 and not grid[self.row][self.col - 2].is_visited():
            self.neighbors.append(grid[self.row][self.col - 2])

        return self.neighbors
