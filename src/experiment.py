import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from psychopy import visual, core, session
from datetime import datetime
import threading
import sqlite3

# ----------------------------------------------------------------
# Global paths
# ----------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))

# Adjust the path to import applications from scripts (MATB, questionnaires, resting-state, etc.)
psychopy_dir = os.path.join(script_dir, '..', 'tasks')  # Where PsychoPy tasks are stored
psychopy_data_dir = os.path.join(psychopy_dir, 'data')  # Where PsychoPy data is stored
matb_directory = os.path.join(script_dir, '..', 'tasks', 'Complex_OpenMATB')
questionnaire_directory = os.path.abspath(os.path.join(script_dir, '..', 'questionnaires'))
RS_directory = os.path.abspath(os.path.join(script_dir, '..', 'tasks', 'Resting_state'))
sys.path.append(matb_directory)
sys.path.append(questionnaire_directory)
sys.path.append(RS_directory)

# Define the local path
db_file = os.path.join(script_dir, '..', 'BIDS_data', 'Participants_expInfo.db')
data_dir = os.path.join(script_dir, '..', 'BIDS_data')

# Define the network data path
network_path = r"\\partage-neurodata\neurodata\MPH"
db_file_network = os.path.join(network_path, '..', 'BIDS_data', 'Participants_expInfo.db')
data_dir_network = os.path.join(network_path, '..', 'BIDS_data')

# --------------------------------------------------------------------------
# Import functions from other scripts: utils, MPH_MATB, ARSQ, questionnaires
# --------------------------------------------------------------------------
from utils import (
    generate_next_id,
    generate_random_id,
    save_participant_info,
    load_participant_info,
    update_participant_info,
    get_participant_info,
    extract_questionnaire_name,
    mark_questionnaire_completed,
    copy_matb_data_to_bids,
    minimize_all_windows,
    send_command_to_labrecorder,
    launch_lsl_metascript,
    run_EyeTracking_Calibration,
    perform_post_task_steps,
    open_url
)

from MPH_MATB import run_matb_task
from MPH_MATB_training import MATB_training
from MPH_MATB_instructions import MATB_instructions
from questionnaire_post_task import QuestionnaireApp
from run_questionnaire import run_questionnaire
from RS import run_RS

# ------------------ Questionnaire paths ------------------
# Session 1
path_demographics_english = os.path.join(questionnaire_directory, 'demographics_eng.txt')
path_demographics_french = os.path.join(questionnaire_directory, 'demographics_fr.txt')
path_BIG5_personality_english = os.path.join(questionnaire_directory, 'Big5_eng.txt')
path_BIG5_personality_french = os.path.join(questionnaire_directory, 'Big5_fr.txt')
path_SCI_sleep_english = os.path.join(questionnaire_directory, 'SCI_eng.txt')
path_SCI_sleep_french = os.path.join(questionnaire_directory, 'SCI_fr.txt')
path_EHI_laterality_english = os.path.join(questionnaire_directory, 'EHI_eng.txt')
path_EHI_laterality_french = os.path.join(questionnaire_directory, 'EHI_fr.txt')
path_presession_english = os.path.join(questionnaire_directory, 'presession_eng.txt')
path_presession_french = os.path.join(questionnaire_directory, 'presession_fr.txt')
path_ARSQ_english = os.path.join(questionnaire_directory, 'arsq_eng.txt')
path_ARSQ_french = os.path.join(questionnaire_directory, 'arsq_fr.txt')

# Session 2
path_REI_rationality_english = os.path.join(questionnaire_directory, 'REI_eng.txt')
path_REI_rationality_french = os.path.join(questionnaire_directory, 'REI_fr.txt')
path_MAI_metacognition_english = os.path.join(questionnaire_directory, 'MAI_eng.txt')
path_MAI_metacognition_french = os.path.join(questionnaire_directory, 'MAI_fr.txt')
path_VGxp_videogames_english = os.path.join(questionnaire_directory, 'VGexp_eng.txt')
path_VGxp_videogames_french = os.path.join(questionnaire_directory, 'VGexp_fr.txt')
path_RSES_selfesteem_english = os.path.join(questionnaire_directory, 'RSES_eng.txt')
path_RSES_selfesteem_french = os.path.join(questionnaire_directory, 'RSES_fr.txt')

