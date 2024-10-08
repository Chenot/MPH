import os
import csv
import random
import string
import shutil
import re
import socket
import sys

# Adjust the path to import LSL_metascript.py
current_directory = os.path.dirname(os.path.abspath(__file__))
lsl_metascript_directory = os.path.abspath(os.path.join(current_directory, '..', 'utils'))
sys.path.append(lsl_metascript_directory)

# Import start_recording function from LSL_metascript
from LSL_metascript import start_recording



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
    # Check if the data directory exists - DEBUG
    #if not os.path.exists(psychopy_data_dir):
    #    print(f"No data found in {psychopy_data_dir}")
    #    return

    # Search for PsychoPy-generated subdirectories
    subdirs = [d for d in os.listdir(psychopy_data_dir) if os.path.isdir(os.path.join(psychopy_data_dir, d))]
    
    #if not subdirs: # DEBUG
    #    print(f"No subdirectories found in {psychopy_data_dir}")
    #    return
    #
    # print(f"Found subdirectories: {subdirs}")

    # Iterate over all subdirectories to find matching files
    for subdir in subdirs:
        subdir_path = os.path.join(psychopy_data_dir, subdir, 'data')

        # Check if the data folder exists in the subdirectory # DEBUG
        #if not os.path.exists(subdir_path):
        #    print(f"No data found in {subdir_path}")
        #    continue
        #print(f"Looking for files in {subdir_path}")

        # Process all files that match the participant ID and are either .csv or .psydat
        for file_name in os.listdir(subdir_path):
            if file_name.startswith(participant_id) and (file_name.endswith('.csv') or file_name.endswith('.psydat')):
                #print(f"Processing file: {file_name}")
                
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
    """Saves participant information into a CSV file."""
    file_exists = os.path.isfile(csv_file)
    
    # Update the fieldnames to match the updated structure
    fieldnames = [
        'participant_id', 'participant_initials', 'participant_anonymized_id', 
        'date_session1', 'date_session2', 'date_session3', 'language', 
        'current_session', 'completed_tasks'
    ]
    
    # Ensure completed_tasks is serialized as a string for CSV
    if 'completed_tasks' in info and isinstance(info['completed_tasks'], list):
        info['completed_tasks'] = ','.join(info['completed_tasks'])  # Convert list to string
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(info)


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


def update_participant_info(csv_file, info):
    """Updates participant information in the CSV file."""
    fieldnames = [
        'participant_id', 'participant_initials', 'participant_anonymized_id', 
        'date_session1', 'date_session2', 'date_session3', 'language', 
        'current_session', 'completed_tasks'
    ]
    
    # Convert completed_tasks list to a string for CSV storage
    if 'completed_tasks' in info and isinstance(info['completed_tasks'], list):
        info['completed_tasks'] = ','.join(info['completed_tasks'])  # Convert list to string
    
    rows = []

    # Read current data and update the row corresponding to the participant
    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['participant_id'] == info['participant_id']:
                    rows.append(info)
                else:
                    rows.append(row)

    # Write updated data back to the file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def launch_lsl_metascript(participant_info):
    """Launch the LSL metascript by calling the recording function directly."""
    try:
        start_recording(participant_info)
        print("LSL_metascript recording started successfully.")
    except Exception as e:
        print(f"Error starting LSL_metascript recording: {e}")

# Function to send a command to LabRecorder and get the response
def send_command_to_labrecorder(command):
    s = socket.create_connection(("localhost", 22346))
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