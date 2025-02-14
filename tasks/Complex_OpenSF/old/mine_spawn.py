import pygame
import random
import os
import math

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_WIDTH = SCREEN_WIDTH // 2
SQUARE_HEIGHT = SCREEN_HEIGHT // 2
MIN_DISTANCE = SQUARE_HEIGHT  # Minimum distance (equal to the height of the game area)

# Load images
ship_image = pygame.image.load(os.path.join(os.getcwd(), 'ship.png'))
mine_image = pygame.image.load(os.path.join(os.getcwd(), 'mine.png'))

# Rescale images
ship_image = pygame.transform.scale(ship_image, (30, 30))
mine_image = pygame.transform.scale(mine_image, (30, 30))

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mine Spawning Simulation")

# Define colors
BLACK = (0, 0, 0)

# Function to generate random ship position in one square
def get_random_ship_position(square):
    if square == 1:  # Upper left
        return random.randint(0, SQUARE_WIDTH - 30), random.randint(0, SQUARE_HEIGHT - 30)
    elif square == 2:  # Upper right
        return random.randint(SQUARE_WIDTH, SCREEN_WIDTH - 30), random.randint(0, SQUARE_HEIGHT - 30)
    elif square == 3:  # Lower left
        return random.randint(0, SQUARE_WIDTH - 30), random.randint(SQUARE_HEIGHT, SCREEN_HEIGHT - 30)
    else:  # Lower right
        return random.randint(SQUARE_WIDTH, SCREEN_WIDTH - 30), random.randint(SQUARE_HEIGHT, SCREEN_HEIGHT - 30)

# Function to calculate distance between two points (Pythagorean theorem)
def calculate_distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

# Adjust the mine's position if it's too close to the ship
def adjust_mine_position(ship_pos, mine_pos):
    distance = calculate_distance(ship_pos, mine_pos)
    
    if distance < MIN_DISTANCE:
        # Find a point along the line from the ship to the mine that meets the minimum distance
        dx = mine_pos[0] - ship_pos[0]
        dy = mine_pos[1] - ship_pos[1]
        scale = MIN_DISTANCE / distance
        mine_pos = (int(ship_pos[0] + dx * scale), int(ship_pos[1] + dy * scale))
    
    return mine_pos

# Function to spawn the mine based on selected spawn type (opposite, vertical, horizontal)
def get_mine_position(ship_square, spawn_type, ship_pos):
    if spawn_type == "opposite":
        mine_pos = get_opposite_square_position(ship_square)
    elif spawn_type == "vertical":
        mine_pos = get_vertical_square_position(ship_square)
    elif spawn_type == "horizontal":
        mine_pos = get_horizontal_square_position(ship_square)
    
    # Adjust the position if too close to the ship
    mine_pos = adjust_mine_position(ship_pos, mine_pos)
    
    return mine_pos

# Function to determine opposite square's position
def get_opposite_square_position(ship_square):
    if ship_square == 1:
        return get_random_ship_position(4)  # Lower right
    elif ship_square == 2:
        return get_random_ship_position(3)  # Lower left
    elif ship_square == 3:
        return get_random_ship_position(2)  # Upper right
    else:
        return get_random_ship_position(1)  # Upper left

# Function to determine vertical square's position
def get_vertical_square_position(ship_square):
    if ship_square == 1:
        return get_random_ship_position(3)  # Lower left
    elif ship_square == 2:
        return get_random_ship_position(4)  # Lower right
    elif ship_square == 3:
        return get_random_ship_position(1)  # Upper left
    else:
        return get_random_ship_position(2)  # Upper right

# Function to determine horizontal square's position
def get_horizontal_square_position(ship_square):
    if ship_square == 1:
        return get_random_ship_position(2)  # Upper right
    elif ship_square == 2:
        return get_random_ship_position(1)  # Upper left
    elif ship_square == 3:
        return get_random_ship_position(4)  # Lower right
    else:
        return get_random_ship_position(3)  # Lower left

# Randomly generate the ship position in one of the four squares
ship_square = random.randint(1, 4)
ship_pos = get_random_ship_position(ship_square)

# Select mine spawn type: "opposite", "vertical", or "horizontal"
mine_spawn_type = "opposite"  # You can change this value to "vertical" or "horizontal"

# Generate mine position based on the selected spawn type and adjust its position if too close to the ship
mine_pos = get_mine_position(ship_square, mine_spawn_type, ship_pos)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Display the ship and mine
    screen.blit(ship_image, ship_pos)
    screen.blit(mine_image, mine_pos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
