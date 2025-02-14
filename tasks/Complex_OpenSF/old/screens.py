import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Fonts (regular and bold)
font_regular = pygame.font.SysFont('Helvetica', 36)
font_bold = pygame.font.SysFont('Helvetica', 48, bold=True)  # Larger for the title
small_font_regular = pygame.font.SysFont('Helvetica', 24)
small_font_bold = pygame.font.SysFont('Helvetica', 24, bold=True)

# Frame rate
clock = pygame.time.Clock()

# Set the screen dynamically for full-screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# Translations for English and French
translations = {
    "eng": {
        "title": "Open Space Fortress",
        "start_prompt": 'Press "spacebar" to begin the task',
        "end_prompt": 'Press "spacebar" to continue',
        "game_stats": "Game Stats",
        "done_prompt": "You're done! Press 'spacebar' to exit",
        "points": "Total score",
        "flight": "Flight",
        "flight_deaths": "deaths",
        "fortress": "Fortresses",
        "fortress_destroyed": "destroyed fortresses",
        "mine": "Mines",
        "mine_destroyed": "destroyed mines",
        "bonus": "Bonuses",
        "bonus_captured": "captured bonuses",
        "of": "of",
        "total": "Total"
    },
    "fr": {
        "title": "Open Space Fortress",
        "start_prompt": 'Appuyez sur "espace" pour commencer',
        "end_prompt": 'Appuyez sur "espace" pour continuer',
        "game_stats": "Statistiques de la partie",
        "done_prompt": 'Vous avez terminé ! Appuyez sur "espace" pour quitter',
        "points": "Score total",
        "flight": "Vol",
        "flight_deaths": "morts",
        "fortress": "Forteresse",
        "fortress_destroyed": "forteresses détruites",
        "mine": "Mines",
        "mine_destroyed": "mines détruites",
        "bonus": "Bonus",
        "bonus_captured": "bonus capturés",
        "of": "sur",
        "total": " "
    }
}

# Function to display text in the center of the screen
def display_centered_text(text, y_offset=0, font_obj=font_regular, color=YELLOW):
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Function to display text at the bottom
def display_bottom_text(text, y_offset=0, font_obj=small_font_regular):
    text_surface = font_obj.render(text, True, YELLOW)
    text_rect = text_surface.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - y_offset))
    screen.blit(text_surface, text_rect)

# Function to load and display the image at the center
def display_centered_image(image_path, y_offset=0):
    try:
        image = pygame.image.load(image_path)
        # Scale the image (twice the original size)
        scaled_image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
        image_rect = scaled_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        screen.blit(scaled_image, image_rect)
    except pygame.error as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit()

# Function to handle the start screen
def start_screen(language, image_filename):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Move to end page when spacebar is pressed
                    running = False
        
        # Fill the screen with black
        screen.fill(BLACK)

        # Display the title text "Open Space Fortress" (bolded)
        display_centered_text(translations[language]["title"], y_offset=-300, font_obj=font_bold)

        # Display the center image (openSF.png)
        display_centered_image(os.path.join(os.path.dirname(__file__), image_filename), y_offset=0)

        # Display the copyright text at the bottom
        display_bottom_text("Copyright (C) 2024 - Neuroergonomics Center, ISAE-SUPAERO, Toulouse, France - Distributed under the MIT License", y_offset=50)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

# Function to display game stats in the end screen
def draw_stats_table(language, scores):
    
    row_height = 50
    
    # Define column widths
    col_widths = [200, 300, 100]  # First, second, and third column widths
    total_table_width = sum(col_widths)
    
    # Calculate the x_start to center the table horizontally
    x_start = (SCREEN_WIDTH - total_table_width) // 2

    # Calculate the y_start to center the table vertically
    y_start = (SCREEN_HEIGHT // 2) - (row_height * 2)

    # Table content using translations and the scores dictionary
    table_data = [
        [f"{translations[language]['flight']}", f"{scores['numberofdeath']} {translations[language]['flight_deaths']}", f"{scores['flight_score']}"],
        [f"{translations[language]['fortress']}", f"{scores['numberofdestroyedfortress']} {translations[language]['fortress_destroyed']}", f"{scores['fortress_score']}"],
        [f"{translations[language]['mine']}", f"{scores['numberofdestroyedmines']} {translations[language]['of']} {scores['numberofmines']} {translations[language]['mine_destroyed']}", f"{scores['mine_score']}"],
        [f"{translations[language]['bonus']}", f"{scores['numberofdestroyedbonuses']} {translations[language]['of']} {scores['numberofbonuses']} {translations[language]['bonus_captured']}", f"{scores['bonus_score']}"],
        [translations[language]["points"], translations[language]["total"], f"{scores['total_score']}"]
    ]

    # Draw the title "Game Stats"
    display_centered_text(translations[language]["game_stats"], y_offset=-250, font_obj=font_bold, color=YELLOW)

    # Draw each row of the table
    for row_index, row_data in enumerate(table_data):
        for col_index, cell_data in enumerate(row_data):
            # Handle alignment: left for first and second columns, right for third column
            if col_index == 2:  # Right-align for the third column, white color for third column
                text_surface = small_font_bold.render(cell_data, True, WHITE)
                text_rect = text_surface.get_rect(right=(x_start + sum(col_widths[:3])), y=y_start + row_index * row_height)
            else:  # Left-align for the first and second columns
                text_surface = small_font_bold.render(cell_data, True, YELLOW)
                text_rect = text_surface.get_rect(topleft=(x_start + sum(col_widths[:col_index]), y_start + row_index * row_height))

            screen.blit(text_surface, text_rect)


# Function to handle the end screen with stats
def end_screen(language, scores):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw the stats table
        draw_stats_table(language, scores)

        # Display the exit instruction at the bottom in green
        display_centered_text(translations[language]["done_prompt"], y_offset=250, font_obj=small_font_regular, color=GREEN)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Exit the game on spacebar press
    pygame.quit()
    sys.exit()
