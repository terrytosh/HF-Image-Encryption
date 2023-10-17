from MainGUI import MainGUI
from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = MainGUI()
    window.setWindowTitle("Image Encryption Tool")
    app.exec_()

if __name__ == '__main__':
    main()