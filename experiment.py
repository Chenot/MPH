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
        move_psychopy_data_to_bids(psychopy_data_dir, bids_folder, participant_info['participant_id'], current_session)

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
