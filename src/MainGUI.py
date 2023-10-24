from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
    
        # Load UI from 'src'
        uic.loadUi("src/mainwindow.ui", self)

        # Display UI
        self.show()

        # Quit app when 'Exit' QAction clicked in the toolbar
        self.actionClose.triggered.connect(qApp.quit)

        # Connect 'Select Input Fiie' button to handle_input_file_select()
        self.select_input_button.clicked.connect(self.handle_input_file_select)

        # Connect 'Select Output Directory' button to handle_output_directory_select()
        self.select_output_button.clicked.connect(self.handle_output_directory_select)

        # Connect 'Execute Action' button to handle_execute()
        self.execute_button.clicked.connect(self.handle_execute)

        # Initialize instance variables
        self.image_file = ""
        self.output_directory = ""
    
    def handle_input_file_select(self):
        print("handle_input_file_select() fucnction called...")

        options = QFileDialog.ReadOnly # Force user to only selected already exisitng files
        file_filter = "Images (*.jpg *.png)" # User can only select .jpg and .png file types

        # Store path of selected image file
        image_file, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", file_filter, options=options)

        if image_file:
            self.image_file = image_file
            self.input_file_label.setText(image_file) # Modify label to show path of selected image file
    
    def handle_output_directory_select(self):
        print("handle_output_directory_select() fucnction called...")

        options = QFileDialog.ShowDirsOnly # Show only existing user directories
        output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)

        if output_directory:
            self.output_directory = output_directory
            self.output_directory_label.setText(output_directory)
    
    def handle_execute(self):

        # Store user action selections from UI radio buttons
        selected_action = ""
        selected_algorithm = ""
        key = self.password_input.text()

        # Handle action selection
        if self.encrypt_radio_button.isChecked():
            selected_action = "encrypt"
        elif self.decrypt_radio_button.isChecked():
            selected_action = "decrypt"
        
        # Handle algorithm selection
        if self.algo1_radio_button.isChecked():
            selected_algorithm = "algo1"
        elif self.algo2_radio_button.isChecked():
            selected_algorithm = "algo2"
        elif self.algo3_radio_button.isChecked():
            selected_algorithm = "algo3"

        # Check for valid user input
        if self.image_file == "" or self.output_directory == "" or selected_action == "" or selected_algorithm == "" or key == "":
            QMessageBox.warning(self, "Error!", "Please fill in all form inputs.")
        else:
            # Handle action
            print("Valid user input. Proceed...")
        

        print("handle_execute() fucnction called with", selected_action, selected_algorithm)
        print(key)