# Session 3
path_RMEQ_chronotype_english = os.path.join(questionnaire_directory, 'rMEQ_eng.txt')
path_RMEQ_chronotype_french = os.path.join(questionnaire_directory, 'rMEQ_fr.txt')
path_TEIQ_emotions_english = os.path.join(questionnaire_directory, 'TEIQ_eng.txt')
path_TEIQ_emotions_french = os.path.join(questionnaire_directory, 'TEIQ_fr.txt')
path_SSEIT_emotions_english = os.path.join(questionnaire_directory, 'SSEIT_eng.txt')
path_SSEIT_emotions_french = os.path.join(questionnaire_directory, 'SSEIT_fr.txt')
path_BRIEF_executivefunctions_english = os.path.join(questionnaire_directory, 'BRIEF_eng.txt')
path_BRIEF_executivefunctions_french = os.path.join(questionnaire_directory, 'BRIEF_fr.txt')

# All sessions
path_post_task_q = os.path.join(questionnaire_directory, 'questionnaire_post-task.csv')

# Supplementary Questionnaires
path_MBTI_personality_english = os.path.join(questionnaire_directory, 'MBTI_eng.txt')
path_MBTI_personality_french = os.path.join(questionnaire_directory, 'MBTI_fr.txt')
path_PID_personality_english = os.path.join(questionnaire_directory, 'PID_eng.txt')
path_PID_personality_french = os.path.join(questionnaire_directory, 'PID_fr.txt')
path_QOL_quality_of_life_english = os.path.join(questionnaire_directory, 'Q-LES_eng.txt')
path_QOL_quality_of_life_french = os.path.join(questionnaire_directory, 'Q-LES_fr.txt')
path_STAI_anxiety_english = os.path.join(questionnaire_directory, 'SSEIT_eng.txt')
path_STAI_anxiety_french = os.path.join(questionnaire_directory, 'SSEIT_fr.txt')
path_BDI_depression_english = os.path.join(questionnaire_directory, 'BDI_eng.txt')
path_BDI_depression_french = os.path.join(questionnaire_directory, 'BDI_fr.txt')

# ------------------ Questionnaire URLs ------------------
# Session 1
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

# Session 2
url_REI_rationality_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=7Uxnwh"
url_REI_rationality_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=ER3HF"
url_MAI_metacognition_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=PXfzb"
url_MAI_metacognition_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=tVpfd"
url_VGxp_videogames_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Jyv4p"
url_VGxp_videogames_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=yL9pb"
url_RSES_selfesteem_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=jR8WZ"
url_RSES_selfesteem_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=FrgPf"

# Session 3
url_RMEQ_chronotype_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=uSgGw"
url_RMEQ_chronotype_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=A6V8e"
url_TEIQ_emotions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=32kBZ"
url_TEIQ_emotions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=zuEca"
url_SSEIT_emotions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=Rt3CC"
url_SSEIT_emotions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=WgpSS"
url_BRIEF_executivefunctions_english = "https://www.psytoolkit.org/c/3.4.6/survey?s=sSMjm"
url_BRIEF_executivefunctions_french = "https://www.psytoolkit.org/c/3.4.6/survey?s=taCZy"

# Supplementary Questionnaires
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

# ----------------------------------------------------------------
# RS and ARSQ tasks
# ----------------------------------------------------------------
def run_RS_task(participant_info):
    """Runs the Resting State task if not already completed."""
    completed_tasks = participant_info.get('completed_tasks', [])
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    if 'RS' in participant_info['completed_tasks']:
        print("Skipping Resting State, already completed.")
        return

    try:
        print("Running Resting State task...")
        run_RS(participant_info)  # The function from RS.py
        completed_tasks.append('RS')
        participant_info['completed_tasks'] = completed_tasks
        update_participant_info(db_file, participant_info)
    except Exception as e:
        print(f"Error while running Resting State: {e}")
        raise


