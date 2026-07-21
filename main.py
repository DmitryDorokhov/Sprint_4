import pygame
from random import randint


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN_CENTER_X, SCREEN_CENTER_Y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
FPS = 5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class GameObject:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color

    def draw(self):
        pass

class Circle(GameObject):
    def __init__(self, surface, color, x, y, radius, speed):
        super().__init__(surface, color)
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = 1

    def draw(self):
        pygame.draw.circle(self.surface, 
                            self.color, 
                            (self.x, self.y), 
                            self.radius)


circles = [Circle(screen,
                  (randint(0, 255), randint(0, 255), randint(0, 255)),
                  randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT),
                  randint(5,50),
                  randint(10, 50)) for _ in range(3)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for circle in circles:
        circle.draw()
        if circle.x + circle.radius >= SCREEN_WIDTH:
            circle.direction = -1
            print(circle.x + circle.radius)
        if circle.x - circle.radius <= 0:
            circle.direction = 1
        circle.x += circle.speed * circle.direction
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()