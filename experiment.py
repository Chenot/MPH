import os
import sys
import tkinter as tk
from psychopy import visual, core, session
from datetime import datetime
from utils import update_participant_info, create_bids_structure, copy_psychopy_data_to_bids, get_parent_directory, send_command_to_labrecorder, launch_lsl_metascript
import webbrowser

# Adjust the path to import MPH_MATB.py
current_directory = os.path.dirname(os.path.abspath(__file__))
matb_directory = os.path.join(current_directory, 'Complex_OpenMATB')
sys.path.append(matb_directory)
from MPH_MATB import run_matb_task

# Adjust the path to import questionnaire_post_task.py
script_dir = os.path.dirname(os.path.abspath(__file__))
psychopytasks_directory = os.path.abspath(os.path.join(script_dir, 'Questionnaires'))
sys.path.append(psychopytasks_directory)
from questionnaire_post_task import QuestionnaireApp


# URLs for questionnaires (Replace these with actual URLs)
# Session 1 URLs
url_demographics_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=CrPRB"
url_demographics_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=u44hj"
url_BIG5_personality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=JU3TJ"
url_BIG5_personality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=pu4pB"
url_SCI_sleep_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Fh9fO"
url_SCI_sleep_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=97LST"
url_EHI_laterality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=TD2kb"
url_EHI_laterality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=zODGs"
url_presession_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=dbt78"
url_presession_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=CsxH2"

# Session 2 URLs
url_REI_rationality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=7Uxnwh"
url_REI_rationality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=ER3HF"
url_MAI_metacognition_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=PXfzb"
url_MAI_metacognition_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=tVpfd"
url_VGxp_videogames_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Jyv4p"
url_VGxp_videogames_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=yL9pb"
url_RSES_selfesteem_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=jR8WZ"
url_RSES_selfesteem_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=FrgPf"
url_presession_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=dbt78"
url_presession_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=CsxH2"

# Session 3 URLs
url_RMEQ_chronotype_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=uSgGw"
url_RMEQ_chronotype_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=A6V8e"
url_TEIQ_emotions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=32kBZ"
url_TEIQ_emotions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=zuEca"
url_SSEIT_emotions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Rt3CC"
url_SSEIT_emotions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=WgpSS"
url_BRIEF_executivefunctions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=sSMjm"
url_BRIEF_executivefunctions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=taCZy"
url_presession_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=dbt78"
url_presession_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=CsxH2"

