import os
import sys
import tkinter as tk
from psychopy import visual, core, session
from datetime import datetime
from utils import update_participant_info, create_bids_structure, copy_psychopy_data_to_bids, get_parent_directory, minimize_all_windows, send_command_to_labrecorder, launch_lsl_metascript, run_EyeTracking_Calibration, close_applications
import webbrowser

# Adjust the path to import MATB, questionnaires, resting-state
script_dir = os.path.dirname(os.path.abspath(__file__))
matb_directory = os.path.join(script_dir, 'Complex_OpenMATB')
questionnaire_directory = os.path.abspath(os.path.join(script_dir, 'Questionnaires'))
RS_directory = os.path.abspath(os.path.join(script_dir, 'Resting_state'))

sys.path.append(matb_directory)
sys.path.append(questionnaire_directory)
sys.path.append(RS_directory)

from MPH_MATB import run_matb_task
from MPH_MATB_training import MATB_training
from MPH_MATB_instructions import MATB_instructions
from questionnaire_post_task import QuestionnaireApp
from questionnaire_ARSQ import ARSQ
from RS import run_RS

# URLs for questionnaires
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


# Path to the data folder created by PsychoPy
psychopy_data_dir = os.path.join(script_dir, 'data')

# Path to the CSV file storing participant information
csv_file = os.path.join(script_dir, 'Participants_expInfo.csv')


def open_url(url):
    """Opens the given URL in the default web browser."""
    webbrowser.open(url)


def run_RS_task(participant_info):
    """Runs the Resting State task if not already completed."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # **Add this code to ensure 'completed_tasks' is a list**
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks
        
    if 'RS' in participant_info.get('completed_tasks', []):
        print("Skipping Resting State, already completed.")
        return

    try:
        print("Running Resting State task...")
        run_RS(participant_info)  # Assuming run_RS is properly defined
        participant_info['completed_tasks'].append('RS')
        update_participant_info(csv_file, participant_info)
    except Exception as e:
        print(f"Error while running Resting State: {e}")
        raise


def run_ARSQ_task(participant_info):
    """Runs the ARSQ questionnaire if not already completed."""
    # Ensure 'completed_tasks' is a list
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # **Add this code to ensure 'completed_tasks' is a list**
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    if 'ARSQ' in participant_info['completed_tasks']:
        print("Skipping ARSQ, already completed.")
        return

    try:
        print("Running ARSQ questionnaire...")
        # Launch the ARSQ questionnaire GUI
        root = tk.Tk()
        root.withdraw()  # Hide the root window if not needed
        arsq_window = tk.Toplevel()
        app = ARSQ(arsq_window, participant_info)
        arsq_window.wait_window()
        root.destroy()

        participant_info['completed_tasks'].append('ARSQ')
        update_participant_info(csv_file, participant_info)
    except Exception as e:
        print(f"Error while running ARSQ: {e}")
        raise

def run_psychopy_tasks(participant_info):
    """Runs the PsychoPy tasks for the current session."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # **Add this code to ensure 'completed_tasks' is a list**
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # Define tasks based on the current session
    if current_session == '1':
        tasks = {
            'SimpleRTT': "Speed_SimpleRTT/simpleRTT_lastrun.py",
            'Similarities': "Verbal_Similarities/Similarities_lastrun.py",
            'DoubleRTT': "Speed_DoubleRTT/DoubleRTT_lastrun.py",
            'Vocabulary': "Verbal_Vocabulary/vocabulary_lastrun.py",
            'SimpleRTT_mouse': "Speed_SimpleRTT_mouse/simpleRTT_mouse_lastrun.py",  
            'Knowledge': "Verbal_Knowledge/knowledge_lastrun.py"
        }
    elif current_session == '2':
        tasks = {
            'Antisaccade': "Inhibition_Antisaccade/Antisaccade_lastrun.py",
            'KeepTrack': "Updating_KeepTrack/KeepTrack_lastrun.py",
            'CategorySwitch': 'Switch_CategorySwitch/CategorySwitch_lastrun.py',
            'GoNoGo': "Inhibition_GoNoGo/GoNoGo_lastrun.py",
            'DualNback': "Updating_DualNback/DualNback_lastrun.py",
            'ColorShape': 'Switch_ColorShape/ColorShape_lastrun.py',
            'Oddball': "Perception_Oddball/Oddball_lastrun.py"
            
        }
    elif current_session == '3':
        tasks = {
            'MentalRotation': "MentalRotation_MRT/MentalRotation_lastrun.py",
            'VAC': "Perception_visuo-auditory-conflict/VAC_lastrun.py",
            'symbols': "Speed_Symbols/symbols_lastrun.py",
            'TOH': "Planning_TowerOfHanoi/TowerOfHanoi_lastrun.py",
            'coding': "Speed_Coding/coding_lastrun.py",
            'MARS': "Reasoning_MARS-IB/MARS-IB_lastrun.py"
        }
    else:
        print(f"No PsychoPy tasks defined for session {current_session}")
        return
    

    # Create the PsychoPy window
    win = visual.Window(
        size=[1920, 1080],
        fullscr=True,
        screen=0,
        winType='pyglet',
        allowGUI=True,
        allowStencil=False,
        monitor='testMonitor',
        color='grey',
        colorSpace='rgb',
        blendMode='avg',
        useFBO=True
    )

    for task_name, script_path in tasks.items():
        if task_name in completed_tasks:
            print(f"Skipping completed task: {task_name}")
            continue

        print(f"Running task: {task_name}")
        try:
            thisSession = session.Session(
                win=win,
                root=os.path.dirname(__file__),
                experiments={task_name: script_path}
            )
            thisSession.runExperiment(task_name, expInfo={
                'participant': participant_info['participant_id'],
                'session': participant_info['current_session'],
                'language': participant_info['language'],
                'date': datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            })
            completed_tasks.append(task_name)
            participant_info['completed_tasks'] = completed_tasks
            update_participant_info(csv_file, participant_info)
        except Exception as e:
            print(f"Error while running task {task_name}: {e}")
            win.close()
            raise

    win.close()
    
