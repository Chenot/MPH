import os
import tkinter as tk
from psychopy import visual, core, session
from datetime import datetime
from utils import update_participant_info, create_bids_structure, move_psychopy_data_to_bids, get_parent_directory

# Path to the data folder created by PsychoPy
psychopy_data_dir = os.path.join(os.path.dirname(__file__), 'data')

# Path to the CSV file storing participant information
csv_file = os.path.join(os.path.dirname(__file__), 'Participants_expInfo.csv')

def launch_experiment_gui(participant_info):
    def start_experiment():
        root.destroy()  # Close the Tkinter window when "Start" is clicked
        current_session = participant_info['current_session']
        task_name = ''  # We'll determine this based on the session and task being run

        # Create the window for the experiment
        win = visual.Window(size=[1920, 1080], fullscr=True, screen=0, 
                            winType='pyglet', allowGUI=True, allowStencil=False,
                            monitor='testMonitor', color='grey', colorSpace='rgb',
                            blendMode='avg', useFBO=True)

        # Choose experiments based on the session
        if current_session == '1':
            task_name = 'SimpleRTT'
            thisSession = session.Session(
                win=win,
                root=os.path.dirname(__file__),
                experiments={
                    'SimpleRTT': "Speed_SimpleRTT/simpleRTT_lastrun.py",
                    'SimpleRTTmouse': "Speed_SimpleRTT_mouse/simpleRTT_mouse_lastrun.py",
                    'DoubleRTT': "Speed_DoubleRTT/DoubleRTT_lastrun.py", 
                }
            )
            run_session(thisSession, participant_info, list(thisSession.experiments.keys()))
        elif current_session == '2':
            task_name = 'Antisaccade'
            thisSession = session.Session(
                win=win,
                root=os.path.dirname(__file__),
                experiments={
                    'RS': "Resting_state/Resting_state_lastrun.py",
                    'Antisaccade': "Inhibition_Antisaccade/Antisaccade_lastrun.py", 
                    'KeepTrack': "Upadting_KeepTrack/KeepTrack_lastrun.py",      
                }
            )
            run_session(thisSession, participant_info, list(thisSession.experiments.keys()))
        elif current_session == '3':
            task_name = 'TOH'
            thisSession = session.Session(
                win=win,  
                root=os.path.dirname(__file__),
                experiments={
                    'RS': "Resting_state/Resting_state_lastrun.py",
                    'TOH': "Planning_TowerOfHanoi/TowerOfHanoi_lastrun.py", 
                    'RAPM': "Reasoning_RavenMatrices/RAPM_lastrun.py",      
                }
            )
            run_session(thisSession, participant_info, list(thisSession.experiments.keys()))

        # Once the session is completed, move data to the BIDS-compliant folder
        root_path = get_parent_directory(os.path.dirname(__file__))  # Get the parent directory
        bids_folder = create_bids_structure(root_path, participant_info['participant_id'], current_session)
        move_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_info['participant_id'], current_session, task_name)

        # Close the window and quit
        win.close()
        core.quit()

    def run_session(thisSession, participant_info, tasks):
        for task in tasks:
            if participant_info['last_task'] == task:
                continue
            thisSession.runExperiment(task, expInfo={
                'participant': participant_info['participant_id'], 
                'session': participant_info['current_session'], 
                'language': participant_info['language'], 
                'date': datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            })
            participant_info['last_task'] = task
            
            # Corrected: pass both the CSV file and participant info to update
            update_participant_info(csv_file, participant_info)

        # Update session date and session number
        session_key = f'date_session{participant_info["current_session"]}'
        participant_info[session_key] = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        participant_info['current_session'] = str(int(participant_info['current_session']) + 1)

        # Corrected: pass both the CSV file and participant info to update
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
