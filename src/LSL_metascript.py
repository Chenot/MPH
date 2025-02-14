import os
import subprocess
import time
import socket
import sys
import tkinter as tk
from tkinter import messagebox
import pygetwindow as gw  # For window manipulation
import pyautogui  # For automating mouse clicks
from pylsl import resolve_streams  # For checking available LSL streams

# Get the base directory (assuming the script is located in the 'utils' folder)
base_dir = os.path.dirname(os.path.abspath(__file__))
bids_data_dir = os.path.join(base_dir, '..', 'BIDS_data')

# Adjusted paths based on your instruction
labrecorder_path = os.path.join(base_dir, '..', 'ext', 'LabRecorder', 'LabRecorder.exe')
keyboard_exe_path = os.path.join(base_dir, '..', 'ext',  'LabStreamingLayerScripts', 'APPS', 'Keyboard', 'Keyboard.exe')
biosemi_exe_path = os.path.join(base_dir, '..', 'ext',  'LabStreamingLayerScripts', 'APPS', 'BioSemi', 'BioSemi.exe')
eye_tracking_py_path = os.path.join(base_dir, '..', 'ext',  'LabStreamingLayerScripts', 'EyeTracking', 'EyeTracking.py')
experimental_py_path = os.path.join(base_dir, '..', 'ext',  'LabStreamingLayerScripts', 'Experimental', 'Experimental.py')

# Function to create BIDS-compliant directory and file paths
def create_bids_path(participant_info):
    sub_id = f"sub-{participant_info['participant_id']}"
    ses_id = f"ses-{participant_info['current_session']}"

    # Create the directory structure if it doesn't exist
    participant_dir = os.path.join(bids_data_dir, sub_id, ses_id)
    if not os.path.exists(participant_dir):
        os.makedirs(participant_dir)

    # Create the filename based on participant and session info
    filename = os.path.join(participant_dir, f"{sub_id}_{ses_id}_task_all_physiological_recordings.xdf")

    return filename

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

# Function to set the LabRecorder save path and parameters via a socket connection
def set_labrecorder_filename(labrecorder_path, save_filename, participant_info):
    # Launch LabRecorder
    labrecorder_process = subprocess.Popen([labrecorder_path])
    print("Launched LabRecorder.")

    # Wait for LabRecorder to be ready
    time.sleep(2)

    # Connect to LabRecorder's socket
    s = socket.create_connection(("localhost", 22345))

    # Create the filename command for LabRecorder
    filename_command = f"filename {{root:{os.path.dirname(save_filename)}}} {{template:{os.path.basename(save_filename)}}} {{task:RS}} {{session:{participant_info['current_session']}}} {{participant:{participant_info['participant_id']}}}\n"

    # Send the command to LabRecorder
    s.sendall(filename_command.encode('utf-8'))
    print(f"Set LabRecorder save path to: {save_filename}")
    s.close()

    return labrecorder_process  # Return the process object


# Function to parse the list of streams from LabRecorder's response
def parse_streams_from_response(response):
    # Parse the response from LabRecorder to extract stream names
    lines = response.strip().split('\n')
    streams = []
    for line in lines:
        if line.startswith('['):
            # Line format is '[1] StreamName'
            parts = line.split('] ')
            if len(parts) == 2:
                stream_name = parts[1]
                streams.append(stream_name)
    return streams

# Function to launch an executable or Python script
def launch_executable(exe_path, is_python_script=False):
    if os.path.exists(exe_path):
        try:
            devnull = open(os.devnull, 'wb')
            if is_python_script:
                process = subprocess.Popen([sys.executable, exe_path], stdout=devnull, stderr=devnull)
            else:
                process = subprocess.Popen([exe_path], stdout=devnull, stderr=devnull)
            print(f"Launched: {exe_path}")
            return process  # Return the process object
        except Exception as e:
            print(f"Failed to launch {exe_path}: {e}")
            return None
    else:
        print(f"File not found: {exe_path}")
        return None


