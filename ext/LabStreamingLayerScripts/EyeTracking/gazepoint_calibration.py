import pygame
import sys
import socket
import pyautogui
import xml.etree.ElementTree as ET

# Function to display a generic start screen
def display_start_screen(title_text, instruction_text, background_color=(0, 0, 0), font_color=(255, 255, 255)):
    pygame.init()
    
    # Set up the display in full screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Get the screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set background color (black by default)
    screen.fill(background_color)
    
    # Set fonts, adjusting the font size dynamically based on screen height
    font_large = pygame.font.Font(None, int(screen_height * 0.06))  # 6% of the screen height
    font_small = pygame.font.Font(None, int(screen_height * 0.05))  # 5% of the screen height
    
    # Render the title and instruction texts
    text_large = font_large.render(title_text, True, font_color)
    text_small = font_small.render(instruction_text, True, font_color)

    # Get text rectangles and center them
    text_large_rect = text_large.get_rect(center=(screen_width // 2, screen_height // 3))
    text_small_rect = text_small.get_rect(center=(screen_width // 2, screen_height // 2))
    
    # Draw text to the screen
    screen.blit(text_large, text_large_rect)
    screen.blit(text_small, text_small_rect)
    
    # Update the display
    pygame.display.flip()
    
    return screen

# Function to wait for key press (spacebar to continue, or 'C' to retry)
def wait_for_key_press():
    waiting = True
    retry = False
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    retry = False
                elif event.key == pygame.K_c:
                    waiting = False
                    retry = True
    return retry

# Function to handle text based on the participant's language
def get_text_for_task(task, language):
    if language == 'French':
        texts = {
            'EyeTracking': ('Calibration oculométrique : fixez votre regard sur les points', 'Appuyez sur la barre espace pour démarrer'),
            'CalibrationResults': ('Calibration', 'Appuyez sur espace pour continuer ou sur C pour recommencer')
        }
    else:  # Default to English
        texts = {
            'EyeTracking': ('Eye-tracking calibration: focus your gaze on the points', 'Press spacebar to start'),
            'CalibrationResults': ('Calibration', 'Press spacebar to continue or C to retry')
        } 
    return texts[task]

# Function to start socket-based calibration
def start_calibration():
    HOST = '127.0.0.1'  # Localhost
    PORT = 4242         # Default Gazepoint port
    
    # Move the mouse to the bottom-right corner (e.g., 1 pixel away from the corner)
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width - 1, screen_height - 1)
    
    try:
        # Establish a persistent connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            # Enable calibration display
            s.sendall('<SET ID="CALIBRATE_SHOW" STATE="1" />\r\n'.encode('utf-8'))

            # Start calibration
            s.sendall('<SET ID="CALIBRATE_START" STATE="1" />\r\n'.encode('utf-8'))

            # Listen for calibration messages
            calibration_result_received = False
            buffer = ''
            rv_sum = 0  # Initialize sum of RV values
            while not calibration_result_received:
                # Receive data from the server
                data = s.recv(4096).decode('utf-8')
                if not data:
                    break  # Connection closed
                buffer += data

                # Split buffer into messages
                messages = buffer.split('\r\n')
                buffer = messages.pop()  # Keep incomplete message

                for message in messages:
                    message = message.strip()
                    if message:
                        try:
                            # Parse the XML message
                            root = ET.fromstring(message)
                            # Check if it's a calibration result
                            if root.tag == 'CAL' and root.attrib.get('ID') == 'CALIB_RESULT':
                                # Extract RV values
                                point = 1
                                while True:
                                    rv_key = f'RV{point}'
                                    if rv_key in root.attrib:
                                        rv = int(root.attrib[rv_key])
                                        rv_sum += rv  # Sum the RV values
                                        point += 1
                                    else:
                                        break
                                calibration_result_received = True
                                break
                        except ET.ParseError:
                            continue

            # Disable calibration display after completion
            s.sendall('<SET ID="CALIBRATE_SHOW" STATE="0" />\r\n'.encode('utf-8'))

            # Return the sum of RV values
            return rv_sum

    except ConnectionRefusedError:
        return None

# Function to show calibration results and handle retry
def display_calibration_results(rv_sum, language):
    title = f"Calibration: {rv_sum}/5"
    instruction = get_text_for_task('CalibrationResults', language)[1]
    
    # Display the result screen (black background, white text)
    display_start_screen(title, instruction, background_color=(0, 0, 0), font_color=(255, 255, 255))

    # Wait for spacebar or "C" press
    retry = wait_for_key_press()

    return retry

# Main function for running the full process
def run_ET_calibration(participant_info):
    language = participant_info.get('language', 'English')
        
    # Display eye tracking start screen
    title, instruction = get_text_for_task('EyeTracking', language)
    display_start_screen(title, instruction, background_color=(0, 0, 0), font_color=(255, 255, 255))

    # Wait for spacebar press to start calibration
    wait_for_key_press()

    # Loop for calibration with retry logic
    while True:
        # Eye-tracking calibration via socket communication
        rv_total = start_calibration()

        if rv_total is not None:
            # Display the calibration result and decide if the user wants to retry
            retry = display_calibration_results(rv_total, language)
            if retry:
                continue  # Retry the calibration
            else:
                break  # Exit after spacebar is pressed

    pygame.quit()  # Ensure pygame quits cleanly

if __name__ == "__main__":
    # Example participant info and scenario (you can change or pass these dynamically)
    participant_info = {
        'participant_id': '002',  # You can prompt the user or dynamically set this
        'participant_initials': 'JD',
        'current_session': '1',
        'completed_tasks': 'MATB',
        'language': 'French'
    }

    # Run the ET calibration
    run_ET_calibration(participant_info)
