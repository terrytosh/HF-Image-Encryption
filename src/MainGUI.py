from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
    
        # Load 'testgui.ui' UI from 'src'
        uic.loadUi("src/testgui.ui", self)

        # Display 'testgui.ui'
        self.show()