def run_MATB_training(participant_info):
    """Runs the MATB training."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # Ensure 'completed_tasks' is a list
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # Define a label for the training task
    training_label = f"MATB_training_session-{current_session}"

    if training_label in completed_tasks:
        print(f"Skipping completed MATB training: {training_label}")
        return  # If the training task is already completed, skip it

    print(f"Running MATB training for session {current_session}")
    try:
        MATB_training(participant_info)  # Runs the actual training

        # Append the training label to completed tasks and update participant info
        completed_tasks.append(training_label)
        participant_info['completed_tasks'] = completed_tasks
        update_participant_info(csv_file, participant_info)

        print(f"MATB training for session {current_session} completed successfully.")
    except Exception as e:
        print(f"Error while running MATB training {training_label}: {e}")
        raise
            
def run_MATB_tasks(participant_info):
    """Runs the MATB tasks with associated questionnaires."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # Ensure 'completed_tasks' is a list
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # Define MATB scenarios with session-specific filenames
    if current_session == '1':
        matb_scenarios = {
            'MATB_easy': f"session-{current_session}_easy.txt",
            'MATB_hard': f"session-{current_session}_hard.txt"
        }
    elif current_session in ['2', '3']:
        matb_scenarios = {
            'MATB_easy': f"session-{current_session}_easy.txt",
            'MATB_hard': f"session-{current_session}_hard.txt",
            'MATB_easy_oddball': f"session-{current_session}_easy_oddball.txt",
            'MATB_hard_oddball': f"session-{current_session}_hard_oddball.txt"
        }

    for scenario_label, scenario_file in matb_scenarios.items():
        completed_label = f"{scenario_label}_session-{current_session}"  # Session-specific label for tracking

        if completed_label in completed_tasks:
            print(f"Skipping completed MATB scenario: {scenario_label} for session {current_session}")
            continue

        print(f"Running MATB scenario: {scenario_label} for session {current_session}")
        try:
            # Run the task with the correct scenario filename
            run_matb_task(participant_info, scenario_file)
            
            # Append the session-specific label to completed tasks
            completed_tasks.append(completed_label)
            participant_info['completed_tasks'] = completed_tasks
            update_participant_info(csv_file, participant_info)

            # Launch the post-MATB questionnaire
            root = tk.Tk()
            app = QuestionnaireApp(root, participant_info, scenario_label)
            root.mainloop()
        except Exception as e:
            print(f"Error while running MATB scenario {scenario_label} for session {current_session}: {e}")
            raise

