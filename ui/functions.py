from ui.settings import *
from PyQt6 import QtWidgets 

class UIFunctions():
    def selectMenu():
        return Settings.MENU_SELECTED_STYLESHEET
    def deselectMenu():
        return Settings.MENU_HOVER_STYLESHEET
    
    def resetStyle(window, widget):
        for w in window.sideMenu.findChildren(QtWidgets.QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu())