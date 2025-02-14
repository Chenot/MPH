import os
import sys
import pygame
import configparser
import subprocess
import shutil
import glob
from datetime import datetime

# Adjust the path to import functions if needed
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

# Function to handle all text translations based on the participant's language
def get_translations(language):
    if language == 'French':
        return {
            'press_space': 'Appuyez sur la barre espace pour continuer',
            'press_space_to_read_again': 'Appuyez sur la barre espace pour relire',
            'title': 'Open MATB',
            'reminder_title': 'Rappel des règles MATB',
            'previous': 'Précédent',
            'next': 'Suivant',
            'session_instructions': "Dans cette session, vous effectuerez 4 parties de MATB, chacune durant 4 minutes.\nPrenez le temps d'ajuster la position du joystick et du clavier si nécessaire.\n\n\nAvant chaque partie, votre indicatif vous sera donné.\nLa MATB pourra également être couplée avec la tâche oddball. Dans ce cas, il vous sera demandé d'appuyer sur 'E' lorsque vous entendrez des sons aigus.\nVous devrez essayer de réaliser les deux tâches simultanément du mieux que vous pouvez, en priorisant la MATB.",
        }
    else:  # Default to English
        return {
            'press_space': 'Press the spacebar to continue',
            'press_space_to_read_again': 'Press the spacebar to read again',
            'title': 'Open MATB',
            'reminder_title': 'Reminder of MATB rules',
            'previous': 'Previous',
            'next': 'Next',
            'session_instructions': "In this session, you will do 4 games of MATB, each one lasting 4 minutes.\nTake the time to adjust the position of the joystick and keyboard if necessary.\n\n\nBefore each game, you will be given your callsign.\nThe MATB can also be coupled with the oddball task. In this case, you will be asked to press 'E' when you hear high-pitched sounds.\nYou should try to complete both tasks simultaneously as best you can, giving priority to the MATB",
        }

# Function to wrap text for pygame rendering
def wrap_text(text, font, max_width):
    lines = []
    if isinstance(text, str):
        text = text.split('\n')
    for paragraph in text:
        words = paragraph.split(' ')
        line = ''
        for word in words:
            test_line = f'{line} {word}'.strip()
            if font.size(test_line)[0] <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        lines.append('')  # Add empty line between paragraphs
    return lines

# Function to display the initial reminder screen
def display_initial_reminder_screen(language):
    pygame.init()
    
    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set background color (grey)
    screen.fill((169, 169, 169))

    # Load fonts, adjust sizes as needed
    font_title = pygame.font.Font(None, int(screen_height * 0.1))  # For the title
    font_instruction = pygame.font.Font(None, int(screen_height * 0.05))  # For the instruction text

    # Get the translations
    translations = get_translations(language)

    # Render the title text (localized)
    text_title = font_title.render(translations['title'], True, (255, 255, 255))
    text_title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 6))  # Adjust position as needed
    screen.blit(text_title, text_title_rect)

    # Render the center text (localized)
    center_text = translations['reminder_title']
    text_center = font_instruction.render(center_text, True, (255, 255, 255))
    text_center_rect = text_center.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_center, text_center_rect)

    # Render the bottom text (localized)
    bottom_text = translations['press_space_to_read_again']
    text_bottom = font_instruction.render(bottom_text, True, (255, 255, 255))
    text_bottom_rect = text_bottom.get_rect(center=(screen_width // 2, int(screen_height * 0.9)))
    screen.blit(text_bottom, text_bottom_rect)

    # Update the display
    pygame.display.flip()

    # Wait for spacebar press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    # Clean up
    pygame.quit()

# Function to display images with navigation buttons
def display_image_gallery(image_paths, language):
    pygame.init()
    
    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Load fonts
    font_title = pygame.font.Font(None, int(screen_height * 0.1))  # For the title
    font_button = pygame.font.Font(None, int(screen_height * 0.05))  # For the buttons

    # Get the translations
    translations = get_translations(language)
    title_text = translations['title']
    previous_text = translations['previous']
    next_text = translations['next']

    # Load images
    images = []
    for path in image_paths:
        try:
            image = pygame.image.load(path)
            images.append(image)
        except pygame.error:
            print(f"Failed to load image from {path}")
            images.append(None)  # Placeholder for failed images

    current_image_index = 0
    total_images = len(images)
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Check if previous button is clicked
                if previous_button_rect.collidepoint(mouse_pos):
                    if current_image_index > 0:
                        current_image_index -= 1
                # Check if next button is clicked
                elif next_button_rect.collidepoint(mouse_pos):
                    if current_image_index < total_images - 1:
                        current_image_index += 1
                    else:
                        # End of images, exit the gallery
                        running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    if current_image_index > 0:
                        current_image_index -= 1
                elif event.key == pygame.K_RIGHT:
                    if current_image_index < total_images - 1:
                        current_image_index += 1
                    else:
                        # End of images, exit the gallery
                        running = False

        # Clear the screen
        screen.fill((169, 169, 169))

        # Render the title text
        text_title = font_title.render(title_text, True, (255, 255, 255))
        text_title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 10))
        screen.blit(text_title, text_title_rect)

        # Display the current image
        image = images[current_image_index]
        if image:
            # Scale image appropriately
            original_width, original_height = image.get_size()
            aspect_ratio = original_width / original_height
            max_width = int(screen_width * 0.7)
            max_height = int(screen_height * 0.7)
            if max_width / aspect_ratio <= max_height:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_width = int(max_height * aspect_ratio)
                new_height = max_height
            # Resize the image
            image_scaled = pygame.transform.scale(image, (new_width, new_height))
            image_rect = image_scaled.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(image_scaled, image_rect)
        else:
            # If image failed to load, display error message
            error_text = font_button.render("Image failed to load.", True, (255, 0, 0))
            error_rect = error_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(error_text, error_rect)

        # Draw 'Previous' button on the left
        previous_button_surface = font_button.render(previous_text, True, (255, 255, 255))
        previous_button_rect = previous_button_surface.get_rect(center=(int(screen_width * 0.1), int(screen_height * 0.9)))
        if current_image_index == 0:
            # Disable the button (greyed out)
            previous_button_surface = font_button.render(previous_text, True, (128, 128, 128))
        screen.blit(previous_button_surface, previous_button_rect)

        # Draw 'Next' button on the right
        next_button_surface = font_button.render(next_text, True, (255, 255, 255))
        next_button_rect = next_button_surface.get_rect(center=(int(screen_width * 0.9), int(screen_height * 0.9)))
        if current_image_index >= total_images - 1:
            # Optionally, change the 'Next' button appearance when on the last image
            next_button_surface = font_button.render(next_text, True, (128, 128, 128))
        screen.blit(next_button_surface, next_button_rect)

        # Update the display
        pygame.display.flip()

    # Clean up
    pygame.quit()


