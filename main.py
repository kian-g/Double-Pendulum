import pygame
from math import pi, sin, cos

# Pendulum arm lengths
radius1 = 160
radius2 = 100

# Adjust starting angles
angle1 = pi - 0.1
angle2 = 0

# Mass of balls 1 and 2
mass1 = 16
mass2 = 5

angle1_velocity = 0
angle2_velocity = 0

angle1_acceleration = 0
angle2_acceleration = 0

# Gravity
g = 9.8

# How much velocity to keep each time step
dampening = 0.999

black = (0, 0, 0)

stroke_weight = 2

# Canvas size
screen_width, screen_height = (600, 600)

pygame.init()
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("double pendulum")

# Center offset coordinates
cx, cy = (screen_width // 2), (screen_height // 2) - 100

# Array to keep (x,y) of previous points to draw path
previous_x, previous_y = [], []


def draw(dt):
    global angle1
    global angle2
    global angle1_velocity
    global angle2_velocity

    x1 = radius1 * sin(angle1)
    y1 = radius1 * cos(angle1)

    x2 = x1 + radius2 * sin(angle2)
    y2 = y1 + radius2 * cos(angle2)

    angle1_acceleration = (
        -g * (2 * mass1 + mass2) * sin(angle1)
        - mass2 * g * sin(angle1 - 2 * angle2)
        - 2
        * sin(angle1 - angle2)
        * mass2
        * (
            angle2_velocity**2 * radius2
            + angle1_velocity**2 * radius1 * cos(angle1 - angle2)
        )
    ) / (radius1 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2)))

    angle2_acceleration = (
        (2 * sin(angle1 - angle2))
        * (
            angle1_velocity**2 * radius1 * (mass1 + mass2)
            + g * (mass1 + mass2) * cos(angle1)
            + angle2_velocity**2 * radius2 * mass2 * cos(angle1 - angle2)
        )
    ) / (radius2 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2)))

    # Set pygame bg white
    screen.fill("white")

    # First pendulum line
    pygame.draw.line(screen, black, (cx, cy), (cx + x1, cy + y1), width=stroke_weight)
    pygame.draw.circle(screen, black, (cx + x1, cy + y1), radius=mass1)

    # Second pendulum line
    pygame.draw.line(
        screen, black, (cx + x1, cy + y1), (cx + x2, cy + y2), width=stroke_weight
    )
    pygame.draw.circle(screen, black, (cx + x2, cy + y2), radius=mass2)

    # Draw contiguous line segments for path
    previous_x.append(x2)
    previous_y.append(y2)

    for i in range(len(previous_x)):
        if i > 1:
            pygame.draw.line(
                screen,
                black,
                (cx + previous_x[i - 2], cy + previous_y[i - 2]),
                (cx + previous_x[i - 1], cy + previous_y[i - 1]),
                width=1,
            )

    # Cap max line segments at 150
    if len(previous_x) > 150:
        previous_x.pop(0)
        previous_y.pop(0)

    angle1_velocity += angle1_acceleration * dt
    angle2_velocity += angle2_acceleration * dt

    angle1 += angle1_velocity * dt
    angle2 += angle2_velocity * dt

    angle1_velocity *= dampening
    angle2_velocity *= dampening

    # Update screen to display changes
    pygame.display.flip()


clock = pygame.time.Clock()

running = True
while running:
    # Consistent time scale dt
    dt = clock.tick(60) / 1000.0 * 15

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw(dt)

pygame.quit()
