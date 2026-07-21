import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN_CENTER_X, SCREEN_CENTER_Y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
FPS = 5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

circle_coordinates = (SCREEN_CENTER_X, SCREEN_CENTER_Y)
circle_radius = 40
circle_color = (255, 0, 0)

triangle_coordinates = [(150, 200), (50, 300), (250, 300)]
triangle_color = (0, 0, 255)

square_coordinates = pygame.Rect(450, 200, 100, 100)
square_color = (0, 255, 90)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, 
                        (SCREEN_CENTER_X, SCREEN_CENTER_Y), 
                        circle_radius)
    pygame.draw.polygon(screen, triangle_color, triangle_coordinates)
    pygame.draw.rect(screen, square_color, square_coordinates)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()