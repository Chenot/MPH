import os
import tkinter as tk
from psychopy import visual, core, session
from datetime import datetime
from utils import update_participant_info, create_bids_structure, copy_psychopy_data_to_bids, get_parent_directory
import webbrowser

# URL placeholders (Replace these with actual URLs)
url_demographics_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=CrPRB"
url_demographics_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=u44hj"
url_presession_english = "https://www.psytoolkit.org/c/3.4.0/survey?s=dbt78"
url_presession_french = "https://www.psytoolkit.org/c/3.4.0/survey?s=CsxH2"

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


# --- GUI for selecting questionnaires ---
def launch_questionnaire_gui(participant_info):
    """Launches the GUI for selecting and opening questionnaires based on participant language."""
    
    # Define the URLs for the participant based on language
    if participant_info['language'] == 'French':
        url_demographics = url_demographics_french
        url_presession = url_presession_french
    else:
        url_demographics = url_demographics_english
        url_presession = url_presession_english

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

    # Button for Demographics questionnaire
    button_demographics = tk.Button(button_frame, text="Demographics", font=("Helvetica", 14), command=lambda: open_url(url_demographics))
    button_demographics.grid(row=0, column=0, padx=20, pady=20)

    # Button for Pre-session questionnaire
    button_presession = tk.Button(button_frame, text="Pre-session", font=("Helvetica", 14), command=lambda: open_url(url_presession))
    button_presession.grid(row=0, column=1, padx=20, pady=20)

    # Back button to return to the main GUI
    button_back = tk.Button(root, text="Back", font=("Helvetica", 16), command=lambda: [root.destroy(), launch_main_gui(participant_info)])
    button_back.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()


# --- Main GUI ---
def launch_main_gui(participant_info):
    """Main GUI with options for 'Questionnaires' and 'Tasks'."""
    
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

    # Run the Tkinter event loop
    root.mainloop()
