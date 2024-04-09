from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import os
from ui import *
from menu import *

class MainProgram(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_login.clicked.connect(self.openMainMenu)
    
    def openMainMenu(self):
        self.window = QMainWindow()
        self.ui_menu = MenuForm()
        self.ui_menu.setupUi(self.window)
        self.ui_menu.update()
        self.hide()
        self.window.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainProgram()
    sys.exit(app.exec())

