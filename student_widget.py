import re
from ui.ui_student import *
from bus.student_bus import *
from bus.class_bus import *
from PyQt6.QtWidgets import QMainWindow
from ui.ui_student_image import *
import tkinter as tk
from tkinter import messagebox
from trainning_widget import *
from PyQt6.QtWidgets import QWidget 
import cv2
import subprocess
from PyQt6.QtCore import QDate
import trainning_widget


class StudentWidget(Ui_Student):

    def __init__(self, page):
        super().__init__()
        self.setupUi(page)
        self.dataStudent = {}
        self.listclass = ClassBUS.get_all()
        self.loadData()
        self.loadList()
        self.loadListClass()
        self.btn_reset.clicked.connect(lambda: self.resetStudent())
        self.tbStudents.itemClicked.connect(lambda: self.tableStudentEvent())
        self.tbClass.itemClicked.connect(lambda: self.tableClassEvent())
        self.btn_them.clicked.connect(self.addStudent)
        self.btn_xoa.clicked.connect(self.deleteStudent)
        self.btn_sua.clicked.connect(self.updateStudent)
        self.btn_themlop.clicked.connect(lambda: self.addClass())
        self.btn_xoalop.clicked.connect(lambda: self.deleteClass())
        self.btnViewInfo.clicked.connect(self.openCapImageForm)
        self.btn_traindata.clicked.connect(self.trainData)
        self.txt_malop.textChanged.connect(self.malopChange)
        self.btn_resetlop.clicked.connect(lambda: self.resetLop())
        self.btn_sualop.clicked.connect(lambda: self.updateClass())
        self.btn_resetsinhvien.clicked.connect(lambda: self.resettbStudent())
        self.btn_tksinhvien.clicked.connect(lambda: self.searchStudent())
        self.txt_tklop.textChanged.connect(lambda: self.searchClass())


    def openCapImageForm(self):
        if self.txt_mssv != None:
            self.cap_image_form = trainning_widget.TrainingWidget(self.txt_mssv.toPlainText())
            self.cap_image_form.show()

    def loadData(self):
        list = StudentBUS.getList()
        if list is not None:
            for row in list:
                student = Student(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
                self.dataStudent[student.masv] = student        
    
    def loadList(self):
        list = StudentBUS.getList()
        if list is not None:
            self.tbStudents.setRowCount(list.__len__())
            tablerow = 0
            for row in list:
                self.tbStudents.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbStudents.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tbStudents.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tbStudents.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[7])))
                self.tbStudents.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tbStudents.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tbStudents.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tbStudents.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[6])))
                tablerow += 1
    
    def tableStudentEvent(self):
        cr = self.tbStudents.currentRow()
        self.txt_mssv.setText(str(self.tbStudents.item(cr, 0).text()))
        self.txt_hoten.setText(str(self.tbStudents.item(cr, 1).text()))
        tenLop = ClassBUS.getTenLop(str(self.tbStudents.item(cr, 2).text()))
        if tenLop is not None:
            self.cbx_lophoc.setCurrentText(str(tenLop))
        else:
            self.cbx_lophoc.setCurrentIndex(0)
        self.dateEdit.setDate(QDate.fromString(str(self.tbStudents.item(cr, 5).text()), "yyyy-MM-dd"))
        self.txt_cccd.setText(str(self.tbStudents.item(cr, 3).text()))
        self.cbx_gioitinh.setCurrentText(str(self.tbStudents.item(cr, 4).text()))
        
        self.txt_email.setText(str(self.tbStudents.item(cr, 6).text()))
        self.txt_sdt.setText(str(self.tbStudents.item(cr, 7).text()))
        
        
    def loadListClass(self):
        if self.listclass is not None:
            self.tbClass.clearContents()
            self.tbClass.setRowCount(self.listclass.__len__())
            tablerow = 0
            for row in self.listclass:
                self.tbClass.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbClass.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                tablerow += 1
            for row in self.listclass:
                self.cbx_lophoc.addItem(row[1])
        else :
            print("Không có dữ liệu")

    def tableClassEvent(self):
        cr = self.tbClass.currentRow()
        cls = self.tbClass.item(cr, 0).text()
        self.txt_malop.setText(str(cls[0]))
        
    def malopChange(self):
        text = self.txt_malop.toPlainText()
        if text is None or text == "":
            self.txt_tenlop.setText("")
        else:
            self.txt_tenlop.setText(ClassBUS.getTenLop(text))
    
    def searchStudent(self):
        selected_text = self.cbx_tksinhvien.currentText()
        column_index = None
        
        if selected_text == "Mã SV":
            column_index = 0
        elif selected_text == "Họ tên":
            column_index = 1
        elif selected_text == "Mã lớp":
            column_index = 2

        if column_index is not None:
            search_text = self.txt_tksinhvien.toPlainText()
            
        for row in range(self.tbStudents.rowCount()):
            item = self.tbStudents.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                if search_text.lower() in cell_text:
                    self.tbStudents.setRowHidden(row, False)
                else:
                    self.tbStudents.setRowHidden(row, True)
                    
    def searchClass(self):
        selected_text = self.cbx_tklophoc.currentText()
        if selected_text == "Mã lớp":
            column_index = 0
        elif selected_text == "Tên lớp":
            column_index = 1

        if column_index is not None:
            search_text = self.txt_tklop.toPlainText()
            
        for row in range(self.tbClass.rowCount()):
            item = self.tbClass.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                if search_text.lower() in cell_text:
                    self.tbClass.setRowHidden(row, False)
                else:
                    self.tbClass.setRowHidden(row, True)
                    
    def addClass(self):
        try:
            if not self.txt_malop.toPlainText() == "":
                messagebox.showwarning("", "Vui lòng làm mới trước khi thêm!")
                return
            
            if self.txt_tenlop.toPlainText() == "" or self.txt_tenlop.toPlainText() == "":
                messagebox.showwarning("", "Vui lòng nhập tên lớp trước khi thêm!")
                return

            if ClassBUS.add(str(self.txt_tenlop.toPlainText())) == True:
                messagebox.showinfo("","Thêm thành công")
                self.loadListClass()
                self.resetLop()
            else:
                messagebox.showerror("Thêm thất bại")
                
        except Exception as e:
            print(e)
            
    def deleteClass(self):
        try:
            if not self.tbClass.selectedItems():
                messagebox.showwarning("", "Vui lòng chọn một lớp để xóa!")
                return
            else:
                cr = self.tbClass.currentRow()
                malop = self.tbClass.item(cr, 0).text()
                if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa ?") == tk.YES:
                    if ClassBUS.delete(malop) == True:
                        messagebox.showinfo("","Xóa thành công")
                        self.listclass = ClassBUS.get_all()
                        self.loadListClass()
                        self.resetLop()
                    else:
                        messagebox.showerror("","Xóa thất bại")
                else:
                    return
        except Exception as e:
            print(e)
            
    def updateClass(self):
        try:
            if not self.tbClass.selectedItems():
                messagebox.showwarning("", "Vui lòng chọn lớp để chỉnh sửa!")
                return
            
            cls = Class_DTO(
                self.txt_malop.toPlainText(),
                self.txt_tenlop.toPlainText())
            
            if ClassBUS.update(cls) == True:
                messagebox.showinfo("","Cập nhật thành công")
                self.listclass = ClassBUS.get_all()
                self.loadListClass()
                self.resetLop()
            else:
                messagebox.showerror("","Cập nhật thất bại")
        except Exception as e:
            print(e)
    
    def resetLop(self):
        self.tbClass.clearSelection()
        self.txt_malop.setText("")
        self.txt_tklop.setText("")
        
    def resettbStudent(self):
        self.cbx_tksinhvien.setCurrentIndex(0)
        self.txt_tksinhvien.setText("")
        self.searchStudent()
        
    def resetStudent(self):
        self.tbStudents.clearSelection()
        self.txt_mssv.setText("")
        self.txt_hoten.setText("")
        self.cbx_lophoc.setCurrentIndex(0)
        self.txt_cccd.setText("")
        self.cbx_gioitinh.setCurrentIndex(0)
        self.dateEdit.setDate(QDate.currentDate())
        self.txt_email.setText("")
        self.txt_sdt.setText("")
        
    def check_email(self, email_text):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_text):
            return True
        else:
            return False
            
    def addStudent(self):
        try:
            if not self.txt_mssv.toPlainText() == "":
                messagebox.showwarning("", "Vui lòng làm mới trước khi thêm!")
                return
            if self.txt_hoten.toPlainText() == "" or self.txt_cccd.toPlainText() == "" or self.txt_email.toPlainText() == "" or self.txt_sdt.toPlainText() == "" or self.cbx_lophoc.currentIndex() == 0 :
                messagebox.showwarning("", "Vui lòng nhập đầy đủ thông tin trước khi thêm!")
                return
            year = self.dateEdit.date().year()
            currentYear = QDate.currentDate().year()
            if self.dateEdit.date() < QDate(1900, 1, 1) or (currentYear - year) < 18:
                messagebox.showwarning("", "Vui lòng nhập năm sinh hợp lệ và trên 18 tuổi!")
                return
            if self.txt_cccd.toPlainText().__len__() != 12 or not self.txt_cccd.toPlainText().isdigit():
                messagebox.showwarning("", "Vui lòng nhập số chứng minh nhân dân đúng định dạng 12 số!")
                return
            if self.txt_sdt.toPlainText().__len__() != 10 or not self.txt_sdt.toPlainText().isdigit():
                messagebox.showwarning("", "Vui lòng nhập số điện thoại đúng định dạng 10 số!")
                return
            if not self.check_email(self.txt_email.toPlainText()):
                messagebox.showwarning("", "Email không đúng định dạng")
                return
            
            student = Student(
                0, 
                self.txt_hoten.toPlainText(), 
                ClassBUS.getIdLop(self.cbx_lophoc.currentText()),
                self.txt_cccd.toPlainText(), 
                self.cbx_gioitinh.currentText(), 
                self.dateEdit.date().toString("yyyy-MM-dd"),
                self.txt_email.toPlainText(),
                self.txt_sdt.toPlainText())

            if StudentBUS.add(student) == True:
                messagebox.showinfo("","Thêm thành công")
                self.loadList()
                self.loadData()
                self.resetStudent()
            else:
                messagebox.showerror("","Thêm thất bại")
        except Exception as e:
            print(e)

    def deleteStudent(self):
        try:
            if not self.tbStudents.selectedItems():
                messagebox.showwarning("", "Vui lòng chọn một sinh viên để xóa!")
                return
        
            masv = self.tbStudents.item(self.tbStudents.currentRow(), 0).text()
            if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa ?") == tk.YES:
                if StudentBUS.delete(masv) == True:
                    messagebox.showinfo("","Xóa thành công")
                    self.loadList()
                    self.loadData()
                    self.resetStudent()
                else:
                    messagebox.showerror("","Xóa thất bại")
            else:
                return
                
        except Exception as e:
            print(e)

    def updateStudent(self):
        try:
            if not self.tbStudents.selectedItems():
                messagebox.showwarning("", "Vui lòng chọn học sinh để chỉnh sửa!")
                return
            if self.txt_hoten.toPlainText() == "" or self.txt_cccd.toPlainText() == "" or self.txt_email.toPlainText() == "" or self.txt_sdt.toPlainText() == "" or self.cbx_lophoc.currentIndex() == 0 :
                messagebox.showwarning("", "Vui lòng nhập đầy đủ thông tin trước khi chỉnh sửa!")
                return
            year = self.dateEdit.date().year()
            currentYear = QDate.currentDate().year()
            if self.dateEdit.date() < QDate(1900, 1, 1) or (currentYear - year) < 18:
                messagebox.showwarning("", "Vui lòng nhập năm sinh hợp lệ và trên 18 tuổi!")
                return
            if self.txt_cccd.toPlainText().__len__() != 12 or not self.txt_cccd.toPlainText().isdigit():
                messagebox.showwarning("", "Vui lòng nhập số chứng minh nhân dân đúng định dạng 12 số!")
                return
            if self.txt_sdt.toPlainText().__len__() != 10 or not self.txt_sdt.toPlainText().isdigit():
                messagebox.showwarning("", "Vui lòng nhập số điện thoại đúng định dạng 10 số!")
                return
            if not self.check_email(self.txt_email.toPlainText()):
                messagebox.showwarning("", "Email không đúng định dạng")
                
            maLop = ClassBUS.getIdLop(self.cbx_lophoc.currentText())
            student = Student(
                self.txt_mssv.toPlainText(), 
                self.txt_hoten.toPlainText(), 
                maLop,
                self.txt_cccd.toPlainText(), 
                self.cbx_gioitinh.currentText(), 
                self.dateEdit.date().toString("yyyy-MM-dd"),
                self.txt_email.toPlainText(),
                self.txt_sdt.toPlainText())
            if StudentBUS.update(student) == True:
                messagebox.showinfo("","Chỉnh sửa thành công")
                self.loadList()
                self.loadData()
            else:
                messagebox.showerror("","Chỉnh sửa thất bại")
        except Exception as e:
            print(e)

    def viewInfo(self):
        cr = self.tbStudents.currentRow()
        if self.tbStudents.item(cr, 0) != None:
            self.newwindow = QMainWindow()
            self.ui_info = Ui_StudentImage()
            self.ui_info.setupUi(self.newwindow)
            self.newwindow.show()

    def trainData(self):
        try:
            shutil.rmtree('face\Dataset\FaceData\processed')
        except Exception as e:
            print(f'Failed to delete directory: {e}')

        try:
            os.mkdir('face\Dataset\FaceData\processed')
        except Exception as e:
            print(f'Failed to delete directory: {e}')

        arg1 = "src/align_dataset_mtcnn.py"
        arg2 ="Dataset/FaceData/raw"
        arg3 = "Dataset/FaceData/processed"
        arg4 = "--image_size"
        arg5 = "160"
        arg6 = "--margin"
        arg7 = "32"
        arg8 = "--random_order"
        arg9 = "--gpu_memory_fraction"
        arg10 ="0.25"

        # Run the called script with arguments
        subprocess.run(['cd', 'face', '&&', 'python', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10],shell=True)


        arg1 = "src/classifier.py"
        arg2 = "TRAIN"
        arg3 = "Dataset/FaceData/processed"
        arg4 = "Models/20180402-114759.pb"
        arg5 = "Models/facemodel.pkl"
        arg6 = "--batch_size"
        arg7 = "1000"

        # Run the called script with arguments
        subprocess.run(['cd', 'face', '&&', 'python', arg1, arg2, arg3, arg4, arg5, arg6, arg7],shell=True)
            