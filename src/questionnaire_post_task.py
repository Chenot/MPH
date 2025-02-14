import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import os

class CustomScale(tk.Canvas):
    def __init__(self, master, from_, to, length=400, variable=None, **kwargs):
        super().__init__(master, width=length, height=60, **kwargs)
        self.from_ = from_
        self.to = to
        self.length = length
        self.variable = variable if variable else tk.IntVar(value=-1)
        self.cursor = None
        self.bind("<Button-1>", self.click)
        self.bind("<B1-Motion>", self.drag)
        self.draw_scale()

    def draw_scale(self):
        # Draw the horizontal line
        self.create_line(10, 30, self.length - 10, 30, fill='black')

        # Draw the ticks
        for i in range(self.from_, self.to + 1, 5):
            x = 10 + (i - self.from_) * (self.length - 20) / (self.to - self.from_)
            if i % 25 == 0 or i == self.from_ or i == self.to:
                # Draw higher tick for 0,25,50,75,100
                self.create_line(x, 20, x, 40, fill='black', width=2)
            else:
                # Draw normal tick
                self.create_line(x, 25, x, 35, fill='black')

        # Draw cursor at initial position (leftmost point)
        if self.variable.get() == -1:
            initial_x = 10  # Starting position at 0
        else:
            initial_x = 10 + (self.variable.get() - self.from_) * (self.length - 20) / (self.to - self.from_)
        self.cursor = self.create_polygon(
            initial_x, 15, initial_x - 5, 25, initial_x + 5, 25, fill='red'
        )

    def click(self, event):
        self.move_cursor(event.x)

    def drag(self, event):
        self.move_cursor(event.x)

    def move_cursor(self, x):
        # Constrain x to the scale boundaries
        x = max(10, min(x, self.length - 10))
        # Move the cursor
        self.coords(
            self.cursor,
            x, 15,
            x - 5, 25,
            x + 5, 25
        )
        # Update variable
        value = self.from_ + (x - 10) * (self.to - self.from_) / (self.length - 20)
        self.variable.set(int(round(value)))

