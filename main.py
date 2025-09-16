import pygame
import pymunk


pygame.init()

screen_height = 840
screen_width = 648

display = pygame.display.set_mode((screen_width, screen_width))
clock = pygame.time.Clock()
window_running = True
target_fps = 60

# create space
space = pymunk.Space()  # holds the logic for our physics 'world' or 'space'
space.gravity = 0, 1000


class Ball:
    def __init__(self, position: tuple, radius: float, density=1, elasticity=1):
        self.body = pymunk.Body()
        self.body.position = position

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density      = density
        self.shape.elasticity   = elasticity

    def add_to_space(self):
        space.add(self.body, self.shape)    


class Wall:
    def __init__(self, start_pos: tuple, end_pos: tuple, radius=5, elasticity=0):
        self.start_pos  = start_pos
        self.end_pos    = end_pos
        self.radius     = radius
        self.elasticity = elasticity

        self.segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.segment_shape = pymunk.Segment(
            self.segment_body,
            (start_pos),
            (end_pos),
            self.radius
        )
        self.segment_shape.elasticity = self.elasticity

    def draw(self):
        pygame.draw.line(
            display,
            (0, 0, 0),
            (self.start_pos),
            (self.end_pos),
            self.radius
        )

    def add_to_space(self):
        space.add(self.segment_body, self.segment_shape)


wall1 = Wall(
    (50, 500),
    (150, 520),
    5,
    0.75
)

wall2 = Wall(
    (397, 464),
    (485, 407),
    5,
    1
)

wall3 = Wall(
    (20, 333),
    (20, 396),
    5,
    1
)

wall4 = Wall(
    (257, 587),
    (348, 577),
    5,
    1
)

wall5 = Wall(
    (517, 632),
    (578, 532),
    5,
    1
)

wall6 = Wall(
    (132, 595),
    (221, 626),
    5,
    1
)

wall7 = Wall(
    (393, 625),
    (494, 636),
    5,
    1
)

wall8 = Wall(
    (608, 533),
    (641, 493),
    5,
    1
)

wall9 = Wall(
    (20, 505),
    (20, 434),
    5,
    1
)

ball1 = Ball(
    (100, 100),
    10,
    1,
    1
)

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9]
for wall in walls:
    wall.add_to_space()

ball1.add_to_space()


# display loop
while window_running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    display.fill((235, 235, 235))

    pygame.draw.circle(display, (255, 0, 0), (ball1.body.position[0], ball1.body.position[1]), 10)
    
    for wall in walls:
        wall.draw()

    pygame.display.update()

    clock.tick(target_fps)
    space.step(1 / target_fps)

pygame.quit()