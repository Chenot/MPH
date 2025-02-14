import configparser
import subprocess
import pygame
import sys
import os
import time
import shutil
from datetime import datetime
import tkinter as tk
import threading

# Adjust the path to import oddball script
current_directory = os.path.dirname(os.path.abspath(__file__))
oddball_directory = os.path.join(current_directory, '..', 'Perception_Oddball')
sys.path.append(oddball_directory)
from oddball_task import start_oddball

# Define the base directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Function to update the config.ini file
def update_config(scenario_file, participant_info):
    config_path = os.path.join(script_dir, "config.ini")
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_path)

    # Check if 'Openmatb' section exists
    if not config.has_section('Openmatb'):
        raise configparser.NoSectionError('Openmatb')
        
    # Determine language code based on participant_info
    language = participant_info.get('language', 'English')
    language_code = 'fr_FR' if language == 'French' else 'en_EN'

    # Write the updated configuration back to the file
    with open(config_path, "w", encoding='utf-8') as config_file:
        config_file.write(
            "# Copyright 2023, by Julien Cegarra & Benoît Valéry. All rights reserved.\n"
            "# Institut National Universitaire Champollion (Albi, France).\n"
            "# License : CeCILL, version 2.1 (see the LICENSE file)\n\n"
            "[Openmatb]\n"
            "# If language is missing, en_EN will be loaded\n"
            f"language={language_code}\n\n" 
            "# If multiple screens layout, you can modify the index\n"
            "# Default : screen_index=0\n"
            f"screen_index={config.get('Openmatb', 'screen_index')}\n\n"
            "# If you don't like the default font, feel free to specify a different one below.\n"
            "# (Leave it empty to get your system default font)\n"
            f"font_name={config.get('Openmatb', 'font_name')}\n\n"
            "# Fullscreen mode\n"
            "# Default : fullscreen=True\n"
            f"fullscreen={config.get('Openmatb', 'fullscreen')}\n\n"
            "# Scenario choice\n"
            f"scenario_path={scenario_file}\n\n"
            "# Display the session number at start\n"
            f"display_session_number={config.get('Openmatb', 'display_session_number')}\n\n"
            "# Hide the MATB environment on pause (\"P\" or \"Escape\" keys)\n"
            f"hide_on_pause={config.get('Openmatb', 'hide_on_pause')}\n\n"
            "# Highlight widgets area of interest (AOI)\n"
            "# If True, will display a red frame around each widget, as well as its name\n"
            f"highlight_aoi={config.get('Openmatb', 'highlight_aoi')}\n\n"
            "# Vertical bounds between plugins areas\n"
            "# (Warning: modify only if you need to change plugins from their initial default location)\n"
            "# Default values: top_bounds=[0.35, 0.85] | bottom_bounds=[0.30, 0.85]\n"
            f"top_bounds={config.get('Openmatb', 'top_bounds')}\n"
            f"bottom_bounds={config.get('Openmatb', 'bottom_bounds')}\n"
        )

