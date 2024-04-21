from ui.ui_student import *
from bus.student_bus import *
from trainning_widget import *
from PyQt6.QtWidgets import QWidget 
import cv2


class StudentWidget(Ui_Student):

    def __init__(self, page):
        super().__init__()
        self.setupUi(page)
        self.dataStudent = {}
        
        
        self.loadData()
        self.loadList()
        self.tbStudents.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(self.addStudent)
        self.btn_xoa.clicked.connect(self.deleteStudent)
        self.btn_sua.clicked.connect(self.updateStudent)
        self.btn_traindata.clicked.connect(self.openCapImageForm)
        

    def openCapImageForm(self):
        masv= self.txt_mssv.toPlainText()
        self.cap_image_form = TrainingWidget(masv)
        self.cap_image_form.show()

    def loadData(self):
        list = StudentBUS.getList()
        if list is not None:
            for row in list:
                student = Student(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
                self.dataStudent[student.masv] = student
    
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
        student = self.dataStudent[self.tbStudents.item(cr, 0).text()]
        self.txt_mssv.setText(student.masv)
        self.txt_hoten.setText(student.hoten)
        self.txt_namsinh.setText(student.malop)
        self.txt_cccd.setText(student.cmnd)
        self.cbx_gioitinh.setCurrentText(student.gioitinh)
        self.txt_email.setText(student.email)
        self.txt_sdt.setText(student.sdt)
        self.txt_namsinh.setText(student.ngaysinh)
        self.txt_malop.setText(student.malop)

    def addStudent(self, s):
        try:
            student = Student(
                0, 
                self.txt_hoten.toPlainText(), 
                self.txt_malop.toPlainText(),
                self.txt_cccd.toPlainText(), 
                self.cbx_gioitinh.currentIndex(), 
                self.txt_namsinh.toPlainText(),
                self.txt_email.toPlainText(),
                self.txt_sdt.toPlainText())

            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 100px;}")
            if StudentBUS.add(student) == True:
                dlg.setText("Thêm thành công")
                dlg.exec()
                self.loadList()
                self.loadData()
            else:
                dlg.setText("Thêm thất bại")
                dlg.exec()
        except Exception as e:
            print(e)

    def deleteStudent(self, s):
        try:
            cr = self.tbStudents.currentRow()
            masv = self.tbStudents.item(cr, 0).text()
            print(masv)
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 100px;}")
            if StudentBUS.delete(masv) == True:
                dlg.setText("Xóa thành công")
                dlg.exec()
                self.loadList()
                self.loadData()
            else:
                dlg.setText("Xóa thất bại")
                dlg.exec()
        except Exception as e:
            print(e)

    def updateStudent(self, s):
        try:
            student = Student(
                self.txt_mssv.toPlainText(), 
                self.txt_hoten.toPlainText(), 
                self.txt_malop.toPlainText(),
                self.txt_cccd.toPlainText(), 
                self.cbx_gioitinh.currentIndex(), 
                self.txt_namsinh.toPlainText(),
                self.txt_email.toPlainText(),
                self.txt_sdt.toPlainText())

            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 150px;}")
            if StudentBUS.update(student) == True:
                dlg.setText("Thay đổi thành công")
                dlg.exec()
                self.loadList()
                self.loadData()
            else:
                dlg.setText("Thay đổi thất bại")
                dlg.exec()
        except Exception as e:
            print(e)