def run_ARSQ_task(participant_info):
    """Runs the ARSQ questionnaire if not already completed."""
    completed_tasks = participant_info.get('completed_tasks', [])
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    if 'ARSQ' in completed_tasks:
        print("Skipping ARSQ, already completed.")
        return

    try:
        print("Running ARSQ questionnaire...")

        # Define the path to the ARSQ questionnaire based on the language
        language = participant_info['language']
        questionnaire_file = path_ARSQ_french if language == 'French' else path_ARSQ_english
        run_questionnaire(questionnaire_file, participant_info)
        completed_tasks.append('ARSQ')
        participant_info['completed_tasks'] = completed_tasks
        update_participant_info(db_file, participant_info)
        
    except Exception as e:
        print(f"Error while running ARSQ: {e}")
        raise


# ----------------------------------------------------------------
# PsychoPy cognitive tasks
# ----------------------------------------------------------------
def run_psychopy_tasks(participant_info):
    """Runs the PsychoPy tasks for the current session."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # Define tasks based on session
    if current_session == '1':
        tasks = {
            'SimpleRTT': os.path.abspath(os.path.join(psychopy_dir, "Speed_SimpleRTT", "simpleRTT_lastrun.py")),
            'Similarities': os.path.abspath(os.path.join(psychopy_dir, "Verbal_Similarities", "Similarities_lastrun.py")),
            'DoubleRTT': os.path.abspath(os.path.join(psychopy_dir, "Speed_DoubleRTT", "DoubleRTT_lastrun.py")),
            'Vocabulary': os.path.abspath(os.path.join(psychopy_dir, "Verbal_Vocabulary", "vocabulary_lastrun.py")),
            'SimpleRTTmouse': os.path.abspath(os.path.join(psychopy_dir, "Speed_SimpleRTTmouse", "simpleRTTmouse_lastrun.py")),
            'Knowledge': os.path.abspath(os.path.join(psychopy_dir, "Verbal_Knowledge", "knowledge_lastrun.py")),
            'numericalRTT': os.path.abspath(os.path.join(psychopy_dir, "Speed_NumericalRTT", "numericalRTT_lastrun.py"))
        }
    elif current_session == '2':
        tasks = {
            'Antisaccade': os.path.abspath(os.path.join(psychopy_dir, "Inhibition_Antisaccade", "Antisaccade_lastrun.py")),
            'KeepTrack': os.path.abspath(os.path.join(psychopy_dir, "Updating_KeepTrack", "KeepTrack_lastrun.py")),
            'CategorySwitch': os.path.abspath(os.path.join(psychopy_dir, "Switch_CategorySwitch", "CategorySwitch_lastrun.py")),
            'GoNoGo': os.path.abspath(os.path.join(psychopy_dir, "Inhibition_GoNoGo", "GoNoGo_lastrun.py")),
            'DualNback': os.path.abspath(os.path.join(psychopy_dir, "Updating_DualNback", "DualNback_lastrun.py")),
            'ColorShape': os.path.abspath(os.path.join(psychopy_dir, "Switch_ColorShape", "ColorShape_lastrun.py")),
            'Oddball': os.path.abspath(os.path.join(psychopy_dir, "Perception_Oddball", "Oddball_lastrun.py"))
        }
    elif current_session == '3':
        tasks = {
            'MentalRotation': os.path.abspath(os.path.join(psychopy_dir, "MentalRotation_MRT", "MentalRotation_lastrun.py")),
            'VAC': os.path.abspath(os.path.join(psychopy_dir, "Perception_visuo-auditory-conflict", "VAC_lastrun.py")),
            'symbols': os.path.abspath(os.path.join(psychopy_dir, "Speed_Symbols", "symbols_lastrun.py")),
            'TOH': os.path.abspath(os.path.join(psychopy_dir, "Planning_TowerOfHanoi", "TowerOfHanoi_lastrun.py")),
            'coding': os.path.abspath(os.path.join(psychopy_dir, "Speed_Coding", "coding_lastrun.py")),
            'MARS': os.path.abspath(os.path.join(psychopy_dir, "Reasoning_MARS-IB", "MARS-IB_lastrun.py"))
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

    # Run each task in turn
    for task_name, script_path in tasks.items():
        if task_name in completed_tasks:
            print(f"Skipping completed task: {task_name}")
            continue
        print(f"Running task: {task_name}")
        
        try:
            thisSession = session.Session(
                win=win,
                root=os.path.abspath(os.path.join(psychopy_dir)),
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
            update_participant_info(db_file, participant_info)
        except Exception as e:
            print(f"Error while running task {task_name}: {e}")
            win.close()
            raise

    win.close()


# ----------------------------------------------------------------
# MATB training/tasks
# ----------------------------------------------------------------
def run_MATB_training(participant_info):
    """Runs the MATB training."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    training_label = f"MATB_training_session-{current_session}"

    if training_label in completed_tasks:
        print(f"Skipping completed MATB training: {training_label}")
        return

    print(f"Running MATB training for session {current_session}")
    try:
        MATB_training(participant_info)
        completed_tasks.append(training_label)
        participant_info['completed_tasks'] = completed_tasks
        update_participant_info(db_file, participant_info)
        print(f"MATB training for session {current_session} completed successfully.")
    except Exception as e:
        print(f"Error while running MATB training {training_label}: {e}")
        raise


