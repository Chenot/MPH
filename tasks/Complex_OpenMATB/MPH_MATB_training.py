import os
import sys
import pygame
import configparser
import subprocess
import shutil
import glob
from datetime import datetime


# Adjust the path to import functions from MPH_MATB
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

# Import the necessary functions from MPH_MATB.py
from MPH_MATB import update_config, launch_matb, save_responses

# Function to handle all text translations based on the participant's language
def get_translations(language):
    if language == 'French':
        return {
            'training_ALL_instructions': 'Entraînement complet.\n\n\nCet entraînement combinera les quatre tâches précédentes.',
            'press_space': 'Appuyez sur la barre espace pour continuer',
            'title': 'Open MATB',
            'initial_training_instructions': 'Bienvenue dans la tâche MATB.\nCette tâche est composée de quatre sous-tâches: surveillance, poursuite, communication et gestion des ressources.\nNous allons commencer par un entraînement sur chacune des quatre sous-tâches.\n\n',
            'end_training_instructions': "La formation est terminée.\n\nNous allons maintenant commencer la vraie tâche.\nCe seront des segments de 4 minutes qui peuvent être de difficulté faible ou élevée.\n\nVotre indicatif sera toujours présenté avant chaque partie.\n\nEssayez de faire de votre mieux pour gérer les quatre tâches simultanément!",
            'previous': 'Précédent',
            'next': 'Suivant'
        }
    else:  # Default to English
        return {
            'training_ALL_instructions': 'Full Training.\n\n\nThis training session will combine all four previous tasks.',
            'press_space': 'Press the spacebar to continue',
            'title': 'Open MATB',
            'initial_training_instructions': 'Welcome to the MATB task.\nThis task consists of four sub-tasks: system monitoring, tracking, communications, and resource management.\nWe will begin by doing a practice in each of the four sub-tasks.\n\n',
            'end_training_instructions': "The training is now over.\n\nWe will now start the actual task.\nThese will be 4-minute segments that can be low or high difficulty.\n\nYour callsign will always be presented before each game.\n\nTry to do your best managing the four tasks simultaneously!",
            'previous': 'Previous',
            'next': 'Next'
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

# Function to display instruction screen with text
def display_instruction_screen(title_text, instruction_text, press_space_text):
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

    # Render the title text
    text_title = font_title.render(title_text, True, (255, 255, 255))
    text_title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 6))  # Top of the screen
    screen.blit(text_title, text_title_rect)

    # Wrap and render the instruction text
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

    # Draw "Press spacebar to continue" at the bottom
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
            images.append(None)  # Placeholder

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
        screen.blit(next_button_surface, next_button_rect)

        # Update the display
        pygame.display.flip()

    # Clean up
    pygame.quit()

