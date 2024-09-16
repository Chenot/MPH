import os
import tkinter as tk
from psychopy import visual, core, session
from datetime import datetime
from utils import update_participant_info, create_bids_structure, copy_psychopy_data_to_bids, get_parent_directory
import webbrowser

# URL placeholders for questionnaires (Replace these with actual URLs)
# Session 1 URLs
url_demographics_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=CrPRB"
url_demographics_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=u44hj"
url_videogames_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=Jyv4p"
url_videogames_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=yL9pb"
url_sleep_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=Fh9fO"
url_sleep_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=97LST"
url_laterality_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=TD2kb"
url_laterality_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=zODGs"
url_presession_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=dbt78"
url_presession_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=CsxH2"

# Session 2 URLs
url_rationality_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=7Uxnwh"
url_rationality_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=ER3HF"
url_metacognition_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=PXfzb"
url_metacognition_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=tVpfd"
url_executivefunctions_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=sSMjm"
url_executivefunctions_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=taCZy"
url_selfesteem_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=jR8WZ"
url_selfesteem_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=FrgPf"

# Session 3 URLs
url_chronotype_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=uSgGw"
url_chronotype_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=A6V8e"
url_emotions1_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=32kBZ"
url_emotions1_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=zuEca"
url_emotions2_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=Rt3CC"
url_emotions2_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=WgpSS"
url_personality_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=JU3TJ"
url_personality_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=pu4pB"

# Supplementary Questionnaires URLs
url_personality1_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=gS9mT"
url_personality1_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=SjgbA"
url_personality2_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=Lt9b4"
url_personality2_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=JXTga"
url_quality_of_life_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=CMR7q"
url_quality_of_life_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=Vu7D5"
url_anxiety_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=UDPaj"
url_anxiety_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=3puxm"
url_depression_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=Qu7kJ"
url_depression_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=EVWWd"
# Path to the data folder created by PsychoPy
psychopy_data_dir = os.path.join(os.path.dirname(__file__), 'data')

# Path to the CSV file storing participant information
csv_file = os.path.join(os.path.dirname(__file__), 'Participants_expInfo.csv')


def open_url(url):
    """Opens the given URL in the default web browser."""
    webbrowser.open(url)