def run_MATB_tasks(participant_info):
    """Runs the MATB tasks with associated questionnaires."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])
    os.chdir(matb_directory)  # Change directory (errors may appear otherwise)

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
    else:
        matb_scenarios = {}

    for scenario_label, scenario_file in matb_scenarios.items():
        completed_label = f"{scenario_label}_session-{current_session}"
        if completed_label in completed_tasks:
            print(f"Skipping completed MATB scenario: {scenario_label} for session {current_session}")
            continue

        print(f"Running MATB scenario: {scenario_label} for session {current_session}")
        try:
            run_matb_task(participant_info, scenario_file)
            completed_tasks.append(completed_label)
            participant_info['completed_tasks'] = completed_tasks
            update_participant_info(db_file, participant_info)

            # Launch the post-MATB questionnaire
            root = tk.Tk()
            app = QuestionnaireApp(root, participant_info, scenario_label)
            root.mainloop()
            copy_matb_data_to_bids(participant_info, scenario_label)
        except Exception as e:
            print(f"Error while running MATB scenario {scenario_label}: {e}")
            raise


def run_MATB_instructions(participant_info):
    """Runs the MATB instructions if required."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
        participant_info['completed_tasks'] = completed_tasks

    # Only for sessions 2 and 3
    if current_session in ['2', '3']:
        instruction_label = f"MATB_instructions_session-{current_session}"
        if instruction_label in completed_tasks:
            print(f"Skipping completed MATB instructions: {instruction_label}")
            return

        print(f"Running MATB instructions for session {current_session}")
        try:
            MATB_instructions(participant_info)
            completed_tasks.append(instruction_label)
            # Here, for historical reasons, completed_tasks was stored as a comma‐separated string:
            participant_info['completed_tasks'] = ",".join(completed_tasks)
            update_participant_info(db_file, participant_info)
            print(f"MATB instructions for session {current_session} completed successfully.")
        except Exception as e:
            print(f"Error while running MATB instructions {instruction_label}: {e}")
            raise
    else:
        print(f"MATB instructions are not required for session {current_session}")


# ----------------------------------------------------------------
# The run_session function (MAIN LOGIC)
# ----------------------------------------------------------------
def run_session(participant_info):
    """Runs the session"""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])

    # Convert completed_tasks to list if needed
    if isinstance(completed_tasks, str):
        completed_tasks = completed_tasks.split(',') if completed_tasks else []
    participant_info['completed_tasks'] = completed_tasks
 
    try:
        # RUN MAIN TASKS
        if current_session == '1':
            #run_EyeTracking_Calibration(participant_info)
            #run_RS_task(participant_info)
            #run_ARSQ_task(participant_info)
            # run_psychopy_tasks(participant_info)
            # run_MATB_training(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_training(participant_info)
            # run_SF_tasks(participant_info)

        elif current_session == '2':
            #run_EyeTracking_Calibration(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_instructions(participant_info)
            # run_SF_tasks(participant_info)

        elif current_session == '3':
            #run_EyeTracking_Calibration(participant_info)
            #run_RS_task(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_instructions(participant_info)
            # run_SF_tasks(participant_info)

        else:
            print(f"No tasks defined for session {current_session}")
            return

        print("All session tasks completed successfully.")
        tasks_completed = True  # Only mark as complete if no exception was raised.
        
    except Exception as e:
        print(f"Error during session tasks: {e}")
        print("You can restart the session to resume from where you left off.")

    finally:
        post_task_thread = threading.Thread(
            target=perform_post_task_steps,
            args=(participant_info, db_file, psychopy_data_dir, data_dir_network, tasks_completed)
        )
        post_task_thread.start()
    
        # At the same time, show the session complete screen in the main thread.
        show_end_page_experiment(participant_info)

