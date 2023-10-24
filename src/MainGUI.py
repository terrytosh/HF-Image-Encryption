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
        print("handle_execute() fucnction called...")