# --- GUI for launching the experiment ---
def launch_experiment_gui(participant_info):
    """Launches the GUI for starting the experiment tasks."""
    
    def start_experiment():
        root.destroy()  # Close the Tkinter window when "Start" is clicked
        current_session = participant_info['current_session']
        completed_tasks = participant_info.get('completed_tasks', [])  # Load completed tasks

        # Create the window for the experiment
        win = visual.Window(size=[1920, 1080], fullscr=True, screen=0, 
                            winType='pyglet', allowGUI=True, allowStencil=False,
                            monitor='testMonitor', color='grey', colorSpace='rgb',
                            blendMode='avg', useFBO=True)

        # Choose experiments based on the session
        if current_session == '1':
            tasks = {
                'SimpleRTT': "Speed_SimpleRTT/simpleRTT_lastrun.py",
                'SimpleRTTmouse': "Speed_SimpleRTT_mouse/simpleRTT_mouse_lastrun.py",
                'DoubleRTT': "Speed_DoubleRTT/DoubleRTT_lastrun.py", 
            }
        elif current_session == '2':
            tasks = {
                'RS': "Resting_state/Resting_state_lastrun.py",
                'Antisaccade': "Inhibition_Antisaccade/Antisaccade_lastrun.py", 
                'KeepTrack': "Upadting_KeepTrack/KeepTrack_lastrun.py",      
            }
        elif current_session == '3':
            tasks = {
                'RS': "Resting_state/Resting_state_lastrun.py",
                'TOH': "Planning_TowerOfHanoi/TowerOfHanoi_lastrun.py", 
                'RAPM': "Reasoning_RavenMatrices/RAPM_lastrun.py",      
            }

        # Run the session and skip completed tasks
        run_session(win, participant_info, tasks, completed_tasks)

        # Once the session is completed, move data to the BIDS-compliant folder
        root_path = get_parent_directory(os.path.dirname(__file__))  # Get the parent directory
        bids_folder = create_bids_structure(root_path, participant_info['participant_id'], current_session)
        copy_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_info['participant_id'], current_session)

        # Close the window and quit
        win.close()
        core.quit()

    def run_session(win, participant_info, tasks, completed_tasks):
        # Ensure completed_tasks is a list before appending tasks
        if isinstance(completed_tasks, str):
            completed_tasks = completed_tasks.split(',') if completed_tasks else []
        for task, script in tasks.items():
            if task in completed_tasks:
                print(f"Skipping completed task: {task}")
                continue  # Skip completed tasks

            print(f"Running task: {task}")
            
            try:
                thisSession = session.Session(
                    win=win,
                    root=os.path.dirname(__file__),
                    experiments={task: script}
                )
                thisSession.runExperiment(task, expInfo={
                    'participant': participant_info['participant_id'], 
                    'session': participant_info['current_session'], 
                    'language': participant_info['language'], 
                    'date': datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                })
                
                # Mark task as completed and update participant_info
                completed_tasks.append(task)
                participant_info['completed_tasks'] = completed_tasks
                update_participant_info(csv_file, participant_info)

            except Exception as e:
                print(f"Error while running task {task}: {e}")
                break  # Stop if there's an error, and allow resuming later

        # Update session date and session number
        session_key = f"date_session{participant_info['current_session']}"
        participant_info[session_key] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        participant_info['current_session'] = str(int(participant_info['current_session']) + 1)

        # Final update of participant info
        update_participant_info(csv_file, participant_info)

    # Create the main Tkinter window for experiment launch
    root = tk.Tk()
    root.title("Launch Experiment")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Display participant info and session
    tk.Label(main_frame, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(main_frame, text=f"Participant Initials: {participant_info['participant_initials']}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(main_frame, text=f"Current Session: {participant_info['current_session']}", font=("Helvetica", 16)).pack(pady=10)

    # Start button
    tk.Button(main_frame, text="Start", command=start_experiment, font=("Helvetica", 16)).pack(pady=10)

    root.mainloop()


# --- GUI for selecting questionnaires based on session ---
def launch_questionnaire_gui(participant_info):
    """Launches the GUI for selecting and opening questionnaires based on the session and language."""
    
    # Get the current session and language
    current_session = participant_info['current_session']
    language = participant_info['language']

    # Define the URLs for the questionnaires based on session and language
    if current_session == '1':
        urls = {
            'Demographics': url_demographics_french if language == 'French' else url_demographics_english,
            'Video Games': url_videogames_french if language == 'French' else url_videogames_english,
            'Sleep': url_sleep_french if language == 'French' else url_sleep_english,
            'Laterality': url_laterality_french if language == 'French' else url_laterality_english,
            'Pre-session': url_presession_french if language == 'French' else url_presession_english
        }
    elif current_session == '2':
        urls = {
            'Rationalité': url_rationality_french if language == 'French' else url_rationality_english,
            'Metacognition': url_metacognition_french if language == 'French' else url_metacognition_english,
            'Executive Functions': url_executivefunctions_french if language == 'French' else url_executivefunctions_english,
            'Self-esteem': url_selfesteem_french if language == 'French' else url_selfesteem_english,
            'Pre-session': url_presession_french if language == 'French' else url_presession_english
        }
    elif current_session == '3':
        urls = {
            'Chronotype': url_chronotype_french if language == 'French' else url_chronotype_english,
            'Emotions (1)': url_emotions1_french if language == 'French' else url_emotions1_english,
            'Emotions (2)': url_emotions2_french if language == 'French' else url_emotions2_english,
            'Personality': url_personality_french if language == 'French' else url_personality_english,
            'Pre-session': url_presession_french if language == 'French' else url_presession_english
        }

    # Create the Tkinter window
    root = tk.Tk()
    root.title(f"Questionnaires for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    # Create a label to display the participant ID
    label_id = tk.Label(root, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16))
    label_id.pack(pady=10)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)

    # Create a button for each questionnaire
    for title, url in urls.items():
        tk.Button(button_frame, text=title, font=("Helvetica", 14), command=lambda url=url: open_url(url)).pack(padx=20, pady=10)

    # Back button to return to the main GUI
    button_back = tk.Button(root, text="Back", font=("Helvetica", 16), command=lambda: [root.destroy(), launch_main_gui(participant_info)])
    button_back.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()

# --- GUI for selecting supplementary questionnaires ---
def launch_supplementary_questionnaire_gui(participant_info):
    """Launches the GUI for selecting supplementary questionnaires based on the language."""

    # Get the participant language
    language = participant_info['language']

    # Define the URLs for the supplementary questionnaires
    urls = {
        'Personnalité (1)': url_personality1_french if language == 'French' else url_personality1_english,
        'Personnalité (2)': url_personality2_french if language == 'French' else url_personality2_english,
        'Qualité de vie': url_quality_of_life_french if language == 'French' else url_quality_of_life_english,
        'Anxiété': url_anxiety_french if language == 'French' else url_anxiety_english,
        'Dépression': url_depression_french if language == 'French' else url_depression_english
    }

    # Create the Tkinter window
    root = tk.Tk()
    root.title(f"Supplementary Questionnaires for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    # Create a label to display the participant ID
    label_id = tk.Label(root, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16))
    label_id.pack(pady=10)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)

    # Create a button for each supplementary questionnaire
    for title, url in urls.items():
        tk.Button(button_frame, text=title, font=("Helvetica", 14), command=lambda url=url: open_url(url)).pack(padx=20, pady=10)

    # Back button to return to the main GUI
    button_back = tk.Button(root, text="Back", font=("Helvetica", 16), command=lambda: [root.destroy(), launch_main_gui(participant_info)])
    button_back.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()
    
# --- Main GUI ---
def launch_main_gui(participant_info):
    """Main GUI with options for 'Questionnaires', 'Tasks', and 'Supplementary Questionnaires'."""
    
    root = tk.Tk()
    root.title(f"Main Menu for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    # Create a label to display the participant ID
    label_id = tk.Label(root, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16))
    label_id.pack(pady=10)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)

    # Button for Questionnaires
    button_questionnaires = tk.Button(button_frame, text="Questionnaires", font=("Helvetica", 14), command=lambda: [root.destroy(), launch_questionnaire_gui(participant_info)])
    button_questionnaires.grid(row=0, column=0, padx=20, pady=20)

    # Button for Tasks
    button_tasks = tk.Button(button_frame, text="Tasks", font=("Helvetica", 14), command=lambda: [root.destroy(), launch_experiment_gui(participant_info)])
    button_tasks.grid(row=0, column=1, padx=20, pady=20)

    # Button for Supplementary Questionnaires
    button_supplementary = tk.Button(button_frame, text="Supplementary Questionnaires", font=("Helvetica", 14), command=lambda: [root.destroy(), launch_supplementary_questionnaire_gui(participant_info)])
    button_supplementary.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    # Run the Tkinter event loop
    root.mainloop()
