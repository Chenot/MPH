import os
from datetime import datetime
import logging
import random
import string
import shutil
import re
import socket
import sys
import webbrowser
import psutil
import pygetwindow as gw
import sqlite3

# Adjust paths to import LSL_metascript/gazepoint_calibration
current_directory = os.path.dirname(os.path.abspath(__file__))
lsl_metascript_directory = os.path.abspath(os.path.join(current_directory, '..', 'utils'))
gazepoint_calibration_directory = os.path.abspath(
    os.path.join(current_directory, '..', 'utils', 'LabStreamingLayer', 'EyeTracking')
)
sys.path.append(lsl_metascript_directory)
sys.path.append(gazepoint_calibration_directory)

# ----------------------------------------------------------------
# Import from LSL/gazepoint scripts
# ----------------------------------------------------------------
from LSL_metascript import start_recording
from gazepoint_calibration import run_ET_calibration


# ------------------ Database helper functions ------------------
def get_db_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_file):
    """Creates the participants table if it does not already exist."""
    conn = get_db_connection(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS participants (
         participant_id TEXT PRIMARY KEY,
         participant_initials TEXT,
         participant_anonymized_id TEXT,
         date_session1 TEXT,
         date_session2 TEXT,
         date_session3 TEXT,
         language TEXT,
         current_session TEXT,
         completed_tasks TEXT
         )''')
    conn.commit()
    conn.close()


# ----------------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------------
def open_url(url):
    """Opens the given URL in the default web browser."""
    webbrowser.open(url)

def get_parent_directory(path):
    """Returns the parent directory of the given path."""
    return os.path.dirname(path)


def create_bids_structure(root_path, participant_id, session_number):
    """
    Creates the BIDS-compliant directory structure for a given participant and session.
    Returns the path to the session folder.
    """
    bids_data_dir = os.path.join(root_path, 'BIDS_data')
    participant_folder = f"sub-{participant_id}"
    session_folder = f"ses-{session_number}"

    session_path = os.path.join(bids_data_dir, participant_folder, session_folder)
    os.makedirs(session_path, exist_ok=True)
    return session_path


def extract_task_and_timestamp(file_name):
    """
    Extracts the task name and timestamp from the file name.
    Assumes filenames are like '001_taskName_YYYY-MM-DD_HH-MM-SS.csv'.
    """
    pattern = r'(\d+)_(\w+)_([\d-]+_[\d-]+)'
    match = re.match(pattern, file_name)
    if match:
        task_name = match.group(2)
        timestamp = match.group(3)
        return task_name, timestamp
    return None, None


def extract_date_from_filename(file_name):
    """Extracts the date 'YYYY-MM-DD' from a filename like '001_task_YYYY-MM-DD_HH-MM-SS.csv'."""
    parts = file_name.split('_')
    # Typically, parts[2] is 'YYYY-MM-DD'
    return datetime.strptime(parts[2], '%Y-%m-%d').date()


def copy_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_id, session_number):
    """
    Copies all relevant data files from the PsychoPy data folder to the BIDS-compliant folder.

    psychopy_data_dir: The directory where PsychoPy stores the data.
    bids_folder: The BIDS-compliant folder where files should be copied.
    participant_id: The participant's ID (to filter relevant files).
    session_number: The session number (to include in the BIDS-compliant filenames).
    """
    if not os.path.exists(psychopy_data_dir):
        print(f"No data found in {psychopy_data_dir}")
        return

    # Get today's date string in the format "YYYY-MM-DD"
    today_str = datetime.now().strftime('%Y-%m-%d')

    # Search for subdirectories that start with today's date
    subdirs = [
        d for d in os.listdir(psychopy_data_dir) 
        if os.path.isdir(os.path.join(psychopy_data_dir, d)) and d.startswith(today_str)
    ]
    
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

                # Construct BIDS-compliant filename (assuming you have extract_task_and_timestamp function)
                task_name, timestamp = extract_task_and_timestamp(file_name)
                if task_name and timestamp:
                    new_file_name = f"sub-{participant_id}_ses-{session_number}_task-{task_name}_{timestamp}{os.path.splitext(file_name)[1]}"
                    source_path = os.path.join(subdir_path, file_name)
                    target_path = os.path.join(bids_folder, new_file_name)

                    try:
                        shutil.copy2(source_path, target_path)
                        print(f"Copied {source_path} to {target_path}")
                    except FileNotFoundError as e:
                        print(f"Error copying file: {e}")
                else:
                    print(f"Could not extract task and timestamp from file: {file_name}")


def generate_next_id(db_file):
    """Generates the next participant ID based on existing DB data (e.g., '001','002', etc.)."""
    init_db(db_file)
    conn = get_db_connection(db_file)
    c = conn.cursor()
    c.execute("SELECT MAX(CAST(participant_id AS INTEGER)) FROM participants")
    result = c.fetchone()[0]
    if result is None:
        next_id = 1
    else:
        next_id = int(result) + 1
    conn.close()
    return str(next_id).zfill(3)


def generate_random_id(length=6):
    """Generates a random anonymized participant ID."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def save_participant_info(db_file, info):
    """Saves new participant info into the DB if the participant does not already exist."""
    init_db(db_file)
    if 'completed_tasks' in info and isinstance(info['completed_tasks'], list):
        info['completed_tasks'] = ','.join(info['completed_tasks'])
    if not participant_exists(db_file, info['participant_id']):
        conn = get_db_connection(db_file)
        c = conn.cursor()
        c.execute('''INSERT INTO participants 
                    (participant_id, participant_initials, participant_anonymized_id, date_session1, date_session2, date_session3, language, current_session, completed_tasks)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (info['participant_id'], info['participant_initials'], info['participant_anonymized_id'],
                     info['date_session1'], info['date_session2'], info['date_session3'], info['language'],
                     info['current_session'], info['completed_tasks']))
        conn.commit()
        conn.close()