# ----------------------------------------------------------------
# GUI-related launch functions
# ----------------------------------------------------------------
def create_main_gui():
    def open_create_participant():
        root.destroy()
        create_participant_gui()

    def open_select_participant():
        root.destroy()
        select_participant_gui()
    
    def close_app():
        root.destroy()  # This will close the Tkinter application
    
    root = tk.Tk()
    root.title("MPH experiment")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Buttons for creating/selecting participants
    tk.Button(main_frame, text="Create Participant", command=open_create_participant, font=("Helvetica", 20)).pack(pady=10)
    tk.Button(main_frame, text="Select Participant", command=open_select_participant, font=("Helvetica", 20)).pack(pady=10)
    
    # Exit button at the bottom
    tk.Button(main_frame, text="Exit", command=close_app, font=("Helvetica", 10)).pack(pady=10)
    root.mainloop()


def create_participant_gui():
    def create_participant():
        participant_id = generate_next_id(db_file)
        participant_initials = entry_initials.get()
        language_participant = language_var.get()
        
        if not participant_initials or not language_participant:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        # Create the participant info dictionary
        participant_info = {
            'participant_id': participant_id,
            'participant_initials': participant_initials,
            'participant_anonymized_id': generate_random_id(),
            'date_session1': 'NA',
            'date_session2': 'NA',
            'date_session3': 'NA',
            'language': language_participant,
            'current_session': '1',
            'completed_tasks': ''  # No tasks completed yet
        }
        
        # Save the participant information to the DB
        save_participant_info(db_file, participant_info)
        
        # Close the window and launch the main GUI
        root.destroy()
        launch_main_gui(participant_info)

    def close_create_participant():
        root.destroy()  # This will close the Tkinter application
        create_main_gui()
        
    # Tkinter window for creating a participant
    root = tk.Tk()
    root.title("Create Participant")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(main_frame, text="Participant Initials", font=("Helvetica", 16)).grid(row=0, column=0, pady=10)
    entry_initials = tk.Entry(main_frame, font=("Helvetica", 16))
    entry_initials.grid(row=0, column=1, pady=10)

    tk.Label(main_frame, text="Language", font=("Helvetica", 16)).grid(row=1, column=0, pady=10)
    language_var = tk.StringVar(root)
    language_var.set("French")
    tk.OptionMenu(main_frame, language_var, "French", "English").grid(row=1, column=1, pady=10)

    tk.Button(main_frame, text="Create", command=create_participant, font=("Helvetica", 16)).grid(row=2, columnspan=2, pady=10)

    # Back button at the bottom
    tk.Button(main_frame, text="Back", command=close_create_participant, font=("Helvetica", 10))\
    .grid(row=3, columnspan=2, pady=20)


