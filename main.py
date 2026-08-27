import pygame
from grid import Grid

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = Grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE, CELL_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grid.handle_click(pos, event.button)

    screen.fill((255, 255, 255))
    grid.draw(screen)
    pygame.display.flip()

pygame.quit()