# Function to display the initial instruction screen with image (from original script)
def display_initial_screen(language):
    pygame.init()

    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set background color (grey)
    screen.fill((169, 169, 169))

    # Load fonts, adjust sizes as needed
    font_title = pygame.font.Font(None, int(screen_height * 0.1))  # For the title
    font_instruction = pygame.font.Font(None, int(screen_height * 0.04))  # For the instruction text

    # Get the translations based on the language
    translations = get_translations(language)

    # Render the title text
    text_title = font_title.render(translations['title'], True, (255, 255, 255))
    text_title_rect = text_title.get_rect(center=(screen_width // 2, screen_height // 10))  # Top of the screen
    screen.blit(text_title, text_title_rect)

    # Instruction text (localized)
    instructions_text = translations['initial_training_instructions']
    instruction_lines = wrap_text(instructions_text, font_instruction, screen_width * 0.8)
    instruction_start_y = screen_height // 5  # Adjust as needed

    y_offset = instruction_start_y
    for line in instruction_lines:
        if line == '':
            y_offset += font_instruction.get_height() // 2  # Add extra space for paragraph breaks
            continue
        line_surface = font_instruction.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(line_surface, line_rect)
        y_offset += line_surface.get_height() + 5  # Adjust spacing between lines

    # Load and display the image with the aspect ratio maintained  
    image_path = os.path.join(current_directory, 'includes', 'img', 'openmatb.png')
    try:
        image = pygame.image.load(image_path)
        
        # Get the original image size
        original_width, original_height = image.get_size()
        
        # Calculate the aspect ratio
        aspect_ratio = original_width / original_height
        
        # Set the maximum width and height based on the screen size, maintaining the aspect ratio
        max_width = int(screen_width * 0.5)
        max_height = int(screen_height * 0.5)
        
        # Calculate the new width and height to maintain the aspect ratio
        if max_width / aspect_ratio <= max_height:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_width = int(max_height * aspect_ratio)
            new_height = max_height
        
        # Resize the image with the new dimensions
        image = pygame.transform.scale(image, (new_width, new_height))
        
        # Place the image lower on the screen (e.g., 70% from the top of the screen)
        image_rect = image.get_rect(center=(screen_width // 2, int(screen_height * 0.62)))
        screen.blit(image, image_rect)
    except pygame.error:
        print(f"Failed to load image from {image_path}")

    # Draw "Press spacebar to continue" at the bottom (localized)
    press_space_surface = font_instruction.render(translations['press_space'], True, (255, 255, 255))
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
    instruction_text = translations['end_training_instructions']
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

    # Draw "Press spacebar to continue" at the bottom (localized)
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

# Function to run the MATB task with the given participant information and scenario
def run_matb_task(participant_info, selected_scenario):
    """
    Runs the MATB task with the given participant information and scenario.

    Parameters:
    - participant_info (dict): Information about the participant.
    - selected_scenario (str): The scenario file to use.
    """
    language = participant_info.get('language', 'English')

    # Get the translations based on the language
    translations = get_translations(language)

    # Update config.ini with the selected scenario
    update_config(selected_scenario, participant_info)

    # Extract the scenario name without extension for instruction lookup
    scenario_key = selected_scenario.replace('.txt', '')

    # Get the localized 'Press spacebar to continue' text and title
    press_space_text = translations.get('press_space', 'Press spacebar to continue')
    title_text = translations.get('title', 'Open MATB')

    # Define the list of scenarios that use images
    image_scenarios = ['training_SYSMON', 'training_TRACK', 'training_COMMUNICATIONS', 'training_RESMAN']

    if scenario_key in image_scenarios:
        # Determine the language code for filenames
        lang_code = 'eng' if language == 'English' else 'fr'

        # Construct the glob pattern to match all images for the scenario and language
        pattern = os.path.join(
            current_directory,
            'includes',
            'img',
            f'instructions_{lang_code}_{scenario_key.replace("training_", "")}*.png'
        )

        # Retrieve and sort all matching image paths
        image_paths = sorted(glob.glob(pattern))

        if not image_paths:
            print(f"No images found for scenario '{scenario_key}' with language '{language}'.")
            sys.exit(1)

        # Display the image gallery with navigation
        display_image_gallery(image_paths, language)
    else:
        # Get the instruction text for the scenario
        instruction_text = translations.get(f'{scenario_key}_instructions', 'No instructions available.')
        # Display instruction screen
        display_instruction_screen(title_text, instruction_text, press_space_text)

    # Run the MATB task
    launch_matb()

    # Save responses to BIDS-compliant format
    save_responses(participant_info, selected_scenario)

# Function to handle MATB training sequence
def MATB_training(participant_info):
    # Display the initial instruction screen
    display_initial_screen(participant_info.get('language', 'English'))

    # List of training scenarios
    training_scenarios = [
        'training_SYSMON.txt',
        'training_TRACK.txt',
        'training_COMMUNICATIONS.txt',
        'training_RESMAN.txt',
        'training_ALL.txt'
    ]

    for scenario in training_scenarios:
        run_matb_task(participant_info, scenario)

    # After training_ALL, display end_training_instructions
    # Get the translations
    language = participant_info.get('language', 'English')
    translations = get_translations(language)

    # Get the localized 'Press spacebar to continue' text and title
    press_space_text = translations.get('press_space', 'Press spacebar to continue')
    title_text = translations.get('title', 'Open MATB')

    # Get the 'end_training_instructions' text
    end_training_text = translations.get('end_training_instructions', '')

    # Display the end training instruction screen
    display_instruction_screen(title_text, end_training_text, press_space_text)

if __name__ == "__main__":
    # Example participant info (you can change or prompt the user)
    participant_info = {
        'participant_id': '002',  # You can prompt the user or dynamically set this
        'participant_initials': 'JD',
        'current_session': '1',
        'completed_tasks': 'MATB',
        'language': 'French'  # Change to 'French' if needed
    }

    MATB_training(participant_info)
