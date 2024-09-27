import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(white)

    # Draw a blue circle in the center
    circle_radius = 50
    circle_center = (screen_width // 2, screen_height // 2)
    pygame.draw.circle(screen, blue, circle_center, circle_radius)

    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()