def participant_exists(db_file, participant_id):
    """Check if a participant_id row exists in the DB."""
    init_db(db_file)
    conn = get_db_connection(db_file)
    c = conn.cursor()
    c.execute("SELECT 1 FROM participants WHERE participant_id = ?", (participant_id,))
    exists = c.fetchone() is not None
    conn.close()
    return exists


def load_participant_info(db_file, participant_id):
    """Loads participant info by ID from the DB, or returns None if not found."""
    init_db(db_file)
    conn = get_db_connection(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM participants WHERE participant_id = ?", (participant_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_participant_info(db_file, participant_id):
    """Retrieve participant info from DB, converting completed_tasks to a list."""
    info = load_participant_info(db_file, participant_id)
    if info:
        tasks_str = info.get('completed_tasks', '')
        if isinstance(tasks_str, str):
            info['completed_tasks'] = tasks_str.split(',') if tasks_str else []
        else:
            info['completed_tasks'] = []
    return info


def update_participant_info(db_file, info):
    """Updates a participant's info in the DB, matching by participant_id."""
    init_db(db_file)
    if 'completed_tasks' in info:
        if isinstance(info['completed_tasks'], list):
            info['completed_tasks'] = ','.join(info['completed_tasks'])
        elif not isinstance(info['completed_tasks'], str):
            info['completed_tasks'] = ''
    else:
        info['completed_tasks'] = ''
    conn = get_db_connection(db_file)
    c = conn.cursor()
    c.execute('''UPDATE participants
                 SET participant_initials = ?,
                     participant_anonymized_id = ?,
                     date_session1 = ?,
                     date_session2 = ?,
                     date_session3 = ?,
                     language = ?,
                     current_session = ?,
                     completed_tasks = ?
                 WHERE participant_id = ?''',
              (info.get('participant_initials'), info.get('participant_anonymized_id'),
               info.get('date_session1'), info.get('date_session2'), info.get('date_session3'),
               info.get('language'), info.get('current_session'), info.get('completed_tasks'),
               info.get('participant_id')))
    conn.commit()
    conn.close()

def increment_session(participant_info, db_file):
    """
    Updates the participant's session date (for the current session) and increments the session number.
    This should be called only after all tasks have been completed without error.
    """
    current_session = participant_info['current_session']
    session_key = f"date_session{current_session}"
    participant_info[session_key] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    participant_info['current_session'] = str(int(current_session) + 1)
    update_participant_info(db_file, participant_info)


def run_EyeTracking_Calibration(participant_info):
    """Just calls the Gazepoint calibration script from gazepoint_calibration.py"""
    run_ET_calibration(participant_info)


def launch_lsl_metascript(participant_info):
    """
    Launch the LSL metascript by directly calling start_recording().
    Raises Exception if streams are missing.
    """
    recording_started = start_recording(participant_info)
    if recording_started:
        print("LSL_metascript recording started successfully.")
    else:
        raise Exception("Recording did not start due to missing streams.")


def minimize_all_windows():
    """Minimizes all application windows using pygetwindow."""
    for window in gw.getAllWindows():
        try:
            window.minimize()
        except Exception as e:
            print(f"Could not minimize window {window.title}: {e}")


def send_command_to_labrecorder(command):
    """
    Sends a command to LabRecorder (listening on localhost:22345),
    returns the response (if any).
    """
    s = socket.create_connection(("localhost", 22345))
    s.settimeout(1)
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
        pass
    s.close()
    return response

def close_applications():
    # List of target process names to close
    target_process_names = ['LabRecorder.exe', 'Keyboard.exe', 'Gazepoint Control x64', 'BioSemi.exe']
    
    # Close processes by name using psutil
    for process_name in target_process_names:
        try:
            # Iterate over all processes to find matching ones
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == process_name:
                    # Terminate process
                    proc.terminate()
                    print(f"Terminated process: {process_name} with PID {proc.info['pid']}")
                    try:
                        # Wait for the process to terminate fully
                        proc.wait(timeout=3)
                    except psutil.TimeoutExpired:
                        # Force kill if termination fails
                        proc.kill()
                        print(f"Force killed process: {process_name} with PID {proc.info['pid']}")
        except Exception as e:
            print(f"Error while terminating process {process_name}: {e}")

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
    
    
# ----------------------------------------------------------------
# perform_post_task_steps
# ----------------------------------------------------------------
def perform_post_task_steps(participant_info, db_file, psychopy_data_dir):
    """
    Performs post-task steps in order, logging any errors:
      1) Stop LabRecorder
      2) Move data to BIDS
      3) Close external applications
    """
    log_messages = []
    current_session = participant_info['current_session']
    bids_folder = None

    # ------------------ STEP 1) Stop LabRecorder ------------------
    try:
        send_command_to_labrecorder('stop\n')
        log_messages.append("LabRecorder stopped.")
    except Exception as e:
        log_messages.append(f"Error while stopping LabRecorder: {repr(e)}")

    # ------------------ STEP 2) Move data to BIDS ------------------
    try:
        root_path = get_parent_directory(os.path.dirname(__file__))
        bids_folder = create_bids_structure(root_path, participant_info['participant_id'], current_session)
        copy_psychopy_data_to_bids(psychopy_data_dir, bids_folder,
                                   participant_info['participant_id'], current_session)
    except Exception as e:
        log_messages.append(f"Error copying data to BIDS: {repr(e)}")

    # ------------------ STEP 3) Close external applications ------------------
    try:
        close_applications()
        log_messages.append("Closed external applications.")
    except Exception as e:
        log_messages.append(f"Error while closing applications: {repr(e)}")

    # At this point, you can also log that the post-task steps completed.
    for msg in log_messages:
        # If you are using the logging module, you could write:
        # logging.info(msg)
        print(msg)
