import re
import tkinter as tk
from tkinter import messagebox
from ui.ui_teacher import *
from bus.account_bus import *
from bus.teacher_bus import *
from dto.teacher import Teacher
from PyQt6.QtWidgets import QMessageBox,QDateEdit
from PyQt6.QtCore import QDate
class TeacherWidget(Ui_Teacher):
   
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.loadCombobox()
        self.tableteacher.itemClicked.connect(lambda: self.tableEvent())
        self.btn_luu.clicked.connect(lambda: self.addgiangvien())
        self.btn_xoa.clicked.connect(lambda: self.deletegiangvien())
        self.btn_sua.clicked.connect(lambda: self.updategiangvien())
        self.btn_reset.clicked.connect(lambda: self.cleartxt())
        self.btn_timkiem.clicked.connect(lambda: self.timkiem())
        self.btn_xemtatca.clicked.connect(lambda: self.resettb())

    def resettb(self):
        self.txt_timkiem.clear()
        self.comboBoxtimkiem.setCurrentIndex(0)
        self.timkiem()
        
    def loadList(self):
        list = TeacherBUS.getList()
        if list is not None:
            self.tableteacher.setRowCount(len(list))
            tablerow=0
            for row in list:
                self.tableteacher.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableteacher.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableteacher.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableteacher.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tableteacher.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tableteacher.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tableteacher.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.tableteacher.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                tablerow += 1
                
    def loadCombobox(self):
        listtk = AccountBUS.getList()
        if listtk is not None:
            for row in listtk:
                # if TeacherBUS.checkAccount(str(row[0])) == False:
                    self.cbx_maTK.addItem(str(row[0]))

        
    def tableEvent(self):
            cr = self.tableteacher.currentRow()
            self.txt_id.setText(self.tableteacher.item(cr, 0).text())
            self.txt_hoten.setText(self.tableteacher.item(cr, 1).text())
            self.txt_cccd.setText(self.tableteacher.item(cr, 3).text())
            self.cbx_gioitinh.setCurrentText(self.tableteacher.item(cr, 2).text())
            self.txt_email.setText(self.tableteacher.item(cr, 5).text())
            self.txt_sdt.setText(self.tableteacher.item(cr, 6).text())
            self.cbx_maTK.setCurrentText(self.tableteacher.item(cr, 7).text())
            self.dateEdit.setDate(QDate.fromString(str(self.tableteacher.item(cr, 4).text()), "yyyy-MM-dd"))
            

    def check_email(self, email_text):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_text):
            return True
        else:
            return False

    def addgiangvien(self):
        if (self.txt_id.toPlainText()==""):
            
            hoTen = self.txt_hoten.toPlainText()
            gioitinh=self.cbx_gioitinh.currentText()
            cccd=self.txt_cccd.toPlainText()
            ngaysinh=self.dateEdit.date().toString("yyyy-MM-dd")
            email=self.txt_email.toPlainText()
            sdt = self.txt_sdt.toPlainText()
            maTK=self.cbx_maTK.currentText()

            if hoTen == "" or cccd == "" or email == "" or sdt == "" or self.cbx_maTK.currentIndex() == 0:
                messagebox.showwarning("", "Vui lòng nhập đầy đủ thông tin trước khi thêm!")
                return
            year = self.dateEdit.date().year()
            currentYear = QDate.currentDate().year()
            if self.dateEdit.date() < QDate(1900, 1, 1) or (currentYear - year) < 18:
                messagebox.showwarning("", "Vui lòng nhập năm sinh hợp lệ và trên 18 tuổi!")
                return
            if cccd.__len__() != 12 or not cccd.isdigit():
                messagebox.showwarning("", "Vui lòng nhập số chứng minh nhân dân đúng định dạng 12 số!")
                return
            if sdt.__len__() != 10 or not sdt.isdigit():
                messagebox.showwarning("", "Vui lòng nhập số điện thoại đúng định dạng 10 số!")
                return
            if not self.check_email(email):
                messagebox.showwarning("", "Email không đúng định dạng")
                return
            
            if TeacherBUS.add(hoTen, gioitinh, cccd, ngaysinh, email, sdt, maTK) == True:
                messagebox.showinfo("", "Thêm thành công!")
                self.loadList()
                self.cleartxt()
            else:
                messagebox.showwarning("", "Thêm thất bại!")
        else:
            messagebox.showwarning("Lỗi", "Vui lòng làm mới thông tin trước khi thêm!")


    def deletegiangvien(self):
        if (self.txt_id.toPlainText() == ""):
            messagebox.showwarning("Lỗi", "Vui lòng chọn giảng viên cần xóa!")
            return
        
        maGV=self.txt_id.toPlainText()
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa ?") == tk.YES:
            if TeacherBUS.delete(maGV) == True:
                    messagebox.showinfo("","Xóa thành công")
                    self.loadList()
                    self.cleartxt()
            else:
                messagebox.showwarning("","Xóa thất bại")
        else:
            return
        

    def updategiangvien(self):
        if (self.txt_id.toPlainText() != ""):
            maGV = self.txt_id.toPlainText()
            hoTen = self.txt_hoten.toPlainText()
            gioitinh = self.cbx_gioitinh.currentText()
            cccd = self.txt_cccd.toPlainText()
            ngaysinh = self.dateEdit.date().toString("yyyy-MM-dd")
            email = self.txt_email.toPlainText()
            sdt = self.txt_sdt.toPlainText()
            maTK = self.cbx_maTK.currentText()
        
            
            if hoTen == "" or cccd == "" or email == "" or sdt == "" or maTK == "":
                messagebox.showwarning("", "Vui lòng nhập đầy đủ thông tin trước khi thêm!")
                return
            year = self.dateEdit.date().year()
            currentYear = QDate.currentDate().year()
            if self.dateEdit.date() < QDate(1900, 1, 1) or (currentYear - year) < 18:
                messagebox.showwarning("", "Vui lòng nhập năm sinh hợp lệ và trên 18 tuổi!")
                return
            if cccd.__len__() != 12 or not cccd.isdigit():
                messagebox.showwarning("", "Vui lòng nhập số chứng minh nhân dân đúng định dạng 12 số!")
                return
            if sdt.__len__() != 10 or not sdt.isdigit():
                messagebox.showwarning("", "Vui lòng nhập số điện thoại đúng định dạng 10 số!")
                return
            if not self.check_email(email):
                messagebox.showwarning("", "Email không đúng định dạng")
                return
        
            giangvien = Teacher(maGV, hoTen, gioitinh, cccd, ngaysinh, email, sdt, maTK)
            if TeacherBUS.update(giangvien) == True:
                messagebox.showinfo("", "Sửa thành công!")
                self.loadList()
                self.cleartxt()
            else:
                messagebox.showwarning("", "Sửa thất bại!")
        else:
            messagebox.showwarning("Lỗi", "Vui lòng chọn thông tin cần sửa!")

    def timkiem(self):
        keyword = self.comboBoxtimkiem.currentText()
       

        if keyword == "Id":
             column_index = 0
        elif keyword == "Họ tên":
             column_index = 1
        elif keyword == "SĐT":
             column_index = 2

        if column_index is not None:
            search_text = self.txt_timkiem.toPlainText().lower()

        for row in range(self.tableteacher.rowCount()):
            item = self.tableteacher.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                # Kiểm tra xem ô có chứa từ khóa tìm kiếm hay không
                if search_text in cell_text:
                    self.tableteacher.setRowHidden(row, False)  # Hiện hàng nếu tìm thấy
                else:
                    self.tableteacher.setRowHidden(row, True)

    
    def cleartxt(self):
        self.txt_id.clear()
        self.txt_hoten.clear()
        self.dateEdit.clear()
        self.txt_cccd.clear()
        self.cbx_gioitinh.setCurrentIndex(0)
        self.cbx_maTK.setCurrentIndex(0)
        self.txt_email.clear()
        self.txt_sdt.clear()
        self.dateEdit.setDate(QDate.currentDate())
      
    