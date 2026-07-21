import pygame


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
    def __init__(self, surface, color, x, y, radius):
        super().__init__(surface, color)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)


class Square(GameObject):
    def __init__(self, surface, color, x, y, side):
        super().__init__(surface, color)
        self.x = x
        self.y = y
        self.side = side

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         pygame.Rect(self.x, self.y, self.side, self.side))


class Triangle(GameObject):
    def __init__(self, surface, color, points):
        super().__init__(surface, color)
        self.points = points

    def draw(self):
        pygame.draw.polygon(self.surface, self.color, self.points)


circle = Circle(screen, (255, 0, 0), SCREEN_CENTER_X, SCREEN_CENTER_Y, 40)
square = Square(screen, (0, 255, 0), 450, 200, 100)
triangle = Triangle(screen, (0, 0, 255), [(150, 200), (50, 300), (250, 300)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    circle.draw()
    square.draw()
    triangle.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()