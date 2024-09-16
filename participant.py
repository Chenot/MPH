import os
import csv
import tkinter as tk
from tkinter import messagebox
from utils import generate_next_id, generate_random_id, save_participant_info, load_participant_info
from experiment import launch_experiment_gui

# CSV file to store participant info
csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Participants_expInfo.csv')


def create_participant_gui():
    def create_participant():
        participant_id = generate_next_id(csv_file)
        participant_initials = entry_initials.get()
        language_participant = language_var.get()
        
        if not participant_initials or not language_participant:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        # Create the participant info dictionary without the 'last_task' field
        participant_info = {
            'participant_id': participant_id,
            'participant_initials': participant_initials,
            'participant_anonymized_id': generate_random_id(),
            'date_session1': 'NA',
            'date_session2': 'NA',
            'date_session3': 'NA',
            'language': language_participant,
            'current_session': '1',
            'completed_tasks': []  # No tasks completed yet
        }
        
        # Save the participant information to the CSV
        save_participant_info(csv_file, participant_info)
        
        # Close the window and launch the experiment GUI
        root.destroy()
        launch_experiment_gui(participant_info)

    # Tkinter window for creating a participant (remains unchanged)
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

    root.mainloop()



def select_participant_gui():
    def load_selected_participant():
        selected = participant_listbox.curselection()
        if not selected:
            messagebox.showerror("Selection Error", "Please select a participant")
            return
        participant_id = participant_ids[selected[0]]
        participant_info = load_participant_info(csv_file, participant_id)
        root.destroy()
        launch_experiment_gui(participant_info)

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
                participant_listbox.insert(tk.END, f"ID: {row['participant_id']}, Initials: {row['participant_initials']}, Language: {row['language']}")

    tk.Button(main_frame, text="Load", command=load_selected_participant, font=("Helvetica", 16)).pack(pady=10)

    root.mainloop()
