import sys
import csv
import re
import os
from datetime import datetime
from PyQt5 import QtWidgets, QtCore, QtGui

# ------------------------------------------------------------
# PARSER FUNCTIONS
# ------------------------------------------------------------

def parse_range_params(param_str):
    param_str = param_str.strip("{}")
    params = {}
    parts = param_str.split(",")
    for part in parts:
        part = part.strip()
        if "=" in part:
            key, value = part.split("=", 1)
            key = key.strip()
            value = value.strip()
            try:
                value = int(value)
            except ValueError:
                pass
            params[key] = value
        else:
            params[part] = True
    return params

def parse_questionnaire_file(filename):
    """
    This parser returns:
      - pages: a list of pages; each page is a list of question dictionaries.
      - scales: a dictionary of scales.
    
    If the file contains explicit page markers (page: begin / page: end) then questions
    in between these markers are grouped on one page. Otherwise, each question is placed on its own page.
    """
    scales = {}
    pages = []       # list of pages (each page is a list of questions)
    questions = []   # if no explicit page markers are found, we collect questions here
    explicit_pages = False
    current_page = None
    current_question = None
    mode = None  # "question" or "scale"
    current_scale_name = None

    with open(filename, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            # Handle explicit page markers.
            if line.startswith("page:"):
                _, page_cmd = line.split(":", 1)
                page_cmd = page_cmd.strip()
                explicit_pages = True
                if page_cmd == "begin":
                    if current_question is not None:
                        current_page.append(current_question)
                        current_question = None
                    current_page = []
                elif page_cmd == "end":
                    if current_question is not None:
                        current_page.append(current_question)
                        current_question = None
                    if current_page is not None:
                        pages.append(current_page)
                        current_page = None
                continue

            # Switch to scale mode if needed.
            if line.startswith("scale:"):
                if mode == "question" and current_question is not None:
                    if explicit_pages:
                        current_page.append(current_question)
                    else:
                        questions.append(current_question)
                _, scale_name = line.split(":", 1)
                current_scale_name = scale_name.strip()
                scales[current_scale_name] = []
                mode = "scale"
                continue

            # Process a new question label.
            if line.startswith("l:"):
                if mode == "question" and current_question is not None:
                    if explicit_pages:
                        current_page.append(current_question)
                    else:
                        questions.append(current_question)
                mode = "question"
                current_question = {}
                current_question["label"] = line.split(":", 1)[1].strip()
                continue

            if line.startswith("t:"):
                if mode == "question" and current_question is not None:
                    t_val = line.split(":", 1)[1].strip()
                    current_question["type"] = t_val
                continue

            if line.startswith("q:"):
                if mode == "question" and current_question is not None:
                    current_question["question"] = line.split(":", 1)[1].strip()
                continue

            # Process options or extra lines.
            if line.startswith("-"):
                option_text = line[1:].strip()
                if mode == "scale":
                    m = re.match(r"\{score=(\d+)\}\s*(.*)", option_text)
                    if m:
                        score = int(m.group(1))
                        text = m.group(2)
                        scales[current_scale_name].append((score, text))
                    else:
                        scales[current_scale_name].append((None, option_text))
                elif mode == "question":
                    if "options" not in current_question:
                        current_question["options"] = []
                    current_question["options"].append(option_text)
                continue

            # For any other line (extra info)
            if mode == "question" and current_question is not None:
                if current_question.get("type", "") == "info":
                    current_question["question"] += "\n" + line.strip()
                continue

    if current_question is not None:
        if explicit_pages:
            if current_page is None:
                current_page = []
            current_page.append(current_question)
        else:
            questions.append(current_question)
    if explicit_pages and current_page is not None:
        pages.append(current_page)

    if not explicit_pages:
        pages = [[q] for q in questions]

    return pages, scales

# ------------------------------------------------------------
# CUSTOM WIDGET: GRID SCALE WITH FIXED COLUMN WIDTHS
# ------------------------------------------------------------

class GridScaleWidget(QtWidgets.QWidget):
    def __init__(self, label_id, items, scale_options, parent=None):
        super().__init__(parent)
        self.label_id = label_id
        self.items = items                  # List of item texts.
        self.scale_options = scale_options  # List of (score, text) tuples.
        self.button_groups = {}             # Maps each item to its QButtonGroup.
        self.row_widgets = {}
        self.initUI()

    def _create_hline(self, height):
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setLineWidth(1)
        line.setFixedHeight(height)
        return line

    def _create_vline(self, width):
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setLineWidth(1)
        line.setFixedWidth(width)
        return line

    def highlightRow(self, key):
        if key in self.row_widgets:
            for widget, orig_style in self.row_widgets[key]:
                new_style = re.sub(r'background-color\s*:\s*[^;]+;', '', orig_style)
                new_style += " background-color: #D3D3D3;"
                widget.setStyleSheet(new_style)

    def initUI(self):
        self.setStyleSheet("background-color: white;")
        num_options = len(self.scale_options)
        num_items = len(self.items)
        real_cols = 1 + num_options  
        total_cols = 2 * real_cols + 1  
        total_rows = 2 * num_items + 3

        if real_cols == 3:
            first_units = 9
            other_units = 3
        elif real_cols == 6:
            first_units = 9
            other_units = 2
        else:
            first_units = 9
            other_units = 2

        scale_factor = 80  
        fixed_first_width = first_units * scale_factor
        fixed_other_width = other_units * scale_factor
        separator_width = 2   
        separator_height = 2  

        total_width = (num_options + 2) * separator_width + fixed_first_width + num_options * fixed_other_width

        layout = QtWidgets.QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        top_border = self._create_hline(separator_height)
        layout.addWidget(top_border, 0, 0, 1, total_cols)

        for col in range(total_cols):
            if col % 2 == 0:
                vline = self._create_vline(separator_width)
                layout.addWidget(vline, 1, col)
            else:
                content_index = (col - 1) // 2
                if content_index == 0:
                    label = QtWidgets.QLabel("Item")
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setWordWrap(True)
                    label.setFixedWidth(fixed_first_width)
                    cell_style = "background-color: #444444; color: white; padding: 4px;"
                    label.setStyleSheet(cell_style)
                    layout.addWidget(label, 1, col)
                else:
                    option_index = content_index - 1
                    text = self.scale_options[option_index][1] if option_index < len(self.scale_options) else ""
                    label = QtWidgets.QLabel(text)
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setWordWrap(True)
                    label.setFixedWidth(fixed_other_width)
                    cell_style = "background-color: #444444; color: white; padding: 4px;"
                    label.setStyleSheet(cell_style)
                    layout.addWidget(label, 1, col)
        
        header_separator = self._create_hline(separator_height)
        layout.addWidget(header_separator, 2, 0, 1, total_cols)
        
        for i, item_text in enumerate(self.items):
            row_content = 2 * i + 3
            button_group = QtWidgets.QButtonGroup(self)
            self.button_groups[item_text] = button_group
            self.row_widgets[item_text] = []
            
            for col in range(total_cols):
                if col % 2 == 0:
                    vline = self._create_vline(separator_width)
                    layout.addWidget(vline, row_content, col)
                else:
                    content_index = (col - 1) // 2
                    if content_index == 0:
                        label = QtWidgets.QLabel(item_text)
                        label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        label.setWordWrap(True)
                        label.setFixedWidth(fixed_first_width)
                        cell_style = "background-color: white; padding: 4px;"
                        label.setStyleSheet(cell_style)
                        layout.addWidget(label, row_content, col)
                        self.row_widgets[item_text].append((label, cell_style))
                    else:
                        option_index = content_index - 1
                        container = QtWidgets.QWidget()
                        container.setFixedWidth(fixed_other_width)
                        h_layout = QtWidgets.QHBoxLayout(container)
                        h_layout.setContentsMargins(0, 0, 0, 0)
                        h_layout.addStretch()
                        radio = QtWidgets.QRadioButton()
                        radio.setStyleSheet("QRadioButton::indicator { width: 50px; height: 50px; }")
                        h_layout.addWidget(radio)
                        h_layout.addStretch()
                        container.setLayout(h_layout)
                        cell_style = "background-color: white; padding: 4px;"
                        container.setStyleSheet(cell_style)
                        layout.addWidget(container, row_content, col)
                        self.row_widgets[item_text].append((container, cell_style))
                        score = self.scale_options[option_index][0] if option_index < len(self.scale_options) else 0
                        button_group.addButton(radio, score)
            
            button_group.buttonClicked.connect(lambda _, key=item_text: self.highlightRow(key))
            
            if i < len(self.items) - 1:
                h_sep = self._create_hline(separator_height)
                layout.addWidget(h_sep, row_content + 1, 0, 1, total_cols)
        
        bottom_border = self._create_hline(separator_height)
        layout.addWidget(bottom_border, (2 * len(self.items) + 2), 0, 1, total_cols)
        
        for col in range(total_cols):
            layout.setColumnStretch(col, 0)
        
        self.setLayout(layout)
        self.setFixedWidth(total_width)

# ------------------------------------------------------------
# MAIN GUI CLASS USING PYQT5
# ------------------------------------------------------------

class QuestionnaireGUI(QtWidgets.QMainWindow):
    def __init__(self, questionnaire_file, participant_info):
        """
        :param questionnaire_file: Path to the questionnaire text file.
        :param participant_info: A dictionary with participant details.
        """
        super().__init__()
        self.questionnaire_file = questionnaire_file
        self.participant_info = participant_info
        self.setWindowTitle("Questionnaire")
        self.response_widgets = {}   # Maps question label to its widget (or button group, etc.)
        self.pages, self.scales = parse_questionnaire_file(questionnaire_file)
        # Create a list of page widgets.
        self.page_widgets = []
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)
        self.createPages()
        self.current_page_index = 0
        self.stack.setCurrentIndex(0)
        self.start_time = datetime.now()
        self.showMaximized()

    def createPages(self):
        for page_idx, page in enumerate(self.pages):
            page_widget = QtWidgets.QWidget()
            main_layout = QtWidgets.QVBoxLayout(page_widget)
            main_layout.setSpacing(40)
            main_layout.setContentsMargins(10, 10, 10, 10)
    
            for question in page:
                item_container = QtWidgets.QWidget()
                item_layout = QtWidgets.QVBoxLayout(item_container)
                item_layout.setSpacing(0)
                item_layout.setContentsMargins(0, 0, 0, 0)
    
                label_id = question.get("label", "unknown")
                qtype = question.get("type", "textline")
                qtext = question.get("question", "")
        
                if qtype == "info":
                    formatted_text = qtext.replace("\n", "<br>")
                    info_label = QtWidgets.QLabel(formatted_text)
                    info_label.setWordWrap(True)
                    info_label.setTextFormat(QtCore.Qt.RichText)
                    font = info_label.font()
                    font.setPointSize(18)
                    info_label.setFont(font)
                    item_layout.addWidget(info_label)
                    main_layout.addWidget(item_container)
                    continue

                question_label = QtWidgets.QLabel(qtext)
                question_label.setWordWrap(True)
                font = question_label.font()
                font.setBold(True)
                question_label.setFont(font)
                item_layout.addWidget(question_label)
    
                if qtype.startswith("textline"):
                    line_edit = QtWidgets.QLineEdit()
                    line_edit.textChanged.connect(self.checkAllAnswered)
                    item_layout.addWidget(line_edit)
                    self.response_widgets[label_id] = line_edit
        
                elif qtype.startswith("radio"):
                    container = QtWidgets.QWidget()
                    v_layout = QtWidgets.QVBoxLayout(container)
                    v_layout.setSpacing(0)
                    v_layout.setContentsMargins(0, 0, 0, 0)
                    button_group = QtWidgets.QButtonGroup(container)
                    if "options" in question:
                        for option in question["options"]:
                            rb = QtWidgets.QRadioButton(option)
                            button_group.addButton(rb)
                            v_layout.addWidget(rb)
                    container.setLayout(v_layout)
                    self.response_widgets[label_id] = button_group
                    button_group.buttonClicked.connect(self.checkAllAnswered)
                    item_layout.addWidget(container)
        
                elif qtype.startswith("scale"):
                    parts = qtype.split()
                    scale_options = []
                    if len(parts) > 1:
                        scale_id = parts[1]
                        scale_options = self.scales.get(scale_id, [])
                    else:
                        if "options" in question:
                            for opt in question["options"]:
                                m = re.match(r"\{score=(\d+)\}\s*(.*)", opt)
                                if m:
                                    score = int(m.group(1))
                                    text = m.group(2)
                                    scale_options.append((score, text))
                    if "options" in question and question["options"] and not question["options"][0].startswith("{score="):
                        grid_widget = GridScaleWidget(label_id, question["options"], scale_options)
                        for item, group in grid_widget.button_groups.items():
                            key = f"{label_id}: {item}"
                            self.response_widgets[key] = group
                            group.buttonClicked.connect(self.checkAllAnswered)
                        item_layout.addWidget(grid_widget)
                    else:
                        container = QtWidgets.QWidget()
                        v_layout = QtWidgets.QVBoxLayout(container)
                        v_layout.setSpacing(0)
                        v_layout.setContentsMargins(0, 0, 0, 0)
                        button_group = QtWidgets.QButtonGroup(container)
                        for score, text in scale_options:
                            rb = QtWidgets.QRadioButton(text)
                            button_group.addButton(rb, score)
                            v_layout.addWidget(rb)
                        container.setLayout(v_layout)
                        self.response_widgets[label_id] = button_group
                        button_group.buttonClicked.connect(self.checkAllAnswered)
                        item_layout.addWidget(container)
                    
                elif qtype.startswith("range"):
                    params = {}
                    if "options" in question and len(question["options"]) > 0:
                        params = parse_range_params(question["options"][0])
                    min_val = params.get("min", 0)
                    max_val = params.get("max", 10)
                    default = params.get("start", min_val)
                    
                    slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
                    slider.setMinimum(min_val)
                    slider.setMaximum(max_val)
                    slider.setValue(default)
                    slider.setTickInterval(1)
                    slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
                    
                    # Custom style sheet for the slider:
                    slider.setStyleSheet("""
                        QSlider::groove:horizontal {
                            border: 1px solid #bbb;
                            background: #eee;
                            height: 10px;
                            border-radius: 5px;
                        }
                        QSlider::sub-page:horizontal {
                            background: #66afe9;
                            border: 1px solid #66afe9;
                            height: 10px;
                            border-radius: 5px;
                        }
                        QSlider::handle:horizontal {
                            background: white;
                            border: 1px solid #5c5c5c;
                            width: 20px;
                            margin: -5px 0; /* Centers the handle on the groove */
                            border-radius: 10px;
                        }
                    """)
                    
                    left_text = params.get("left", "")
                    center_text = params.get("center", "")
                    right_text = params.get("right", "")
                    left_label = QtWidgets.QLabel(left_text)
                    center_label = QtWidgets.QLabel(center_text)
                    right_label = QtWidgets.QLabel(right_text)
                    left_label.setAlignment(QtCore.Qt.AlignLeft)
                    center_label.setAlignment(QtCore.Qt.AlignCenter)
                    right_label.setAlignment(QtCore.Qt.AlignRight)
                
                    container = QtWidgets.QWidget()
                    v_layout = QtWidgets.QVBoxLayout(container)
                    v_layout.setContentsMargins(0, 0, 0, 0)
                    v_layout.addWidget(slider)
                    labels_layout = QtWidgets.QHBoxLayout()
                    labels_layout.addWidget(left_label)
                    labels_layout.addStretch()
                    labels_layout.addWidget(center_label)
                    labels_layout.addStretch()
                    labels_layout.addWidget(right_label)
                    v_layout.addLayout(labels_layout)
                
                    self.response_widgets[label_id] = slider
                    item_layout.addWidget(container)
                
                    
                main_layout.addWidget(item_container)
    
            nav_layout = QtWidgets.QHBoxLayout()
            if len(self.pages) > 1:
                if page_idx > 0:
                    prev_btn = QtWidgets.QPushButton("Previous")
                    prev_btn.clicked.connect(self.goPrevious)
                    nav_layout.addWidget(prev_btn)
                if page_idx < len(self.pages) - 1:
                    next_btn = QtWidgets.QPushButton("Next")
                    next_btn.clicked.connect(self.goNext)
                    nav_layout.addWidget(next_btn)
                else:
                    self.submit_btn = QtWidgets.QPushButton("Submit")
                    self.submit_btn.clicked.connect(self.handleSubmit)
                    self.submit_btn.setEnabled(False)
                    nav_layout.addWidget(self.submit_btn)
            else:
                self.submit_btn = QtWidgets.QPushButton("Submit")
                self.submit_btn.clicked.connect(self.handleSubmit)
                self.submit_btn.setEnabled(False)
                nav_layout.addWidget(self.submit_btn)
            main_layout.addLayout(nav_layout)
            page_widget.setLayout(main_layout)
    
            scroll = QtWidgets.QScrollArea()
            scroll.setWidget(page_widget)
            scroll.setWidgetResizable(True)
            self.page_widgets.append(scroll)
            self.stack.addWidget(scroll)

    def goNext(self):
        if self.current_page_index < len(self.page_widgets) - 1:
            self.current_page_index += 1
            self.stack.setCurrentIndex(self.current_page_index)
        self.checkAllAnswered()

    def goPrevious(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1
            self.stack.setCurrentIndex(self.current_page_index)
        self.checkAllAnswered()

    def checkAllAnswered(self):
        all_answered = True
        for key, widget in self.response_widgets.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                if widget.text().strip() == "":
                    all_answered = False
                    break
            elif isinstance(widget, QtWidgets.QButtonGroup):
                if widget.checkedId() == -1:
                    all_answered = False
                    break
            elif isinstance(widget, QtWidgets.QSlider):
                if widget.value() == 0:
                    all_answered = False
                    break
        if hasattr(self, "submit_btn"):
            self.submit_btn.setEnabled(all_answered)

    def handleSubmit(self):
        responses = {}
        for key, widget in self.response_widgets.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                responses[key] = widget.text().strip()
            elif isinstance(widget, QtWidgets.QButtonGroup):
                responses[key] = widget.checkedId() if widget.checkedId() != -1 else None
            elif isinstance(widget, QtWidgets.QSlider):
                responses[key] = widget.value()

        time_end = datetime.now()
        time_start_str = self.start_time.strftime("%Y-%m-%d-%H-%M-%S")
        time_end_str = time_end.strftime("%Y-%m-%d-%H-%M-%S")
        responses["TIME_start"] = time_start_str
        responses["TIME_end"] = time_end_str

        final_responses = {}
        final_responses["participant_id"] = self.participant_info.get("participant_id", "")
        final_responses.update(responses)

        participant_id = self.participant_info.get("participant_id", "unknown")
        current_session = self.participant_info.get("current_session", "unknown")
        sub_str = f"sub-{participant_id.zfill(3)}"
        ses_str = f"ses-{current_session}"
        base_name = os.path.splitext(os.path.basename(self.questionnaire_file))[0]
        current_directory = os.path.dirname(os.path.abspath(__file__))
        bids_directory = os.path.abspath(os.path.join(current_directory, '..', 'BIDS_data'))
        output_folder = os.path.join(bids_directory, sub_str, ses_str)
        os.makedirs(output_folder, exist_ok=True)
        csv_filename = f"{sub_str}_{ses_str}_questionnaire_{base_name}.csv"
        output_path = os.path.join(output_folder, csv_filename)

        try:
            with open(output_path, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(final_responses.keys())
                writer.writerow(final_responses.values())
        except Exception as e:
            print(f"Error saving responses: {e}")

        # --- Set the flag to indicate the questionnaire is complete ---
        self.participant_info["questionnaire_completed"] = True
    
        self.close()

# ------------------------------------------------------------
# RUN THE QUESTIONNAIRE AS A FUNCTION
# ------------------------------------------------------------

def run_questionnaire(questionnaire_file, participant_info):
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    font = QtGui.QFont("Helvetica", 16)
    app.setFont(font)
    window = QuestionnaireGUI(questionnaire_file, participant_info)
    window.show()
    app.exec_()

# ------------------------------------------------------------
# MAIN FUNCTION (only runs if this script is executed directly)
# ------------------------------------------------------------

if __name__ == "__main__":
    participant_info = {
        'participant_id': '001',
        'current_session': '1',
        'language': 'English'
    }
    questionnaire_file = "arsq_fr.txt"  # adjust as needed for testing
    run_questionnaire(questionnaire_file, participant_info)