def select_participant_gui():
    def load_selected_participant_from_tree():
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a participant")
            return
        # Get the participant_id from the selected row.
        pid = treeview.set(selected_item[0], "participant_id")
        participant_info = load_participant_info(db_file, pid)
        root.destroy()
        launch_main_gui(participant_info)

    def close_load_selected_participant():
        root.destroy()  # Close the Tkinter application
        create_main_gui()

    def on_double_click(event):
        # Identify the item and column clicked.
        region = treeview.identify("region", event.x, event.y)
        if region != "cell":
            return

        rowid = treeview.identify_row(event.y)
        column = treeview.identify_column(event.x)
        if not rowid or column == "#0":
            return

        # Get bounding box of the cell in the treeview.
        x, y, width, height = treeview.bbox(rowid, column)
        # Map the Treeview column (e.g. "#1") to our field name.
        col_index = int(column.replace("#", "")) - 1
        col_names = ["participant_id", "participant_initials", "current_session", "completed_tasks"]
        field = col_names[col_index]

        # Get the current cell value.
        current_value = treeview.set(rowid, column)

        # Create an Entry widget over the cell.
        entry = tk.Entry(treeview)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, current_value)
        entry.focus_set()

        def on_focus_out(event):
            new_value = entry.get()
            treeview.set(rowid, column, new_value)
            entry.destroy()
            # Update the database record.
            pid = treeview.set(rowid, "participant_id")
            # Load the full participant info dictionary.
            p_info = load_participant_info(db_file, pid)
            # Update the changed field.
            p_info[field] = new_value
            update_participant_info(db_file, p_info)

        entry.bind("<Return>", lambda e: on_focus_out(e))
        entry.bind("<FocusOut>", on_focus_out)

    # Create the main window.
    root = tk.Tk()
    root.title("Select Participant")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create a Treeview widget with our desired columns.
    columns = ("participant_id", "participant_initials", "current_session", "completed_tasks")
    treeview = ttk.Treeview(main_frame, columns=columns, show="headings", height=20)
    treeview.heading("participant_id", text="Participant ID")
    treeview.heading("participant_initials", text="Participant Initials")
    treeview.heading("current_session", text="Current Session")
    treeview.heading("completed_tasks", text="Completed Tasks")
    treeview.column("participant_id", width=80)
    treeview.column("participant_initials", width=130)
    treeview.column("current_session", width=100)
    treeview.column("completed_tasks", width=1500)
    treeview.pack(pady=10)

    # Load participants from the database.
    participant_ids = []
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM participants")
        rows = c.fetchall()
        for row in rows:
            pid = row['participant_id']
            participant_ids.append(pid)
            initials = row['participant_initials']
            current_session = row['current_session']
            completed = row['completed_tasks']
            treeview.insert("", tk.END, values=(pid, initials, current_session, completed))
        conn.close()
    except Exception as e:
        print(f"Error loading participants from DB: {e}")

    # Bind a double-click to allow editing cells.
    treeview.bind("<Double-1>", on_double_click)

    # Load button.
    tk.Button(main_frame, text="Load", command=load_selected_participant_from_tree, font=("Helvetica", 16)).pack(pady=10)
    # Back button.
    tk.Button(main_frame, text="Back", command=close_load_selected_participant, font=("Helvetica", 10)).pack(pady=20)

    root.mainloop()


