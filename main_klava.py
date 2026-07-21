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

    def move(self):
        pass

    def check_border(self):
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

    def move(self):
        if self.direction == -1 or self.direction == 1:
            self.x += self.speed * self.direction
        if self.direction == -2 or self.direction == 2:
            self.y += self.speed * self.direction

    def check_border(self):
        if self.x + self.radius >= SCREEN_WIDTH:
            self.direction = -1
        if self.x - self.radius <= 0:
            self.direction = 1
        if self.y + self.radius >= SCREEN_HEIGHT:
            self.direction = -2
        if self.y - self.radius <= 0:
            self.direction = 2


def handle_keys(object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                object.direction = -1
            if event.key == pygame.K_RIGHT:
                object.direction = 1
            if event.key == pygame.K_DOWN:
                object.direction = 2
            if event.key == pygame.K_UP:
                object.direction = -2              


circle = Circle(screen, (255, 0, 0), SCREEN_CENTER_X, SCREEN_CENTER_Y, 40, 10)

running = True
while running:
    handle_keys(circle)
    screen.fill((0, 0, 0))
    circle.draw()
    circle.move()
    circle.check_border()
    pygame.display.update()
    clock.tick(FPS)