# Supplementary Questionnaires URLs
url_MBTI_personality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=gS9mT"
url_MBTI_personality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=SjgbA"
url_PID_personality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Lt9b4"
url_PID_personality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=JXTga"
url_QOL_quality_of_life_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=CMR7q"
url_QOL_quality_of_life_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=Vu7D5"
url_STAI_anxiety_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=UDPaj"
url_STAI_anxiety_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=3puxm"
url_BDI_depression_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Qu7kJ"
url_BDI_depression_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=EVWWd"

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

    def launch_questionnaire(participant_info, completed_complex_task):
        # Directly instantiate the QuestionnaireApp class and pass completed_complex_task
        root = tk.Tk()
        QuestionnaireApp(root, participant_info, completed_complex_task)
        root.mainloop()

    
    def run_session(win, participant_info, tasks, completed_tasks):
        # Ensure completed_tasks is a list before appending tasks
        if isinstance(completed_tasks, str):
            completed_tasks = completed_tasks.split(',') if completed_tasks else []
    
        # Run PsychoPy tasks
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
                participant_info['completed_tasks'] = ','.join(completed_tasks)  # Ensure it's saved as a string
                update_participant_info(csv_file, participant_info)
    
            except Exception as e:
                print(f"Error while running task {task}: {e}")
                break  # Stop if there's an error, and allow resuming later
    
        # Close the PsychoPy window after all tasks have been run
        win.close() 
    
        # Define the 4 MATB scenarios based on the current session, but use meaningful labels
        matb_scenarios = {
            'MATB_easy': f"session-{participant_info['current_session']}_easy.txt",
            'MATB_hard': f"session-{participant_info['current_session']}_hard.txt",
            'MATB_easy_oddball': f"session-{participant_info['current_session']}_easy_oddball.txt",
            'MATB_hard_oddball': f"session-{participant_info['current_session']}_hard_oddball.txt"
        }
    
        # Run MATB scenarios (track completed scenarios using meaningful labels)
        for label, scenario in matb_scenarios.items():
            if label in completed_tasks:
                print(f"Skipping completed MATB scenario: {label}")
                continue  # Skip completed MATB scenarios
    
            print(f"Running MATB scenario: {label}")
            try:
                # Run the MATB task
                run_matb_task(participant_info, scenario)
    
                # Mark the MATB scenario as completed and update participant_info
                completed_tasks.append(label)
                participant_info['completed_tasks'] = ','.join(completed_tasks)  # Save as a comma-separated string
                update_participant_info(csv_file, participant_info)
                
                # Launch the questionnaire
                launch_questionnaire(participant_info, label)

            except Exception as e:
                print(f"Error while running MATB scenario {label}: {e}")
                break  # Stop if there's an error, and allow resuming later
    
        # Update session date and session number
        session_key = f"date_session{participant_info['current_session']}"
        participant_info[session_key] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        participant_info['current_session'] = str(int(participant_info['current_session']) + 1)

        # Final update of participant info
        update_participant_info(csv_file, participant_info)
        
        # Stop Lab Recorder
        send_command_to_labrecorder('stop\n')
        print("Session completed.")
        
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
            'Personality (BIG-5)': url_BIG5_personality_french if language == 'French' else url_BIG5_personality_english,
            'Sleep Quality (SCI)': url_SCI_sleep_french if language == 'French' else url_SCI_sleep_english,
            'Handedness (EHI)': url_EHI_laterality_french if language == 'French' else url_EHI_laterality_english,
            'Pre-session': url_presession_french if language == 'French' else url_presession_english
        }
    elif current_session == '2':
        urls = {
            'Rationality (REI)': url_REI_rationality_french if language == 'French' else url_REI_rationality_english,
            'Meta-cognition (MAI)': url_MAI_metacognition_french if language == 'French' else url_MAI_metacognition_english,
            'Video Game Experience (VGxp)': url_VGxp_videogames_french if language == 'French' else url_VGxp_videogames_english,
            'Self-esteem (RSES)': url_RSES_selfesteem_french if language == 'French' else url_RSES_selfesteem_english,
            'Pre-session': url_presession_french if language == 'French' else url_presession_english
        }
    elif current_session == '3':
        urls = {
            'Chronotype (rMEQ)': url_RMEQ_chronotype_french if language == 'French' else url_RMEQ_chronotype_english,
            'Emotions (TEIQ)': url_TEIQ_emotions_french if language == 'French' else url_TEIQ_emotions_english,
            'Emotions (SSEIT)': url_SSEIT_emotions_french if language == 'French' else url_SSEIT_emotions_english,
            'Executive Functions (BRIEF)': url_BRIEF_executivefunctions_french if language == 'French' else url_BRIEF_executivefunctions_english
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
        'Personality (MBTI)': url_MBTI_personality_french if language == 'French' else url_MBTI_personality_english,
        'Personality (PID)': url_PID_personality_french if language == 'French' else url_PID_personality_english,
        'Quality of Life': url_QOL_quality_of_life_french if language == 'French' else url_QOL_quality_of_life_english,
        'Anxiety (STAI)': url_STAI_anxiety_french if language == 'French' else url_STAI_anxiety_english,
        'Depression (BDI)': url_BDI_depression_french if language == 'French' else url_BDI_depression_english
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
    """Main GUI with options for 'Questionnaires', 'Start Recording', 'Tasks', 'Supplementary Questionnaires', and other buttons."""

    root = tk.Tk()
    root.title(f"Main Menu for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    # Create a label to display the participant ID
    label_id = tk.Label(root, text=f"Participant ID: P{participant_info['participant_id']}", font=("Helvetica", 20))
    label_id.pack(pady=10)

    # Create a label to display the current session
    label_session = tk.Label(root, text=f"Session: {participant_info['current_session']}", font=("Helvetica", 18))
    label_session.pack(pady=10)

    # Middle frame for the main buttons (centered and larger)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=100)  # Increase the padding to center the buttons vertically

    # Button styling options with larger size
    button_options = {"font": ("Helvetica", 20), "width": 30, "height": 2}

    # Button for Questionnaires
    button_questionnaires = tk.Button(button_frame, text="Questionnaires", **button_options, command=lambda: [root.destroy(), launch_questionnaire_gui(participant_info)])
    button_questionnaires.grid(row=0, column=0, padx=20, pady=20)

    # Button for Start Recording (Launch LSL Metascript)
    button_start_recording = tk.Button(button_frame, text="Start Recording", **button_options, command=lambda: launch_lsl_metascript(participant_info))
    button_start_recording.grid(row=1, column=0, padx=20, pady=20)

    # Button for Tasks (Initially disabled)
    button_tasks = tk.Button(button_frame, text="Start Tasks", **button_options,  command=lambda: [root.destroy(), launch_experiment_gui(participant_info)])
    button_tasks.grid(row=2, column=0, padx=20, pady=20)

    # Button for Supplementary Questionnaires
    button_supplementary = tk.Button(button_frame, text="Supplementary Questionnaires", **button_options, command=lambda: [root.destroy(), launch_supplementary_questionnaire_gui(participant_info)])
    button_supplementary.grid(row=3, column=0, padx=20, pady=20)

    # Bottom frame for the "Back" and "Finish Session" buttons
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, pady=20)

    # 'Back' button to return to the main GUI in main.py
    button_back = tk.Button(bottom_frame, text="Back", font=("Helvetica", 16), width=20, height=2, command=lambda: go_back_to_main_gui(root))
    button_back.grid(row=0, column=0, padx=10)

    # 'Finish Session' button to close the Tkinter window
    button_finish = tk.Button(bottom_frame, text="Finish Session", font=("Helvetica", 16), width=20, height=2, command=root.destroy)
    button_finish.grid(row=0, column=1, padx=10)

    root.mainloop()


def go_back_to_main_gui(root):
    """Handles the back button to return to the main GUI in main.py."""
    root.destroy()  # Close the current window
    from main import create_main_gui  # Import the main GUI function
    create_main_gui()  # Launch the main GUI




