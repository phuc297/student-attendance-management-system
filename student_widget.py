from ui.ui_student import *
from bus.student_bus import *

class StudentWidget(Ui_Student):

    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tbStudents.itemClicked.connect(lambda: self.tableEvent())
        
    def loadList(self):
        list = StudentBUS.getList()
        self.tbStudents.setRowCount(list.__len__())
        tablerow = 0
        if list is not None:
            for row in list:
                self.tbStudents.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbStudents.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tbStudents.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tbStudents.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tbStudents.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tbStudents.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tbStudents.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.tbStudents.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                tablerow += 1
    
    def tableEvent(self):
        cr = self.tbStudents.currentRow()
        self.txt_hoten.setText(self.tbStudents.item(cr, 1).text())
        self.txt_namsinh.setText(self.tbStudents.item(cr, 2).text())
        self.txt_cccd.setText(self.tbStudents.item(cr, 3).text())
        self.cbx_gioitinh.setCurrentText(self.tbStudents.item(cr, 4).text())
        self.txt_email.setText(self.tbStudents.item(cr, 5).text())
        self.txt_sdt.setText(self.tbStudents.item(cr, 6).text())
        self.txt_diachi.setText(self.tbStudents.item(cr, 7).text())

    def update(self):
        pass