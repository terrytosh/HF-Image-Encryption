from ActionHandler import ActionHandler
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
        self.output_file = ""
        self.output_directory = ""
        self.selected_action = ""
        self.selected_algorithm = ""
        self.key = ""
    
    def handle_input_file_select(self):
        # print("handle_input_file_select() fucnction called...")

        options = QFileDialog.ReadOnly # Force user to only selected already exisitng files
        file_filter = "Images (*.jpg *.png)" # User can only select .jpg and .png file types

        # Store path of selected image file
        self.image_file, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", file_filter, options=options)

        if self.image_file:
            self.input_file_label.setText(self.image_file) # Modify label to show path of selected image file
    
    def handle_output_directory_select(self):
        # print("handle_output_directory_select() fucnction called...")

        options = QFileDialog.ShowDirsOnly # Show only existing user directories
        self.output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)

        if self.output_directory:
            self.output_directory_label.setText(self.output_directory)
    
    def handle_execute(self):

        self.key = self.password_input.text()
        self.output_file = self.output_file_name_input.text()

        # Handle action selection
        if self.encrypt_radio_button.isChecked():
            self.selected_action = "Encryption"
        elif self.decrypt_radio_button.isChecked():
            self.selected_action = "Decryption"
        
        # Handle algorithm selection
        if self.xor_radio_button.isChecked():
            self.selected_algorithm = "XOR"
        elif self.pixel_shuffling_radio_button.isChecked():
            self.selected_algorithm = "Pixel Shuffling"
        elif self.aes_radio_button.isChecked():
            self.selected_algorithm = "AES"
        elif self.rsa_radio_button.isChecked():
            self.selected_algorithm = "RSA"
        elif self.des_radio_button.isChecked():
            self.selected_algorithm = "3DES"

        # Check for valid user input
        if self.image_file == "" or self.output_directory == "" or self.selected_action == "" or self.selected_algorithm == "" or self.key == "" or self.output_file == "":
            QMessageBox.warning(self, "Error!", "Please fill in all form inputs.")
        else:
            action_handler = ActionHandler(self.image_file, self.output_directory, self.selected_action, self.selected_algorithm, self.key, self.output_file)
            if self.selected_action == "Encryption":
                action_handler.handle_encryption()
            elif self.selected_action == "Decryption":
                action_handler.handle_decryption()