def run_MATB_instructions(participant_info):
    """Runs the MATB instructions if required."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # Ensure 'completed_tasks' is a list
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # The instructions are only used in sessions 2 and 3
    if current_session in ['2', '3']:
        instruction_label = f"MATB_instructions_session-{current_session}"
        
        if instruction_label in completed_tasks:
            print(f"Skipping completed MATB instructions: {instruction_label}")
            return  # If the instructions are already completed, skip it

        print(f"Running MATB instructions for session {current_session}")
        try:
            MATB_instructions(participant_info)  # Runs the instructions script

            # Append the instruction label to completed tasks and update participant info
            completed_tasks.append(instruction_label)
            participant_info['completed_tasks'] = ','.join(completed_tasks)
            update_participant_info(csv_file, participant_info)

            print(f"MATB instructions for session {current_session} completed successfully.")
        except Exception as e:
            print(f"Error while running MATB instructions {instruction_label}: {e}")
            raise
    else:
        print(f"MATB instructions are not required for session {current_session}")

def run_session(participant_info):
    """Runs the session tasks based on the current session number."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
    participant_info['completed_tasks'] = completed_tasks

    try:
        if current_session == '1':
            run_EyeTracking_Calibration(participant_info)
            run_RS_task(participant_info)
            run_ARSQ_task(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_training(participant_info)
            run_MATB_tasks(participant_info)
            #run_SF_training(participant_info)
            #run_SF_tasks(participant_info)            
        elif current_session == '2':
            run_EyeTracking_Calibration(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            #run_SF_instructions(participant_info)
            #run_SF_tasks(participant_info)          
        elif current_session == '3':
            run_EyeTracking_Calibration(participant_info)
            run_RS_task(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            #run_SF_instructions(participant_info)
            #run_SF_tasks(participant_info)    
        else:
            print(f"No tasks defined for session {current_session}")
            return

        # Move data to BIDS-compliant folder
        root_path = get_parent_directory(os.path.dirname(__file__))
        bids_folder = create_bids_structure(root_path, participant_info['participant_id'], current_session)
        copy_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_info['participant_id'], current_session)

        # Update session date and increment session number
        session_key = f"date_session{current_session}"
        participant_info[session_key] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        participant_info['current_session'] = str(int(current_session) + 1)
        update_participant_info(csv_file, participant_info)

        # Stop LabRecorder (if needed)
        send_command_to_labrecorder('stop\n')
        print("Session completed.")

    except Exception as e:
        print(f"Session interrupted due to error: {e}")
        print("You can restart the session to resume from where you left off.")
        # Optionally, re-raise the exception if you want to crash the program
        # raise
        
    finally:
        close_applications()
        
        
def launch_experiment_gui(participant_info):
    """Launches the GUI for starting the experiment tasks."""

    def start_experiment():
        root.destroy()
        run_session(participant_info)
        core.quit()

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
    def start_recording():
        try:
            launch_lsl_metascript(participant_info)
            button_tasks.config(state="normal")  # Enable the tasks button after recording starts
        except Exception as e:
            print(f"Error starting recording: {e}")
            tk.messagebox.showerror("Error", f"Failed to start recording: {e}")

    button_start_recording = tk.Button(button_frame, text="Start Recording", **button_options, command=start_recording)
    button_start_recording.grid(row=1, column=0, padx=20, pady=20)

    # Button for Tasks (Initially disabled)
    def start_tasks():
        minimize_all_windows()  # Minimize all open windows
        root.iconify()  # Minimize the main Tkinter window
        root.destroy()  # Optionally, destroy the main window if no longer needed
        launch_experiment_gui(participant_info)  # Start tasks
        button_finish.config(state="normal")  # Enable the finish button after tasks are completed

    button_tasks = tk.Button(button_frame, text="Start Tasks", **button_options, state="disabled", command=start_tasks)
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

    # 'Finish Session' button (Initially disabled) to stop recording and close the Tkinter window
    button_finish = tk.Button(bottom_frame, text="Finish Session", font=("Helvetica", 16), width=20, height=2, 
                              state="disabled", command=lambda: [send_command_to_labrecorder('stop\n'), root.destroy()])
    button_finish.grid(row=0, column=1, padx=10)

    root.mainloop()

def go_back_to_main_gui(root):
    """Handles the back button to return to the main GUI in main.py."""
    root.destroy()  # Close the current window
    from main import create_main_gui  # Import the main GUI function
    create_main_gui()  # Launch the main GUI




