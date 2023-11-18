from PyQt5.QtWidgets import QMessageBox

class SuccessMessage:
    def __init__(self, algorithm, action):
        self.algorithm = algorithm
        self.action = action
    
    def show_success_message(self):
        success_msg = QMessageBox()
        success_msg.setIcon(QMessageBox.Information)
        success_msg.setWindowTitle("Success")
        msg = self.algorithm + " " + self.action + " Successful!"
        success_msg.setText(msg)
        success_msg.exec()