class QuestionnaireApp:
    def __init__(self, master, participant_info, completed_complex_task):
        self.master = master
        self.participant_info = participant_info
        self.completed_complex_task = completed_complex_task
        self.language = self.participant_info.get('language', 'English')

        # Set the title and fullscreen mode
        self.master.title("Questionnaire")
        self.master.attributes('-fullscreen', True)
        self.master.lift()
        self.master.focus_force()
        self.master.attributes('-topmost', True)
        self.master.after(100, lambda: self.master.attributes('-topmost', False))

        # Configuration for the questionnaire
        self.config = {
            'custom_questionnaire': {
                'type': 'slider',
                'points': 100,
                'headers': {
                    'English': ['Totally disagree', 'Totally agree'],
                    'French': ['Pas du tout d’accord', 'Tout à fait d’accord']
                },
                'instructions': {
                    'English': "Post-Task Questionnaire\n\nPlease rate the following items based on your experience:",
                    'French': "Questionnaire Post-Task\n\nVeuillez évaluer les éléments suivants en fonction de votre expérience :"
                }
            }
        }

        self.current_page = 0
        self.responses = {}
        self.sliders_moved = {}  # Track if scales have been moved

        # Load the custom questionnaire
        self.load_questionnaire('custom_questionnaire')

        # Navigation buttons at the bottom
        self.navigation_frame = tk.Frame(self.master)
        self.navigation_frame.pack(side=tk.BOTTOM, pady=20)

        # Initially disable the "Next" button
        self.next_button = tk.Button(
            self.navigation_frame, text="Next", state=tk.DISABLED, command=self.finish_questionnaire
        )
        self.next_button.pack(side="right", padx=10)

    def load_questionnaire(self, questionnaire_name):
        # Clear any existing content
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.navigation_frame:
                widget.destroy()

        # Load the CSV file for the questionnaire
        current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        csv_file = os.path.abspath(os.path.join(current_directory, '..', 'questionnaires', 'questionnaire_post-task.csv'))
        self.df = pd.read_csv(csv_file)

        # Get the configuration for this questionnaire
        self.current_config = self.config[questionnaire_name]

        # Create the UI for the questionnaire
        self.create_questionnaire_ui()

    def create_questionnaire_ui(self):
        # Frame for instructions
        self.instructions_frame = tk.Frame(self.master)
        self.instructions_frame.pack(pady=10)

        # Choose instructions text based on the language and questionnaire
        instructions_text = self.current_config['instructions'][self.language]
        instructions_label = tk.Label(
            self.instructions_frame, text=instructions_text, font=("Arial", 18), wraplength=1000
        )
        instructions_label.pack(anchor="w")

        # Frame for questions and responses
        self.questions_frame = tk.Frame(self.master)
        self.questions_frame.pack(pady=10, expand=True)

        # Center the questions vertically
        self.questions_frame.pack_propagate(False)
        self.questions_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Choose headers based on the language
        headers = self.current_config['headers'][self.language]

        # Add questions and response widgets (CustomScale)
        for index, row in self.df.iterrows():
            trial = row['trial']
            item_fr = row['item_fr']
            item_eng = row['item_eng']

            # Choose the appropriate question text based on language
            question_text = item_eng if self.language == 'English' else item_fr

            # Question label
            question_label = tk.Label(
                self.questions_frame, text=f"{question_text}", font=("Arial", 14),
                justify="left", anchor="w", wraplength=850
            )
            question_label.grid(row=index * 2 + 2, column=0, padx=40, pady=15, sticky="w")

            # Store the response variable with initial value -1
            self.responses[(self.current_page, trial)] = tk.IntVar(value=-1)
            self.sliders_moved[trial] = False  # Track if scale has been moved

            # CustomScale widget with from_=0 and to=100
            scale = CustomScale(
                self.questions_frame, from_=0, to=self.current_config['points'],
                length=400, variable=self.responses[(self.current_page, trial)]
            )
            scale.grid(row=index * 2 + 2, column=2, padx=20)

            # Start and end headers
            start_header = tk.Label(self.questions_frame, text=headers[0], font=("Arial", 12))
            start_header.grid(row=index * 2 + 2, column=1, padx=(100, 10), sticky="w")
            end_header = tk.Label(self.questions_frame, text=headers[1], font=("Arial", 12))
            end_header.grid(row=index * 2 + 2, column=3, padx=(10, 100), sticky="e")

            # Add a horizontal line below the item
            separator = tk.Frame(
                self.questions_frame, height=2, bd=1, relief=tk.SUNKEN, bg='black'
            )
            separator.grid(row=index * 2 + 3, column=0, columnspan=6, pady=5, sticky='we')

            # Bind the variable to detect changes
            self.responses[(self.current_page, trial)].trace_add(
                'write', lambda *args, trial=trial, scale=scale: self.on_scale_moved(trial, scale)
            )

    def on_scale_moved(self, trial, scale):
        """Mark the scale as moved and update its appearance."""
        self.sliders_moved[trial] = True
        # Optionally change the cursor color to indicate it's been moved
        scale.itemconfig(scale.cursor, fill='green')

        # Check if all scales have been moved to enable the "Next" button
        if all(self.sliders_moved.values()):
            self.next_button.config(state=tk.NORMAL)

    def validate_responses(self):
        """Ensure all questions have been answered."""
        for index, row in self.df.iterrows():
            trial = row['trial']
            response_value = self.responses[(self.current_page, trial)].get()

            # If the value is still at -1, which indicates not moved
            if response_value == -1:
                # Show error message based on the language
                if self.language == 'French':
                    messagebox.showwarning("Erreur", "Répondez à chaque item svp")
                else:
                    messagebox.showwarning("Error", "Please answer each item")
                return False  # Prevent moving forward
        return True  # All items have been answered

    def finish_questionnaire(self):
        # Validate responses before saving
        if not self.validate_responses():
            return

        # Save responses for the current page
        self.save_responses()
        self.master.destroy()  # Close the window when finished

    def save_responses(self):
        """Save the responses in a BIDS-compliant format."""
        participant_id = self.participant_info.get('participant_id', 'unknown')
        session_id = self.participant_info.get('current_session', '1')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        completed_complex_task = self.completed_complex_task

        data_to_save = []
        for index, row in self.df.iterrows():
            trial = row['trial']
            item_eng = row['item_eng']
            response = self.responses[(self.current_page, trial)].get()

            data_to_save.append({
                'trial': trial,
                'item': item_eng,
                'answer': response
            })

        # Create DataFrame
        df_responses = pd.DataFrame(data_to_save)

        # BIDS-compliant saving
        current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        bids_directory = os.path.abspath(os.path.join(current_directory, '..', 'BIDS_data'))

        # Create BIDS-compliant folder structure
        bids_sub_dir = os.path.join(bids_directory, f"sub-{participant_id}", f"ses-{session_id}")
        os.makedirs(bids_sub_dir, exist_ok=True)  # Ensure the directory exists

        # Define the BIDS filename
        bids_filename = f"sub-{participant_id}_ses-{session_id}_task-{completed_complex_task}_questionnaire_{timestamp}.csv"
        bids_file_path = os.path.join(bids_sub_dir, bids_filename)

        # Save the file in BIDS-compliant format
        df_responses.to_csv(bids_file_path, index=False)

# Main code to run the application
if __name__ == "__main__":
    participant_info = {
        'participant_id': '001',
        'participant_initials': 'JD',
        'participant_anonymized_id': 'X123',
        'language': 'French',
        'current_session': '1',
        'completed_tasks': 'MATB'
    }
    completed_complex_task = 'MATB'
    
    root = tk.Tk()
    app = QuestionnaireApp(root, participant_info, completed_complex_task)
    root.mainloop()