def launch_experiment_gui(participant_info):
    """Launches the GUI for starting the experiment tasks."""
    def start_experiment():
        root.destroy()
        run_session(participant_info)
        core.quit()

    root = tk.Tk()
    root.title("Launch Experiment")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(main_frame, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(main_frame, text=f"Participant Initials: {participant_info['participant_initials']}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(main_frame, text=f"Current Session: {participant_info['current_session']}", font=("Helvetica", 16)).pack(pady=10)

    tk.Button(main_frame, text="Start", command=start_experiment, font=("Helvetica", 16)).pack(pady=10)
    root.mainloop()

def run_and_update_questionnaire(q_path, participant_info, db_file):
    # Run the questionnaire (this call blocks until the questionnaire window is closed)
    run_questionnaire(q_path, participant_info)
    if participant_info.get("questionnaire_completed", False):
        mark_questionnaire_completed(db_file, participant_info, q_path)
    updated_info = get_participant_info(db_file, participant_info['participant_id'])
    current_root = tk._default_root
    if current_root is not None:
        current_root.destroy()
    launch_questionnaire_gui(updated_info)

def launch_questionnaire_gui(participant_info):
    """Launches the GUI for selecting questionnaires based on the session and language."""
    # Refresh participant_info from the DB so we have the latest completed_questionnaires.
    participant_info = get_participant_info(db_file, participant_info['participant_id'])
    
    current_session = participant_info['current_session']
    language = participant_info['language']
    
    # Define the paths for each questionnaire based on the session and language
    if current_session == '1':
        paths = {
            "Demographics": path_demographics_french if language == "French" else path_demographics_english,
            "Personality (BIG-5)": path_BIG5_personality_french if language == "French" else path_BIG5_personality_english,
            "Sleep Quality (SCI)": path_SCI_sleep_french if language == "French" else path_SCI_sleep_english,
            "Handedness (EHI)": path_EHI_laterality_french if language == "French" else path_EHI_laterality_english,
            "Pre-session": path_presession_french if language == "French" else path_presession_english
        }
    elif current_session == '2':
        paths = {
            "Rationality (REI)": path_REI_rationality_french if language == "French" else path_REI_rationality_english,
            "Meta-cognition (MAI)": path_MAI_metacognition_french if language == "French" else path_MAI_metacognition_english,
            "Video Game Experience (VGxp)": path_VGxp_videogames_french if language == "French" else path_VGxp_videogames_english,
            "Self-esteem (RSES)": path_RSES_selfesteem_french if language == "French" else path_RSES_selfesteem_english,
            "Pre-session": path_presession_french if language == "French" else path_presession_english
        }
    elif current_session == '3':
        paths = {
            "Chronotype (rMEQ)": path_RMEQ_chronotype_french if language == "French" else path_RMEQ_chronotype_english,
            "Emotions (TEIQ)": path_TEIQ_emotions_french if language == "French" else path_TEIQ_emotions_english,
            "Emotions (SSEIT)": path_SSEIT_emotions_french if language == "French" else path_SSEIT_emotions_english,
            "Executive Functions (BRIEF)": path_BRIEF_executivefunctions_french if language == "French" else path_BRIEF_executivefunctions_english
        }
    else:
        paths = {}

    root = tk.Tk()
    root.title(f"Questionnaires for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    tk.Label(root, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16)).pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)
    
    # Process the completed_questionnaires list: split and strip any whitespace.
    completed_questionnaires = participant_info.get("completed_questionnaires", [])
    if isinstance(completed_questionnaires, str):
        completed_questionnaires = [x.strip() for x in completed_questionnaires.split(',') if x.strip()]

    # We'll also keep a reference to the buttons if needed later.
    questionnaire_buttons = {}

    for title, path in paths.items():
        # Extract and trim the questionnaire name from the file path.
        qname = extract_questionnaire_name(path).strip()
        # Disable the button if the questionnaire is already completed.
        state = "disabled" if qname in completed_questionnaires else "normal"
        btn = tk.Button(
            button_frame, text=title, font=("Helvetica", 14),
            command=lambda p=path: run_and_update_questionnaire(p, participant_info, db_file),
            state=state
        )
        btn.pack(padx=20, pady=10)
        questionnaire_buttons[qname] = btn

    # Back button to return to main menu
    button_back = tk.Button(
        root, text="Back", font=("Helvetica", 16),
        command=lambda: [root.destroy(), launch_main_gui(participant_info)]
    )
    button_back.pack(pady=20)

    root.mainloop()



def launch_supplementary_questionnaire_gui(participant_info):
    """Launches the GUI for selecting supplementary questionnaires based on language."""
    language = participant_info['language']
    urls = {
        "Personality (MBTI)": url_MBTI_personality_french if language == "French" else url_MBTI_personality_english,
        "Personality (PID)": url_PID_personality_french if language == "French" else url_PID_personality_english,
        "Quality of Life": url_QOL_quality_of_life_french if language == "French" else url_QOL_quality_of_life_english,
        "Anxiety (STAI)": url_STAI_anxiety_french if language == "French" else url_STAI_anxiety_english,
        "Depression (BDI)": url_BDI_depression_french if language == "French" else url_BDI_depression_english
    }

    root = tk.Tk()
    root.title(f"Supplementary Questionnaires for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    tk.Label(root, text=f"Participant ID: {participant_info['participant_id']}", font=("Helvetica", 16)).pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)

    for title, url in urls.items():
        tk.Button(button_frame, text=title, font=("Helvetica", 14), command=lambda u=url: open_url(u)).pack(padx=20, pady=10)

    button_back = tk.Button(root, text="Back", font=("Helvetica", 16),
                            command=lambda: [root.destroy(), launch_main_gui(participant_info)])
    button_back.pack(pady=20)
    root.mainloop()


def launch_main_gui(participant_info):
    """Main GUI with options for 'Questionnaires', 'Start Recording', 'Tasks', 'Supplementary Questionnaires', etc."""
    root = tk.Tk()
    root.title(f"Main Menu for Participant {participant_info['participant_id']}")
    root.attributes('-fullscreen', True)

    tk.Label(root, text=f"Participant ID: P{participant_info['participant_id']}", font=("Helvetica", 20)).pack(pady=10)
    tk.Label(root, text=f"Session: {participant_info['current_session']}", font=("Helvetica", 18)).pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=100)

    button_options = {"font": ("Helvetica", 20), "width": 30, "height": 2}

    def start_recording():
        try:
            launch_lsl_metascript(participant_info)
            button_tasks.config(state="normal")
        except Exception as e:
            print(f"Error starting recording: {e}")
            tk.messagebox.showerror("Error", f"Failed to start recording: {e}")

    def start_tasks():
        minimize_all_windows()
        root.iconify()
        root.destroy()
        launch_experiment_gui(participant_info)
        button_finish.config(state="normal")

    button_questionnaires = tk.Button(button_frame, text="Questionnaires", **button_options,
                                      command=lambda: [root.destroy(), launch_questionnaire_gui(participant_info)])
    button_questionnaires.grid(row=0, column=0, padx=20, pady=20)

    button_start_recording = tk.Button(button_frame, text="Start Recording", **button_options, command=start_recording)
    button_start_recording.grid(row=1, column=0, padx=20, pady=20)

    button_tasks = tk.Button(button_frame, text="Start Tasks", **button_options, state="normal", command=start_tasks)
    button_tasks.grid(row=2, column=0, padx=20, pady=20)

    button_supplementary = tk.Button(button_frame, text="Supplementary Questionnaires", **button_options,
                                     command=lambda: [root.destroy(), launch_supplementary_questionnaire_gui(participant_info)])
    button_supplementary.grid(row=3, column=0, padx=20, pady=20)

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, pady=20)

    def go_back_to_main_gui_local():
        root.destroy()
        from main import create_main_gui
        create_main_gui()

    button_back = tk.Button(bottom_frame, text="Back", font=("Helvetica", 16), width=20, height=2,
                            command=go_back_to_main_gui_local)
    button_back.grid(row=0, column=0, padx=10)

    button_finish = tk.Button(bottom_frame, text="Finish Session", font=("Helvetica", 16),
                              width=20, height=2, state="disabled",
                              command=lambda: [send_command_to_labrecorder('stop\n'), root.destroy()])
    button_finish.grid(row=0, column=1, padx=10)

    root.mainloop()


def show_end_page_experiment(participant_info):
    """
    Displays a fullscreen grey Tkinter page with a message in 
    French or English, depending on participant_info['language'].
    """
    root = tk.Tk()
    root.title("Session Complete")
    root.attributes('-fullscreen', True)
    root.configure(bg='grey')

    # Centered frame
    frame = tk.Frame(root, bg='grey')
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    language = participant_info.get('language', 'English')

    if language == 'French':
        text = (
            "La session est maintenant terminée.\n\n"
            "Merci pour votre participation.\n\n"
            "Vous pouvez maintenant appeler l'expérimentateur :\n"
            "Quentin Chenot : 06.32.47.81.42\n"
        )
    else:
        text = (
            "The session is now over.\n\n"
            "Thank you for your participation.\n\n"
            "You can now call the experimenters:\n"
            "Quentin Chenot: +33.6.32.47.81.42\n"
        )

    label = tk.Label(frame, text=text, font=("Helvetica", 24), fg='white', bg='grey')
    label.pack()

    # Optionally, let them press Escape or click to close
    def close_window(_event=None):
        root.destroy()

    root.bind("<Escape>", close_window)
    # Or root.bind("<Button-1>", close_window) to close on mouse click

    root.mainloop()
