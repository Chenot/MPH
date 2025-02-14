import csv
import time
import winsound
import socket
import json
import threading
import os
from pylsl import local_clock

# Get the current directory of the oddball_task.py script
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'oddball_task.csv')

# Function to send markers to the LSL server
def send_marker(marker):
    """Send a marker to the LSL server."""
    event = {
        'marker': marker,
        'timestamp': local_clock()
    }
    message = json.dumps(event)
    
    def send():
        try:
            # Connect to the socket server and send the marker with a timeout
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(0.1)  # Set timeout to 100 milliseconds
            client_socket.connect(('localhost', 5000))  # Connect to the LSL server
            client_socket.sendall(message.encode('utf-8'))  # Send marker data
            client_socket.close()
        except (ConnectionRefusedError, socket.timeout):
            print("LSL server is not running or connection timed out. Continuing without sending marker.")
    
    # Create and start a thread to send the marker asynchronously
    send_thread = threading.Thread(target=send)
    send_thread.start()

# Function to play a .wav file
def play_wav(file_path):
    """Plays a .wav file."""
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

# Load the CSV file with the task data using the absolute path
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    sound_data = list(reader)

# Simulate playing the sounds according to the timeline
def start_oddball():
    start_time = time.time()
    for row in sound_data:
        current_time = time.time()
        target_time = float(row['time'])
        delay = target_time - (current_time - start_time)
    
        if delay > 0:
            time.sleep(delay)  # Wait until the correct time to play the sound
    
        # Construct the file path based on the sound type ('low' or 'high')
        sound_file = os.path.join(current_directory, f"ressources/{row['sound']}.wav")
        
        # Play the .wav file
        play_wav(sound_file)
    
        # Send LSL marker for the sound
        marker = "Oddball_" + row['sound']
        send_marker(marker)
    
        # Print for logging purposes (optional)
        # print(f"Time: {target_time:.2f}s, Sound: {row['sound']}, File: {sound_file}")
    
    # print("Task completed!")

if __name__ == "__main__":
    start_oddball()
