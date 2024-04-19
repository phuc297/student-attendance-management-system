from ui.ui_class import *
from bus.class_bus import *

class ClassWidget(Ui_Class):

    def __init__(self, page):
        self.setupUi(page)
        self.data = {}
        self.loadData()
        self.loadList()
        
    def loadData(self):
        pass
    
    def loadList(self):
        list = ClassBUS.get_all()
        self.tbClass.setRowCount(list.__len__())
        tablerow=0
        if list is not None:
            for row in list:
                self.tbClass.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbClass.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                tablerow += 1

    def tableEvent(self):
        pass

    def addStudent(self, s):
        pass

    def deleteStudent(self, s):
        pass

    def updateStudent(self, s):
        pass