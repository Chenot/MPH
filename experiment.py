import os
import sys
import csv
import tkinter as tk
from tkinter import messagebox
from psychopy import visual, core, session
from datetime import datetime

# ----------------------------------------------------------------
# Global paths
# ----------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
psychopy_data_dir = os.path.join(script_dir, 'data')  # Where PsychoPy data is stored
csv_file = os.path.join(script_dir, 'Participants_expInfo.csv')

# Adjust the path to import MATB, questionnaires, resting-state
script_dir = os.path.dirname(os.path.abspath(__file__))
matb_directory = os.path.join(script_dir, 'Complex_OpenMATB')
questionnaire_directory = os.path.abspath(os.path.join(script_dir, 'Questionnaires'))
RS_directory = os.path.abspath(os.path.join(script_dir, 'Resting_state'))
 

sys.path.append(matb_directory)
sys.path.append(questionnaire_directory)
sys.path.append(RS_directory)

# --------------------------------------------------------------------------
# Import functions from other scripts: utils, MPH_MATB, ARSQ, questionnaires
# --------------------------------------------------------------------------
from utils import (
    generate_next_id,
    generate_random_id,
    save_participant_info,
    load_participant_info,
    update_participant_info,
    create_bids_structure,
    copy_psychopy_data_to_bids,
    get_parent_directory,
    minimize_all_windows,
    send_command_to_labrecorder,
    launch_lsl_metascript,
    run_EyeTracking_Calibration,
    close_applications,
    perform_post_task_steps,
    open_url
)