def launch_gazepoint():
    # Path to the Gazepoint executable
    exe_path = r"C:\Program Files (x86)\Gazepoint\Gazepoint\bin64\Gazepoint.exe"

    try:
        # Launch the Gazepoint executable
        gazepoint_process = subprocess.Popen(exe_path)
        print("Gazepoint Control launched successfully.")
        time.sleep(5)
        return gazepoint_process  # Return the process object
    except FileNotFoundError:
        print(f"Executable not found at {exe_path}. Please check the path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to launch Keyboard.exe and click the 'link' button
def launch_keyboard_and_click_link(exe_path):
    if os.path.exists(exe_path):
        try:
            # Launch the Keyboard.exe
            keyboard_process = subprocess.Popen([exe_path])
            print(f"Launched: {exe_path}")
        except Exception as e:
            print(f"Failed to launch {exe_path}: {e}")
            return None
    else:
        print(f"File not found: {exe_path}")
        return None

    # Wait for the window to appear
    time.sleep(2)  # Adjust the sleep time as needed

    # Find the window titled 'Keyboard'
    windows = gw.getWindowsWithTitle('Keyboard')
    if not windows:
        print("Keyboard window not found.")
        return
    else:
        keyboard_window = windows[0]

    # Bring the window to the front
    keyboard_window.activate()
    time.sleep(0.5)  # Give time for the window to activate

    # Get window position
    left, top = keyboard_window.left, keyboard_window.top

    # Coordinates of the "link" button relative to the window
    x_offset = 75   # Horizontal offset from the top-left corner of the window
    y_offset = 60   # Vertical offset from the top-left corner of the window

    # Move the mouse to the position and click
    pyautogui.moveTo(left + x_offset, top + y_offset)
    pyautogui.click()
    print("Clicked on the 'link' button in Keyboard.")
    
    return keyboard_process  # Return the process object    

def update_biosemi_config(config_file_path):
    # Determine the base directory (where the script is located)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the dynamic path for the BioSemi configuration file (biosemi64.sfp)
    dynamic_sfp_path = os.path.join(base_dir, 'LabStreamingLayer', 'APPS', 'BioSemi', 'biosemi64.sfp')

    # Read the original config file
    with open(config_file_path, 'r') as file:
        config_lines = file.readlines()

    # Check if the path is already correct, if so, skip modification
    for i, line in enumerate(config_lines):
        if line.startswith('filename='):
            current_path = line.strip().split('=')[1]  # Extract the current filename value
            if current_path == dynamic_sfp_path:
                print(f"Filename path is already correct: {current_path}")
                return  # Exit the function, no need to overwrite the file
            else:
                # If not correct, modify the line
                config_lines[i] = f"filename={dynamic_sfp_path}\n"
                print(f"Updated filename path to: {dynamic_sfp_path}")
                break

    # Write the updated config back to the file only if necessary
    with open(config_file_path, 'w') as file:
        file.writelines(config_lines)
    print(f"Configuration file '{config_file_path}' updated successfully.")


# Function to launch BioSemi.exe and click the 'link' button
def launch_biosemi_and_click_link(exe_path):
    if os.path.exists(exe_path):
        try:
            # Construct the path to biosemi_config.cfg in the same directory as BioSemi.exe
            config_file_path = os.path.join(os.path.dirname(exe_path), 'biosemi_config.cfg')
            update_biosemi_config(config_file_path)
            config_path = os.path.join(os.path.dirname(exe_path), 'biosemi_config.cfg')

            # Check if the config file exists
            if not os.path.exists(config_path):
                print(f"Config file not found: {config_path}")
                return None

            # Launch the BioSemi.exe with the config file
            biosemi_process = subprocess.Popen([exe_path, '-c', config_path])
            print(f"Launched: {exe_path} with config {config_path}")
        except Exception as e:
            print(f"Failed to launch {exe_path}: {e}")
            return None
    else:
        print(f"File not found: {exe_path}")
        return None

    # Wait for the window to appear
    time.sleep(2)  # Adjust the sleep time as needed

    # Find the window titled 'BioSemi'
    windows = gw.getWindowsWithTitle('BioSemi')
    if not windows:
        print("BioSemi window not found.")
        return
    else:
        biosemi_window = windows[0]

    # Bring the window to the front
    biosemi_window.activate()
    time.sleep(0.5)  # Give time for the window to activate

    # Get window position
    left, top = biosemi_window.left, biosemi_window.top

    # Coordinates of the "link" button relative to the window
    x_offset = 300   # Horizontal offset from the top-left corner of the window
    y_offset = 280   # Vertical offset from the top-left corner of the window

    # Move the mouse to the position and click
    pyautogui.moveTo(left + x_offset, top + y_offset)
    pyautogui.click()
    print("Clicked on the 'link' button in BioSemi.")

    return biosemi_process  # Return the process object

def minimize_launched_windows():
    # List of window titles to minimize
    windows_to_minimize = ['Gazepoint Control', 'BioSemi', 'Keyboard', 'Lab Recorder']
    windows = gw.getAllWindows()
    for window in windows:
        # Check if the window title matches any of the applications we want to minimize
        if any(title in window.title for title in windows_to_minimize):
            window.minimize()
    print("Minimized launched applications.")

def close_launched_applications(processes):
    # First, try to terminate the processes
    for process in processes:
        if process and process.poll() is None:  # Check if process is still running
            try:
                process.terminate()
                print(f"Terminated process with PID {process.pid}")
            except Exception as e:
                print(f"Failed to terminate process with PID {process.pid}: {e}")

    # Now, close the application windows
    windows_to_close = ['LabRecorder', 'BioSemi', 'Keyboard', 'Gazepoint Control']
    windows = gw.getAllWindows()
    for window in windows:
        if any(title in window.title for title in windows_to_close):
            try:
                window.close()
                print(f"Closed window: {window.title}")
            except Exception as e:
                print(f"Failed to close window {window.title}: {e}")
    print("Closed launched applications.")

def get_local_streams():
    # Get all available streams
    streams_info = resolve_streams()
    # Get the current machine's hostname
    local_hostname = socket.gethostname()
    
    # Filter streams based on their hostname
    local_streams = [stream.name() for stream in streams_info if stream.hostname() == local_hostname]
    return local_streams

def show_missing_streams_gui(missing_streams, processes):
    # Create the main window
    root = tk.Tk()
    root.title("Missing Streams Detected")

    # Set window size and position
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2) - (window_width/2)
    y_coordinate = (screen_height/2) - (window_height/2)
    root.geometry(f"{int(window_width)}x{int(window_height)}+{int(x_coordinate)}+{int(y_coordinate)}")

    # Set the window to be always on top
    root.attributes('-topmost', True)
    root.lift()  # Bring window to the top
    root.focus_force()  # Focus on the window

    # Display the missing streams
    message = "The following streams are missing:\n\n" + "\n".join(missing_streams)
    label = tk.Label(root, text=message, padx=20, pady=20)
    label.pack()

    # Close button
    def on_close():
        # Close the launched applications
        close_launched_applications(processes)
        # Close the GUI window
        root.destroy()

    close_button = tk.Button(root, text="Close", command=on_close, padx=10, pady=5)
    close_button.pack(pady=(0, 20))

    # Start the Tkinter event loop
    root.mainloop()