# Function to launch the MATB task by running main.py using the virtual environment's python interpreter
def launch_matb():
    python_executable = os.path.join(script_dir, '.venv', 'Scripts', 'python.exe')
    main_script = os.path.join(script_dir, 'main.py')

    if not os.path.exists(python_executable):
        print(f"[WARNING] The specified Python executable does not exist: {python_executable}")
    else:
        print(f"Launching MATB with Python executable: {python_executable}")

    # Print what directory we are about to use for subprocess
    print(f"Using script_dir as the working directory (cwd): {script_dir}")

    # Also print Python's current working directory (just for clarity)
    print(f"Python's current working directory (os.getcwd()): {os.getcwd()}")

    # Optionally check Python version in that .venv:
    version_check = subprocess.Popen(
        [python_executable, "--version"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    stdout, _ = version_check.communicate()
    print("Reported Python version from .venv is:", stdout.strip())

    # Launch MATB and wait for it to finish
    process = subprocess.Popen(
        [python_executable, main_script],
        cwd=script_dir,        # Make sure to set your desired working directory
        shell=True
    )
    
    # Wait for the MATB task to complete
    process.wait()
    print("MATB task has completed.")

# Function to check if the scenario is an oddball scenario
def is_oddball_scenario(scenario_file):
    return 'oddball' in scenario_file

# Function to run MATB and Oddball tasks simultaneously
def run_tasks_concurrently():
    # Create threads for both MATB and Oddball
    matb_thread = threading.Thread(target=launch_matb)
    oddball_thread = threading.Thread(target=start_oddball)

    # Start both threads
    matb_thread.start()
    oddball_thread.start()

    # Optionally, you can join the threads to ensure the main script waits for both tasks to complete
    matb_thread.join()
    oddball_thread.join()

# Function to parse the scenario file and extract the callsign
def get_callsign(scenario_file):
    callsign = "Unknown"
    
    with open(scenario_file, 'r') as file:
        lines = file.readlines()
        
        # Find the owncallsign in the scenario file
        for line in lines:
            if 'communications;owncallsign;' in line:
                callsign = line.strip().split(';')[-1]
                
    return callsign

# Function to display a generic start screen
def display_start_screen(title_text, instruction_text, callsign, oddball_presence):
    pygame.init()
    
    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set background color (grey)
    screen.fill((169, 169, 169))
    
    # Load a bold font for the title, dynamically adjusting the font size
    font_bold_large = pygame.font.Font(None, int(screen_height * 0.1))  # 10% of the screen height for the title
    font_medium = pygame.font.Font(None, int(screen_height * 0.06))     # 6% for callsign and oddball status
    font_small = pygame.font.Font(None, int(screen_height * 0.05))      # 5% for the instruction text
    
    # Render the title, instruction, callsign, and oddball presence texts
    text_large = font_bold_large.render(title_text, True, (255, 255, 255))
    text_callsign = font_medium.render(f'Callsign: {callsign}', True, (255, 255, 255))
    text_oddball = font_medium.render(f'Oddball: {oddball_presence}', True, (255, 255, 255))
    text_small = font_small.render(instruction_text, True, (255, 255, 255))

    # Get text rectangles and center them
    text_large_rect = text_large.get_rect(center=(screen_width // 2, screen_height // 6))  # Top of the screen
    text_callsign_rect = text_callsign.get_rect(center=(screen_width // 2, screen_height // 2.2))  # Centered
    text_oddball_rect = text_oddball.get_rect(center=(screen_width // 2, screen_height // 1.9))    # Centered below callsign
    text_small_rect = text_small.get_rect(center=(screen_width // 2, screen_height * 0.9))  # Bottom of the screen
    
    # Draw text to the screen
    screen.blit(text_large, text_large_rect)
    screen.blit(text_callsign, text_callsign_rect)
    screen.blit(text_oddball, text_oddball_rect)
    screen.blit(text_small, text_small_rect)
    
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

# Function to handle all text translations based on the participant's language
def get_translations(language):
    if language == 'French':
        return {
            'title': 'Open MATB',
            'instruction': 'Appuyez sur la barre espace pour commencer',
            'oddball_yes': "oui (appuyez sur 'E' lorsque vous entendez un bruit aigu)",
            'oddball_no': 'non',
        }
    else:  # Default to English
        return {
            'title': 'Open MATB',
            'instruction': 'Press spacebar to start',
            'oddball_yes': "yes (press 'E' when you hear high-pitched noise)",
            'oddball_no': 'no',
        }

def save_responses(participant_info, selected_scenario):
    """Save the generated files in a BIDS-compliant format."""
    
    # Extract the relevant part of the scenario for the filename (e.g., "easy", "easy_oddball")
    scenario = "_".join(selected_scenario.split('_')[1:]).replace('.txt', '')
    
    # Get participant and session info
    participant_id = participant_info.get('participant_id', 'unknown')
    session_id = participant_info.get('current_session', '1')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Get the current directory and create the BIDS-compliant path
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    bids_directory = os.path.abspath(os.path.join(current_directory, '..', '..', 'BIDS_data'))

    # Create BIDS-compliant folder structure
    bids_sub_dir = os.path.join(bids_directory, f"sub-{participant_id}", f"ses-{session_id}")
    os.makedirs(bids_sub_dir, exist_ok=True)  # Ensure the directory exists

    # Define the BIDS filename based on the scenario
    bids_filename = f"sub-{participant_id}_ses-{session_id}_task-MATB_{scenario}_{timestamp}.csv"
    bids_file_path = os.path.join(bids_sub_dir, bids_filename)

    # Path to the generated files (adapt this path based on your folder structure)
    session_date = datetime.now().strftime("%Y-%m-%d")
    data_directory = os.path.join(current_directory, 'sessions', session_date)

    # Copy generated files to the BIDS directory
    for file_name in os.listdir(data_directory):
        full_file_name = os.path.join(data_directory, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, bids_file_path)
    print(f"MATB data saved to {bids_file_path}")
    
# Main function for running the full process
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

    # Parse the scenario to get the callsign
    scenario_file = os.path.join(script_dir, "includes", "scenarios", selected_scenario)
    callsign = get_callsign(scenario_file)
    
    # Check if this is an oddball scenario using the scenario filename
    oddball_presence = translations['oddball_yes'] if is_oddball_scenario(selected_scenario) else translations['oddball_no']
    
    # Display MATB start screen with the callsign and oddball status
    display_start_screen(translations['title'], translations['instruction'], callsign, oddball_presence)
    
    # If it's an oddball scenario, run MATB and Oddball tasks concurrently
    if is_oddball_scenario(selected_scenario):
        run_tasks_concurrently()
    else:
        # Otherwise, just run the MATB task
        launch_matb()

if __name__ == "__main__":
    # Example participant info and scenario (you can change or pass these dynamically)
    participant_info = {
        'participant_id': '002',  # You can prompt the user or dynamically set this
        'participant_initials': 'JD',
        'current_session': '1',
        'completed_tasks': 'MATB',
        'language': 'English'
    }

    selected_scenario = "session-2_easy_oddball.txt"  # You can change or select this dynamically

    # Run the MATB task
    run_matb_task(participant_info, selected_scenario)
