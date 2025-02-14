import socket
import time

def send_command(command):
    HOST = '127.0.0.1'  # Localhost
    PORT = 4242         # Default Gazepoint port
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall((command + '\r\n').encode('utf-8'))
            data = s.recv(1024)
            return data.decode('utf-8')
    except ConnectionRefusedError:
        print("Could not connect to Gazepoint Control. Please ensure it's running.")
        return None

def start_calibration():
    # Enable calibration display
    response_show = send_command('<SET ID="CALIBRATE_SHOW" STATE="1" />')
    if response_show:
        print('Calibration display enabled:', response_show)
    else:
        print('Failed to enable calibration display.')
        return

    # Start calibration
    response_start = send_command('<SET ID="CALIBRATE_START" STATE="1" />')
    if response_start:
        print('Calibration started:', response_start)
        # Wait for calibration to finish
        # You can also check for a calibration completion event if available
        time.sleep(10)  # Adjust this delay based on your calibration duration
        print('Calibration completed.')
        # Disable calibration display after completion
        response_hide = send_command('<SET ID="CALIBRATE_SHOW" STATE="0" />')
        if response_hide:
            print('Calibration display hidden:', response_hide)
    else:
        print('Failed to start calibration.')

if __name__ == "__main__":
    # Ensure Gazepoint Control is running
    start_calibration()
