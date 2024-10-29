import tkinter as tk
from participant import create_participant_gui, select_participant_gui

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
    root.title("Cognitive Experiment Meta Script")
    root.attributes('-fullscreen', True)

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Buttons for creating/selecting participants
    tk.Button(main_frame, text="Create Participant", command=open_create_participant, font=("Helvetica", 20)).pack(pady=10)
    tk.Button(main_frame, text="Select Participant", command=open_select_participant, font=("Helvetica", 20)).pack(pady=10)
    
    # Exit button at the bottom
    tk.Button(main_frame, text="Exit", command=close_app, font=("Helvetica", 10)).pack(pady=10)
    root.mainloop()

if __name__ == '__main__':
    create_main_gui()
