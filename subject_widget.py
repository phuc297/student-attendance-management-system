from PyQt6 import QtWidgets
from ui.ui_subject import Ui_Subject
from bus.subject_bus import subjectBUS
from dto.subject import *

class SubjectWidget(Ui_Subject):
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()  
        self.table_mh.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(lambda: self.addMH())
        
    def loadList(self):
        list = subjectBUS.get_all()
        self.table_mh.setRowCount(list.__len__())
        tablerow=0
        if list is not None:
            for row in list:
                self.table_mh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.table_mh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.table_mh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))            
                tablerow += 1
    
    def tableEvent(self):
        cr = self.table_mh.currentRow()
        self.txt_maMH.setText(self.table_mh.item(cr, 0).text())
        self.txt_tenMH.setText(self.table_mh.item(cr, 1).text())
        self.txt_gv.setText(self.table_mh.item(cr, 2).text())
       
    

    def addMH(self):
        tenMH=self.txt_tenMH.toPlainText()
        gv = self.txt_gv.toPlainText()
        mh = subject(None,tenMH,gv)
        subjectBUS.add(mh)
        self.loadList()



    def update(self):
        pass