import pygame
import time
import os
import socket
import json
import threading
import sys
from pylsl import local_clock

# Class to run the Resting-State task
class RestingState:
    def __init__(self, participant_info):
        pygame.init()
        self.clock = pygame.time.Clock()


        # Extract participant information
        self.language = participant_info.get('language', 'English')

        # Set up full screen and gray background like PsychoPy
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Resting-State Task")
        pygame.mouse.set_visible(False)  # Disable mouse
        self.GRAY = (128, 128, 128)  # Adjusted PsychoPy default gray

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Load the appropriate language for instructions
        self.load_instructions()

        # Set up audio
        pygame.mixer.init()
        self.load_audio_files()

        # Task states
        self.task_running = False
        self.instructions_shown = True

        # Number of cycles eyes open / eyes closed & duration per cycle
        self.ncycle = 5
        self.durationcycle = 30  # in seconds (for eyes open or closed)

    # Function to load the correct instructions based on language
    def load_instructions(self):
        if self.language == "English":
            self.instructions = {
                'name_task': 'RESTING-STATE',
                'Text_instructions': (
                    "Welcome to the Resting-State\n\n\n"
                    "During this, you will alternate between eyes open and eyes closed during 5 minutes.\nA voice will tell you when to switch.\n"
                    "When your eyes are open, please fix your gaze on the cross in the center.\n\n"
                    "Try to relax, refrain from moving, and let your mind wander while staying awake.\n\n\n"
                    "Press the spacebar to start."
                ),
                'Text_end_task': "The task is now over.\n\nThank you!\n\nPress the spacebar to continue."
            }
            self.text_eyes_closed = "Close your eyes"
        else:
            self.instructions = {
                'name_task': 'RESTING-STATE',
                'Text_instructions': (
                    "Bienvenue dans la tâche de Resting-State\n\n\n"
                    "Vous allez devoir alterner entre yeux ouverts et yeux fermés pendant 5 minutes.\nUne voix vous indiquera quand changer.\n"
                    "Lorsque vos yeux sont ouverts, fixez votre regard sur la croix au centre.\n\n"
                    "Essayez de vous détendre, de ne pas bouger et de laisser libre cours à vos pensées "
                    "tout en restant éveillé.\n\n\n"
                    "Appuyez sur la barre d'espace pour commencer."
                ),
                'Text_end_task': "La tâche est terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer."
            }
            self.text_eyes_closed = "Fermez les yeux"

    # Function to load the audio files using pygame.mixer
    def load_audio_files(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if self.language == "English":
            suffix = '_eng.wav'
        else:
            suffix = '_fr.wav'
        self.audio_eyes_open = os.path.join(script_dir, 'ressources', 'EO' + suffix)
        self.audio_eyes_closed = os.path.join(script_dir, 'ressources', 'EC' + suffix)

    # LSL marker sending function
    def send_marker(self, marker):
        event = {'marker': marker, 'timestamp': local_clock()}
        message = json.dumps(event)

        def send():
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.settimeout(0.1)
                client_socket.connect(('localhost', 5000))
                client_socket.sendall(message.encode('utf-8'))
                client_socket.close()
            except (ConnectionRefusedError, socket.timeout):
                print("LSL server is not running or connection timed out. Continuing without sending marker.")

        send_thread = threading.Thread(target=send)
        send_thread.start()

    # Function to display text with manual line breaks
    def draw_multiline_text(self, text, font_size=50, line_spacing=10):
        font = pygame.font.Font(None, font_size)
        lines = text.splitlines()  # Split text by lines
        rendered_lines = []
        total_height = 0
        for line in lines:
            rendered_text = font.render(line, True, self.WHITE)
            rendered_lines.append(rendered_text)
            total_height += rendered_text.get_height() + line_spacing
        total_height -= line_spacing  # Remove extra spacing after last line

        screen_width, screen_height = self.screen.get_size()
        y_offset = (screen_height - total_height) // 2

        self.screen.fill(self.GRAY)  # Set the screen background to grey

        for rendered_text in rendered_lines:
            text_rect = rendered_text.get_rect(center=(screen_width // 2, y_offset + rendered_text.get_height() // 2))
            self.screen.blit(rendered_text, text_rect)
            y_offset += rendered_text.get_height() + line_spacing

        pygame.display.flip()

    # Function to draw a centered cross
    def draw_centered_cross(self, font_size=72):
        font = pygame.font.Font(None, font_size)
        cross_text = font.render('+', True, self.WHITE)
        text_rect = cross_text.get_rect(center=self.screen.get_rect().center)
        self.screen.fill(self.GRAY)
        self.screen.blit(cross_text, text_rect)
        pygame.display.flip()

    # Function to play sound using pygame.mixer
    def play_audio(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    # Main task loop function
    def run_task(self):
        self.task_running = True
        for cycle in range(self.ncycle):
            # Eyes open phase
            self.run_phase('Eyes Open', self.audio_eyes_open, '+')
    
            # Eyes closed phase
            self.run_phase('Eyes Closed', self.audio_eyes_closed, self.text_eyes_closed)
    
        # At the end of the last cycle, play the "eyes open" audio to ensure participants open their eyes
        self.play_audio(self.audio_eyes_open)
    
        # End of task
        self.send_marker('Task Ended')
        self.task_running = False
        self.draw_multiline_text(self.instructions['Text_end_task'], font_size=50)


    # Function to run a phase (eyes open/eyes closed)
    def run_phase(self, phase_name, audio_file, display_text):
        phase_duration = self.durationcycle  # The actual duration of the phase
        total_duration = 2 + phase_duration  # 2 seconds for marker + phase duration
    
        # Start the phase and display the initial text
        self.play_audio(audio_file)
        if phase_name == 'Eyes Open' and display_text == '+':
            self.draw_centered_cross(font_size=144)
        else:
            self.draw_multiline_text(display_text, font_size=72)
    
        start_ticks = pygame.time.get_ticks()
        marker_sent = False  # To ensure marker is sent only once at t=2
        running_phase = True
        while running_phase:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # Convert to seconds
            if not marker_sent and elapsed_time >= 2:
                # Send the marker at 2 seconds (only once)
                self.send_marker(f'{phase_name} Marker at 2 seconds')
                marker_sent = True
            if elapsed_time >= total_duration:
                running_phase = False
    
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            # Update display
            pygame.display.flip()
            # Control the frame rate
            self.clock.tick(60)  # Limit to 60 frames per second


    # Function to start the task
    def start(self):
        # Combine the task name with the instructions
        full_instructions = self.instructions['name_task'] + '\n\n\n\n\n' + self.instructions['Text_instructions']
        self.draw_multiline_text(full_instructions, font_size=45)
    
        # Main event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.instructions_shown:
                            self.instructions_shown = False
                            self.run_task()
                        elif not self.task_running:
                            running = False
                            break
            pygame.display.flip()
            self.clock.tick(60)  # Limit to 60 frames per second
        # After the loop ends, clean up and return
        pygame.quit()
        return


# Function to run the resting-state task
def run_RS(participant_info):
    task = RestingState(participant_info)
    task.start()

if __name__ == "__main__":
    participant_info = {
        'participant_id': '001',
        'participant_initials': 'JD',
        'participant_anonymized_id': 'X123',
        'language': 'French',
        'current_session': '1',
    }

    run_RS(participant_info)
