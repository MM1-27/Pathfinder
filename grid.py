import pygame
from algorithms.BFS import bfs
from algorithms.DFS import dfs
from algorithms.dijkstra import dijkstra

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.size = cell_size

        # 0 = empty, 1 = wall, 2 = start, 3 = end
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]

        self.start = None
        self.end = None

    def get_color(self, value):
        if value == 0:
            return (255, 255, 255)  # empty
        if value == 1:
            return (0, 0, 0)        # wall
        if value == 2:
            return (0, 255, 0)      # start
        if value == 3:
            return (255, 0, 0)      # end
        if value == 4:
            return (0, 0, 255)      # visited (blue)
        if value == 5:
            return (0, 255, 255)    # final path (cyan)

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                color = self.get_color(self.cells[r][c])
                pygame.draw.rect(
                    screen,
                    color,
                    (c*self.size, r*self.size, self.size, self.size)
                )
                pygame.draw.rect(
                    screen,
                    (180, 180, 180),
                    (c*self.size, r*self.size, self.size, self.size),
                    1
                )

    def handle_click(self, pos, button):
        c = pos[0] // self.size
        r = pos[1] // self.size

        if button == 1:  # left click = wall
            self.cells[r][c] = 1

        elif button == 3:  # right click = start
            if self.start:
                old_r, old_c = self.start
                self.cells[old_r][old_c] = 0
            self.start = (r, c)
            self.cells[r][c] = 2

        elif button == 2:  # middle click = end
            if self.end:
                old_r, old_c = self.end
                self.cells[old_r][old_c] = 0
            self.end = (r, c)
            self.cells[r][c] = 3



    ##################

    def run_bfs(self):
        bfs(self)


    def run_dfs(self):
        dfs(self)


    def run_dijkstra(self):
        dijkstra(self)