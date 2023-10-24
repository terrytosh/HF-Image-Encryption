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
    
    # TODO: Implement this function
    def handle_input_file_select(self):
        print("handle_input_file_select() fucnction called...")
    
    # TODO: Implement this function
    def handle_output_directory_select(self):
        print("handle_output_directory_select() fucnction called...")
    
    # TODO: Implement this function
    def handle_execute(self):

        # Store user action selections from UI radio buttons
        selected_action = ""
        selected_algorithm = ""
        key = self.password_input.text()

        # Handle selected action input
        if self.encrypt_radio_button.isChecked():
            selected_action = "encrypt"
        elif self.decrypt_radio_button.isChecked():
            selected_action = "decrypt"
        
        # Handle selected algorithm input
        if self.algo1_radio_button.isChecked():
            selected_algorithm = "algo1"
        elif self.algo2_radio_button.isChecked():
            selected_algorithm = "algo2"
        elif self.algo3_radio_button.isChecked():
            selected_algorithm = "algo3"
        

        print("handle_execute() fucnction called with", selected_action, selected_algorithm)
        print(key)