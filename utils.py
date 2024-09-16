import os
import csv
import random
import string
import shutil
import re

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

def move_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_id, session_number, task_name=None):
    """
    Moves data files from the PsychoPy data folder to the BIDS-compliant folder.

    psychopy_data_dir: The directory where PsychoPy stores the data.
    bids_folder: The BIDS-compliant folder where files should be moved.
    participant_id: The participant's ID.
    session_number: The session number.
    task_name: (Optional) The task name for BIDS-compliance. If not provided, it will be extracted from the filename.
    """
    # Check if the data directory exists
    if not os.path.exists(psychopy_data_dir):
        print(f"No data found in {psychopy_data_dir}")
        return

    # Search for PsychoPy-generated subdirectories (if they exist)
    subdirs = [d for d in os.listdir(psychopy_data_dir) if os.path.isdir(os.path.join(psychopy_data_dir, d))]
    
    # If there are subdirectories, look into them for files
    if subdirs:
        print(f"Found subdirectories: {subdirs}")
        latest_subdir = max(subdirs, key=lambda d: os.path.getctime(os.path.join(psychopy_data_dir, d)))
        psychopy_data_dir = os.path.join(psychopy_data_dir, latest_subdir, 'data')  # Adjust for the subfolder structure

    # Check if we have the correct directory now
    if not os.path.exists(psychopy_data_dir):
        print(f"No data found in {psychopy_data_dir} after checking subfolders.")
        return

    print(f"Looking for files in {psychopy_data_dir}")

    # Move and rename files
    for file_name in os.listdir(psychopy_data_dir):
        if file_name.endswith('.csv') or file_name.endswith('.psydat'):
            print(f"Processing file: {file_name}")
            
            # Extract task and timestamp if not provided
            if task_name is None:
                task_name, timestamp = extract_task_and_timestamp(file_name)
            else:
                # Use task_name provided, and extract only the timestamp
                _, timestamp = extract_task_and_timestamp(file_name)

            if task_name and timestamp:
                # Construct simplified BIDS-compliant filename
                new_file_name = f"sub-{participant_id}_ses-{session_number}_task-{task_name}_{timestamp}{os.path.splitext(file_name)[1]}"
                source_path = os.path.join(psychopy_data_dir, file_name)
                target_path = os.path.join(bids_folder, new_file_name)

                # Move file to BIDS-compliant folder
                try:
                    shutil.move(source_path, target_path)
                    print(f"Moved {source_path} to {target_path}")
                except FileNotFoundError as e:
                    print(f"Error moving file: {e}")
            else:
                print(f"Could not extract task and timestamp from file: {file_name}")


def generate_next_id(csv_file):
    """Generates the next participant ID based on existing CSV data."""
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        return '001'
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        participant_ids = sorted(int(row['participant_id']) for row in reader)
        next_id = participant_ids[-1] + 1
    
    return str(next_id).zfill(3)


def generate_random_id(length=6):
    """Generates a random anonymized participant ID."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def save_participant_info(csv_file, info):
    """Saves participant information into a CSV file."""
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'participant_id', 'participant_initials', 'participant_anonymized_id', 
            'date_session1', 'date_session2', 'date_session3', 'language', 
            'last_task', 'current_session'
        ])
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
        writer = csv.DictWriter(file, fieldnames=[
            'participant_id', 'participant_initials', 'participant_anonymized_id', 
            'date_session1', 'date_session2', 'date_session3', 'language', 
            'last_task', 'current_session'
        ])
        writer.writeheader()
        writer.writerows(rows)
