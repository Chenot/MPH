import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Fonts
font_label = pygame.font.SysFont('Helvetica', 28, bold=True)  # White, uppercase text for labels
font_value = pygame.font.SysFont('Helvetica', 26, bold=True)  # Yellow text for variables

# Frame rate
clock = pygame.time.Clock()

# Set up the screen for full-screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# Example variables to represent dynamic game values (can be updated in the game loop)
vlnr = 0
iff = "N"
points = 1235
time_value = 146.4
shots = 50

# Function to display text on the screen
def display_text(text, font, color, x, y, align="center"):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    # Adjust text alignment
    if align == "center":
        text_rect.center = (x, y)
    elif align == "left":
        text_rect.topleft = (x, y)
    elif align == "right":
        text_rect.topright = (x, y)
    
    screen.blit(text_surface, text_rect)

# Function to render the upper panel interface
def render_interface(vlnr, iff, points, time_value, shots):
    screen.fill(BLACK)  # Fill the background with black

    # Define the game rectangle ratio 14:12
    game_rect_ratio_width = 14
    game_rect_ratio_height = 12

    # Calculate the game rectangle size based on the available screen size and the aspect ratio
    available_height = SCREEN_HEIGHT - 120  # Account for the upper panel and some margin
    game_rect_height = min(available_height, (SCREEN_WIDTH * game_rect_ratio_height) // game_rect_ratio_width)
    game_rect_width = (game_rect_height * game_rect_ratio_width) // game_rect_ratio_height

    # Calculate the x and y position for the game rectangle to center it
    square_x = (SCREEN_WIDTH - game_rect_width) // 2
    square_y = 110

    # Draw the game boundaries rectangle (14:12 ratio)
    pygame.draw.rect(screen, WHITE, pygame.Rect(square_x, square_y, game_rect_width, game_rect_height), 2)

    # Adjust the width of the upper panel to match the game rectangle width
    upper_panel_height = 100
    pygame.draw.rect(screen, WHITE, pygame.Rect(square_x, 0, game_rect_width, upper_panel_height), 2)

    # Text positions in the upper panel
    middle_x = square_x + game_rect_width // 2
    middle_spacing = 400  # Increased spacing between VLNR, IFF, and SHOTS

    # Left side (Points)
    display_text("POINTS", font_label, WHITE, 100, upper_panel_height // 3, align="center")
    display_text(str(points), font_value, YELLOW, 100, 2 * upper_panel_height // 3, align="center")

    # Right side (Time)
    display_text("TIME", font_label, WHITE, SCREEN_WIDTH - 100, upper_panel_height // 3, align="center")
    display_text(f"{time_value:.1f}", font_value, YELLOW, SCREEN_WIDTH - 100, 2 * upper_panel_height // 3, align="center")

    # Inside the upper panel for VLNR, IFF, SHOTS (matching the game rectangle width)
    # Middle left (VLNR)
    display_text("VLNR", font_label, WHITE, middle_x - middle_spacing, upper_panel_height // 3, align="center")
    display_text(str(vlnr), font_value, YELLOW, middle_x - middle_spacing, 2 * upper_panel_height // 3, align="center")

    # Middle center (IFF)
    display_text("IFF", font_label, WHITE, middle_x, upper_panel_height // 3, align="center")
    display_text(str(iff), font_value, YELLOW, middle_x, 2 * upper_panel_height // 3, align="center")

    # Middle right (SHOTS)
    display_text("SHOTS", font_label, WHITE, middle_x + middle_spacing, upper_panel_height // 3, align="center")
    display_text(str(shots), font_value, YELLOW, middle_x + middle_spacing, 2 * upper_panel_height // 3, align="center")

    pygame.display.update()  # Update the display

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the interface
    render_interface(vlnr, iff, points, time_value, shots)
    
    # Update values for demonstration purposes (replace with actual game logic)
    time_value -= 0.1  # Simulate the passing of time
    
    clock.tick(60)  # Maintain 60 FPS

# Clean up
pygame.quit()
sys.exit()