from MPH_MATB import run_matb_task
from MPH_MATB_training import MATB_training
from MPH_MATB_instructions import MATB_instructions
from questionnaire_post_task import QuestionnaireApp
from questionnaire_ARSQ import ARSQ
from RS import run_RS

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
        update_participant_info(csv_file, participant_info)
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
        root = tk.Tk()
        root.withdraw()
        arsq_window = tk.Toplevel()
        app = ARSQ(arsq_window, participant_info)
        arsq_window.wait_window()
        root.destroy()

        completed_tasks.append('ARSQ')
        participant_info['completed_tasks'] = completed_tasks
        update_participant_info(csv_file, participant_info)
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
            'SimpleRTT': "Speed_SimpleRTT/simpleRTT_lastrun.py",
            'Similarities': "Verbal_Similarities/Similarities_lastrun.py",
            'DoubleRTT': "Speed_DoubleRTT/DoubleRTT_lastrun.py",
            'Vocabulary': "Verbal_Vocabulary/vocabulary_lastrun.py",
            'SimpleRTTmouse': "Speed_SimpleRTTmouse/simpleRTTmouse_lastrun.py",
            'Knowledge': "Verbal_Knowledge/knowledge_lastrun.py",
            'numericalRTT': "Speed_Numerical/numericalRTT_lastrun.py"
        }
    elif current_session == '2':
        tasks = {
            'Antisaccade': "Inhibition_Antisaccade/Antisaccade_lastrun.py",
            'KeepTrack': "Updating_KeepTrack/KeepTrack_lastrun.py",
            'CategorySwitch': "Switch_CategorySwitch/CategorySwitch_lastrun.py",
            'GoNoGo': "Inhibition_GoNoGo/GoNoGo_lastrun.py",
            'DualNback': "Updating_DualNback/DualNback_lastrun.py",
            'ColorShape': "Switch_ColorShape/ColorShape_lastrun.py",
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

    # Run each task in turn
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
        update_participant_info(csv_file, participant_info)
        print(f"MATB training for session {current_session} completed successfully.")
    except Exception as e:
        print(f"Error while running MATB training {training_label}: {e}")
        raise


def run_MATB_tasks(participant_info):
    """Runs the MATB tasks with associated questionnaires."""
    current_session = participant_info['current_session']
    completed_tasks = participant_info.get('completed_tasks', [])
    os.chdir(matb_directory) # Change directory (errors may appear otherwise)

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
            update_participant_info(csv_file, participant_info)

            # Launch the post-MATB questionnaire
            root = tk.Tk()
            app = QuestionnaireApp(root, participant_info, scenario_label)
            root.mainloop()
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
            participant_info['completed_tasks'] = ",".join(completed_tasks)
            update_participant_info(csv_file, participant_info)
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
            run_EyeTracking_Calibration(participant_info)
            run_RS_task(participant_info)
            run_ARSQ_task(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_training(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_training(participant_info)
            # run_SF_tasks(participant_info)

        elif current_session == '2':
            run_EyeTracking_Calibration(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_instructions(participant_info)
            # run_SF_tasks(participant_info)

        elif current_session == '3':
            run_EyeTracking_Calibration(participant_info)
            run_RS_task(participant_info)
            run_psychopy_tasks(participant_info)
            run_MATB_instructions(participant_info)
            run_MATB_tasks(participant_info)
            # run_SF_instructions(participant_info)
            # run_SF_tasks(participant_info)

        else:
            print(f"No tasks defined for session {current_session}")
            return

        print("All session tasks completed successfully.")

    except Exception as e:
        print(f"Error during session tasks: {e}")
        print("You can restart the session to resume from where you left off.")

    finally:
        # PERFORM POST-TASK STEPS:
        # 1) Stop Lab Recoder
        # 2) Update session date & increment session number in the Participants_expInfo file
        # 3) Move data to BIDS folder
        # 4) Create a log file of the session
        # 5) Close apps
        # 6) Show the end of the session page for the participant
        perform_post_task_steps(participant_info, csv_file, psychopy_data_dir)
        


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
        participant_id = generate_next_id(csv_file)
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
        
        # Save the participant information to the CSV
        save_participant_info(csv_file, participant_info)
        
        # Close the window and launch the questionnaire GUI
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
    def load_selected_participant():
        selected = participant_listbox.curselection()
        if not selected:
            messagebox.showerror("Selection Error", "Please select a participant")
            return
        participant_id = participant_ids[selected[0]]
        participant_info = load_participant_info(csv_file, participant_id)

        # Close the window and launch the questionnaire GUI
        root.destroy()
        launch_main_gui(participant_info)

    def close_load_selected_participant():
        root.destroy()  # This will close the Tkinter application
        create_main_gui()

    # Tkinter window for selecting a participant
    root = tk.Tk()
    root.title("Select Participant")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(main_frame, text="Select Participant", font=("Helvetica", 16)).pack(pady=10)
    participant_listbox = tk.Listbox(main_frame, width=50, height=20, font=("Helvetica", 14))
    participant_listbox.pack(pady=10)

    participant_ids = []
    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                participant_ids.append(row['participant_id'])
                participant_listbox.insert(tk.END, f"ID: {row['participant_id']}, Initials: {row['participant_initials']}, session: {row['current_session']}, Language: {row['language']}")

    tk.Button(main_frame, text="Load", command=load_selected_participant, font=("Helvetica", 16)).pack(pady=10)

    # Back button at the bottom
    tk.Button(main_frame, text="Back", command=close_load_selected_participant, font=("Helvetica", 10)).pack(pady=20)
    root.mainloop()


def launch_experiment_gui(participant_info):
    """Launches the GUI for starting the experiment tasks."""
    def start_experiment():
        root.destroy()
        run_session(participant_info)
        show_end_page_experiment(participant_info)
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


def launch_questionnaire_gui(participant_info):
    """Launches the GUI for selecting questionnaires based on the session and language."""
    current_session = participant_info['current_session']
    language = participant_info['language']

    if current_session == '1':
        urls = {
            "Demographics": url_demographics_french if language == "French" else url_demographics_english,
            "Personality (BIG-5)": url_BIG5_personality_french if language == "French" else url_BIG5_personality_english,
            "Sleep Quality (SCI)": url_SCI_sleep_french if language == "French" else url_SCI_sleep_english,
            "Handedness (EHI)": url_EHI_laterality_french if language == "French" else url_EHI_laterality_english,
            "Pre-session": url_presession_french if language == "French" else url_presession_english
        }
    elif current_session == '2':
        urls = {
            "Rationality (REI)": url_REI_rationality_french if language == "French" else url_REI_rationality_english,
            "Meta-cognition (MAI)": url_MAI_metacognition_french if language == "French" else url_MAI_metacognition_english,
            "Video Game Experience (VGxp)": url_VGxp_videogames_french if language == "French" else url_VGxp_videogames_english,
            "Self-esteem (RSES)": url_RSES_selfesteem_french if language == "French" else url_RSES_selfesteem_english,
            "Pre-session": url_presession_french if language == "French" else url_presession_english
        }
    elif current_session == '3':
        urls = {
            "Chronotype (rMEQ)": url_RMEQ_chronotype_french if language == "French" else url_RMEQ_chronotype_english,
            "Emotions (TEIQ)": url_TEIQ_emotions_french if language == "French" else url_TEIQ_emotions_english,
            "Emotions (SSEIT)": url_SSEIT_emotions_french if language == "French" else url_SSEIT_emotions_english,
            "Executive Functions (BRIEF)": url_BRIEF_executivefunctions_french if language == "French" else url_BRIEF_executivefunctions_english
        }
    else:
        urls = {}

    root = tk.Tk()
    root.title(f"Questionnaires for Participant {participant_info['participant_id']}")
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

    button_tasks = tk.Button(button_frame, text="Start Tasks", **button_options, state="disabled", command=start_tasks)
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