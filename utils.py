import os
import csv
import random
import string
import shutil
import re
import socket
import sys
import subprocess
import pygetwindow as gw

# Adjust the path to import LSL_metascript.py
current_directory = os.path.dirname(os.path.abspath(__file__))
lsl_metascript_directory = os.path.abspath(os.path.join(current_directory, '..', 'utils'))
gazepoint_calibration_directory = os.path.abspath(os.path.join(current_directory, '..', 'utils','LabStreamingLayer','EyeTracking'))
sys.path.append(lsl_metascript_directory)
sys.path.append(gazepoint_calibration_directory)

# Import start_recording function from LSL_metascript
from LSL_metascript import start_recording
from gazepoint_calibration import run_ET_calibration

def get_parent_directory(path):
    """Returns the parent directory of the given path."""
    return os.path.dirname(path)

def create_bids_structure(root_path, participant_id, session_number):
    """
    Creates the BIDS-compliant directory structure for a given participant and session.
    
    root_path: The root directory where the BIDS folder will be created.
    participant_id: The participant's ID.
    session_number: The current session number.
    """
    # Define BIDS folder path
    bids_data_dir = os.path.join(root_path, 'BIDS_data')

    # Create participant and session folder in BIDS structure
    participant_folder = f"sub-{participant_id}"
    session_folder = f"ses-{session_number}"
    
    session_path = os.path.join(bids_data_dir, participant_folder, session_folder)
    os.makedirs(session_path, exist_ok=True)
    
    return session_path  # Return the session path to store task files directly

def extract_task_and_timestamp(file_name):
    """
    Extracts the task name and timestamp from the file name.
    Assumes filenames are formatted like: '001_taskName_YYYY-MM-DD_HH-MM-SS.csv'
    """
    pattern = r'(\d+)_(\w+)_([\d-]+_[\d-]+)'
    match = re.match(pattern, file_name)
    
    if match:
        participant_id = match.group(1)
        task_name = match.group(2)
        timestamp = match.group(3)
        return task_name, timestamp
    return None, None

def copy_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_id, session_number): 
    """
    Copies all relevant data files from the PsychoPy data folder to the BIDS-compliant folder.

    psychopy_data_dir: The directory where PsychoPy stores the data.
    bids_folder: The BIDS-compliant folder where files should be copied.
    participant_id: The participant's ID (to filter relevant files).
    session_number: The session number (to include in the BIDS-compliant filenames).
    """
    # Check if the data directory exists
    if not os.path.exists(psychopy_data_dir):
        print(f"No data found in {psychopy_data_dir}")
        return

    # Search for PsychoPy-generated subdirectories
    subdirs = [d for d in os.listdir(psychopy_data_dir) if os.path.isdir(os.path.join(psychopy_data_dir, d))]
    
    for subdir in subdirs:
        subdir_path = os.path.join(psychopy_data_dir, subdir, 'data')

        # Check if the 'data' folder exists in the subdirectory
        if not os.path.exists(subdir_path):
            print(f"No data found in {subdir_path}")
            continue
        else:
            print(f"Looking for files in {subdir_path}")

        # Process all files that match the participant ID and are either .csv or .psydat
        for file_name in os.listdir(subdir_path):
            if file_name.startswith(participant_id) and (file_name.endswith('.csv') or file_name.endswith('.psydat')):
                print(f"Processing file: {file_name}")
                
                # Construct BIDS-compliant filename
                task_name, timestamp = extract_task_and_timestamp(file_name)
                if task_name and timestamp:
                    new_file_name = f"sub-{participant_id}_ses-{session_number}_task-{task_name}_{timestamp}{os.path.splitext(file_name)[1]}"
                    source_path = os.path.join(subdir_path, file_name)
                    target_path = os.path.join(bids_folder, new_file_name)

                    # Copy the file to the BIDS-compliant folder
                    try:
                        shutil.copy2(source_path, target_path)
                        print(f"Copied {source_path} to {target_path}")
                    except FileNotFoundError as e:
                        print(f"Error copying file: {e}")
                else:
                    print(f"Could not extract task and timestamp from file: {file_name}")

def generate_next_id(csv_file):
    """Generates the next participant ID based on existing CSV data."""
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        # If the CSV doesn't exist or is empty, return the first ID '001'
        return '001'
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        participant_ids = [int(row['participant_id']) for row in reader if row['participant_id']]

    # If no participant IDs are found, start from '001'
    if not participant_ids:
        return '001'

    # Return the next participant ID by incrementing the last ID
    next_id = max(participant_ids) + 1
    return str(next_id).zfill(3)  # Pad with zeros (e.g., '001', '002')