# Function to display the final instruction screen
def display_final_instruction_screen(language):
    pygame.init()
    
    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set background color (grey)
    screen.fill((169, 169, 169))

    # Load fonts
    font_title = pygame.font.Font(None, int(screen_height * 0.1))  # For the title
    font_instruction = pygame.font.Font(None, int(screen_height * 0.05))  # For the instruction text

    # Get the translations
    translations = get_translations(language)

    # Render the title text
    title_text = translations['title']
    text_title = font_title.render(title_text, True, (255, 255, 255))
    text_title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 10))
    screen.blit(text_title, text_title_rect)

    # Wrap and render the instruction text
    instruction_text = translations['session_instructions']
    instruction_lines = wrap_text(instruction_text, font_instruction, screen_width * 0.8)
    instruction_start_y = screen_height // 3  # Adjust as needed

    y_offset = instruction_start_y
    for line in instruction_lines:
        if line == '':
            y_offset += font_instruction.get_height() // 2  # Add extra space for paragraph breaks
            continue
        line_surface = font_instruction.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(line_surface, line_rect)
        y_offset += line_surface.get_height() + 5  # Adjust spacing between lines

    # Draw "Press spacebar to begin" at the bottom (localized)
    press_space_text = translations.get('press_space', 'Press spacebar to continue')
    press_space_surface = font_instruction.render(press_space_text, True, (255, 255, 255))
    press_space_rect = press_space_surface.get_rect(center=(screen_width // 2, int(screen_height * 0.9)))
    screen.blit(press_space_surface, press_space_rect)

    # Update the display
    pygame.display.flip()

    # Wait for spacebar press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    # Clean up
    pygame.quit()

# Function to generate image paths based on language
def generate_image_paths(language):
    image_scenarios = ['training_SYSMON', 'training_TRACK', 'training_COMMUNICATIONS', 'training_RESMAN']
    image_paths = []
    lang_code = 'eng' if language == 'English' else 'fr'
    
    for scenario_key in image_scenarios:
        # Construct the glob pattern to match all images for the scenario and language
        pattern = os.path.join(
            current_directory,
            'includes',
            'img',
            f'instructions_{lang_code}_{scenario_key.replace("training_", "")}*.png'
        )
        
        # Retrieve all matching image paths and sort them
        scenario_image_paths = sorted(glob.glob(pattern))
        
        if not scenario_image_paths:
            print(f"No images found for scenario '{scenario_key}' with language '{language}'.")
            # Optionally, handle the missing images as needed
            continue  # Skip to the next scenario
        
        image_paths.extend(scenario_image_paths)
    
    return image_paths


def MATB_instructions(participant_info):
    language = participant_info.get('language', 'English')

    # Display initial reminder screen
    display_initial_reminder_screen(language)

    # Generate image paths
    image_paths = generate_image_paths(language)

    # Display the images with navigation
    display_image_gallery(image_paths, language)

    # Display the final instruction screen
    display_final_instruction_screen(language)

if __name__ == "__main__":
    # Example participant info (you can change or prompt the user)
    participant_info = {
        'participant_id': '002',  # You can prompt the user or dynamically set this
        'participant_initials': 'JD',
        'current_session': '1',
        'completed_tasks': 'MATB',
        'language': 'French'  # Change to 'French' if needed
    }
    MATB_instructions(participant_info)
