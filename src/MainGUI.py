from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
    
        # Load UI from 'src'
        uic.loadUi("src/mainwindow.ui", self)

        # Display UI
        self.show()