def generate_random_id(length=6):
    """Generates a random anonymized participant ID."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def save_participant_info(csv_file, info):
    """Saves participant information into the CSV file, appending if necessary."""
    file_exists = os.path.isfile(csv_file)
    
    fieldnames = [
        'participant_id', 'participant_initials', 'participant_anonymized_id', 
        'date_session1', 'date_session2', 'date_session3', 'language', 
        'current_session', 'completed_tasks'
    ]

    if 'completed_tasks' in info and isinstance(info['completed_tasks'], list):
        info['completed_tasks'] = ','.join(info['completed_tasks'])

    # Append participant info (new row) if it doesn't exist
    if not file_exists or not participant_exists(csv_file, info['participant_id']):
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(info)

def participant_exists(csv_file, participant_id):
    """Checks if a participant already exists in the CSV."""
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['participant_id'] == participant_id:
                    return True
    return False

def load_participant_info(csv_file, participant_id):
    """Loads participant information by ID from a CSV file."""
    if not os.path.exists(csv_file):
        return None
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['participant_id'] == participant_id:
                return row
    return None

def get_participant_info(csv_file, participant_id):
    """Retrieves participant information from the CSV file."""
    if not os.path.exists(csv_file):
        return None
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['participant_id'] == participant_id:
                participant_info = dict(row)
                # Convert 'completed_tasks' from a comma-separated string to a list
                completed_tasks = participant_info.get('completed_tasks', '')
                if isinstance(completed_tasks, str):
                    participant_info['completed_tasks'] = completed_tasks.split(',') if completed_tasks else []
                else:
                    participant_info['completed_tasks'] = []
                return participant_info
    return None

def update_participant_info(csv_file, info):
    """Updates participant information in the CSV file, only modifying the participant's line."""
    fieldnames = [
        'participant_id', 'participant_initials', 'participant_anonymized_id', 
        'date_session1', 'date_session2', 'date_session3', 'language', 
        'current_session', 'completed_tasks'
    ]

    # Ensure 'completed_tasks' is a string before writing
    if 'completed_tasks' in info:
        if isinstance(info['completed_tasks'], list):
            info['completed_tasks'] = ','.join(info['completed_tasks'])
        elif not isinstance(info['completed_tasks'], str):
            # If it's neither a list nor a string, set it to an empty string
            info['completed_tasks'] = ''
    else:
        # If 'completed_tasks' is missing, add it as an empty string
        info['completed_tasks'] = ''

    # Filter the `info` dictionary to only include keys in `fieldnames`
    filtered_info = {key: info[key] for key in fieldnames if key in info}

    # Read all rows, update only the participant's line
    updated = False
    rows = []

    # Read the current file and update the relevant row
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['participant_id'] == filtered_info['participant_id']:
                    rows.append(filtered_info)  # Update this participant's info
                    updated = True
                else:
                    rows.append(row)
    else:
        # If the file doesn't exist, we'll create a new one
        rows.append(filtered_info)
        updated = True

    # If no update was made (participant was not found), append new info
    if not updated:
        rows.append(filtered_info)

    # Write everything back
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run_EyeTracking_Calibration(participant_info):
    run_ET_calibration(participant_info)

def launch_lsl_metascript(participant_info):
    """Launch the LSL metascript by calling the recording function directly."""
    recording_started = start_recording(participant_info)
    if recording_started:
        print("LSL_metascript recording started successfully.")
    else:
        raise Exception("Recording did not start due to missing streams.")

def minimize_all_windows():
    """Minimizes all application windows."""
    for window in gw.getAllWindows():
        try:
            window.minimize()
        except Exception as e:
            print(f"Could not minimize window {window.title}: {e}")
            
# Function to send a command to LabRecorder and get the response
def send_command_to_labrecorder(command):
    s = socket.create_connection(("localhost", 22345))
    s.settimeout(1)  # Set a timeout to prevent blocking
    s.sendall(command.encode('utf-8'))
    response = ''
    try:
        while True:
            data = s.recv(4096).decode('utf-8')
            if not data:
                break
            response += data
            if '\n' in data:
                break
    except socket.timeout:
        pass  # Ignore timeout errors
    s.close()
    return response

def close_applications():
    # List of target process names to close
    target_process_names = ['LabRecorder.exe', 'Keyboard.exe', 'Gazepoint Control x64', 'Biosemi.exe']
    
    # Terminate target processes by name using taskkill
    for process_name in target_process_names:
        try:
            subprocess.run(['taskkill', '/f', '/im', process_name], check=True)
            print(f"Terminated process: {process_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to terminate process {process_name}: {e}")
    
    # Close application windows by title
    windows_to_close = ['LabRecorder', 'BioSemi', 'Keyboard', 'Gazepoint Control']
    windows = gw.getAllWindows()
    for window in windows:
        if any(title in window.title for title in windows_to_close):
            try:
                window.close()
                print(f"Closed window: {window.title}")
            except Exception as e:
                print(f"Failed to close window {window.title}: {e}")

    print("Closed specified applications and windows.")
    