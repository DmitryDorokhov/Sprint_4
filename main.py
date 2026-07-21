import pygame
from random import randint


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN_CENTER_X, SCREEN_CENTER_Y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
FPS = 5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    circle_x, circle_y = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), 40)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()