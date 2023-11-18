from datetime import datetime
import os
from PyQt5.QtWidgets import QMessageBox

class DataLog:
    def __init__(self, image, action, algorithm, output_dir, output_file):
        self.image = image
        self.action = action
        self.algorithm = algorithm
        self.output_dir = output_dir
        self.output_file = output_file
        self.data_log_entry = ""
        self.data_log_file_path = "datalog.txt"
        # # Create the directory if it doesn't exist
        # os.makedirs(os.path.dirname(self.data_log_file_path), exist_ok=True)
    
    def build_data_log_entry(self):
        current_datetime = datetime.now()
        formatted_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        file_name = os.path.basename(self.image)

        if (self.action == "Encryption"):
            action = "encrypted"
        if (self.action == "Decryption"):
            action = "decrypted"

        self.data_log_entry += file_name + " " + action + " with " + self.algorithm + " saved as " + self.output_file + " to " + self.output_dir + " on " + formatted_date_time

    def write_entry_to_file(self):
        self.build_data_log_entry()
        print(self.data_log_entry)
        try:
            with open(self.data_log_file_path, 'a') as file:
                file.write(self.data_log_entry + '\n')
        except Exception as e:
            failed_msg = QMessageBox()
            failed_msg.setIcon(QMessageBox.Information)
            failed_msg.setWindowTitle("Error")
            msg = "Failed writing entry to data log..."
            failed_msg.setText(msg)
            failed_msg.exec()