def start_recording(participant_info):
    # Generate the BIDS-compliant file path
    save_filename = create_bids_path(participant_info)

    # List to keep track of process objects
    processes = []

    # Set LabRecorder to save the file with the correct path and info
    labrecorder_process = set_labrecorder_filename(labrecorder_path, save_filename, participant_info)
    if labrecorder_process:
        processes.append(labrecorder_process)

    # Launch Gazepoint Software
    gazepoint_process = launch_gazepoint()
    if gazepoint_process:
        processes.append(gazepoint_process)

    # Launch other required streams
    biosemi_process = launch_biosemi_and_click_link(biosemi_exe_path)
    if biosemi_process:
        processes.append(biosemi_process)

    keyboard_process = launch_keyboard_and_click_link(keyboard_exe_path)
    if keyboard_process:
        processes.append(keyboard_process)

    eye_tracking_process = launch_executable(eye_tracking_py_path, is_python_script=True)
    if eye_tracking_process:
        processes.append(eye_tracking_process)

    experimental_process = launch_executable(experimental_py_path, is_python_script=True)
    if experimental_process:
        processes.append(experimental_process)

    time.sleep(2)  # Wait for streams to initialize

    # Store processes in participant_info for access in other functions if needed
    participant_info['processes'] = processes

    # Get the list of available local streams
    local_streams = get_local_streams()
    print(f"Available local streams: {local_streams}")

    # Define expected local streams (these should be local streams only)
    expected_local_streams = ['BioSemi', 'Keyboard', 'GazepointEyeTracker', 'ExperimentMarkers']

    # Check if all expected streams are present
    missing_streams = [stream for stream in expected_local_streams if stream not in local_streams]
    if missing_streams:
        print(f"Error: The following local streams are missing: {missing_streams}")
        print("Recording will not start.") 
        show_missing_streams_gui(missing_streams, processes)  # Show GUI with missing streams
        return False  # Indicate that recording did not start
    else:
        # Update stream list in LabRecorder
        send_command_to_labrecorder('update\n')
        time.sleep(0.5)  # Give LabRecorder time to update the streams
        send_command_to_labrecorder('select all\n')  # Select all streams
        send_command_to_labrecorder('start\n')  # Start recording
        print("Recording started successfully.")
        minimize_launched_windows()  # Minimize all windows except LabRecorder
        return True  # Indicate that recording started successfully
    
if __name__ == '__main__':
    # Example participant_info dictionary
    participant_info = {
        'participant_id': '001',
        'participant_initials': 'AB',
        'participant_anonymized_id': '001',
        'date_session1': '2024-10-07',
        'date_session2': 'NA',
        'date_session3': 'NA',
        'language': 'English',
        'current_session': '1',
        'completed_tasks': ''
    }

    # Start recording
    start_recording(participant_info)
