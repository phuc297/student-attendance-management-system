import datetime
from ui.ui_session import *
from dal.sesson_dal import *
from bus.sesson_bus import *
from bus.class_bus import *
from bus.subject_bus import *
from bus.teacher_bus import *
from dto.lesson import *
from dto.subject import *
from dto.teacher import *
import tkinter as tk
from tkinter import messagebox
from PyQt6.QtCore import QDate


class LessonWidget(Ui_Session):

    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.loadCB()
        self.table_bh.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(lambda: self.addMH())
        self.btn_lammoi.clicked.connect(lambda: self.clear())
        self.btn_sua.clicked.connect(lambda: self.editMH())
        self.btn_xoa.clicked.connect(lambda: self.delete())
        self.btn_timkiem.clicked.connect(lambda: self.timKiem())

    def loadList(self):
        list = lessonBUS.getInfo()
        if list is not None:
            self.table_bh.setRowCount(list.__len__())
            tablerow = 0
            for row in list:
                self.table_bh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.table_bh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.table_bh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[4])))
                self.table_bh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[2])))
                self.table_bh.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[5])))
                self.table_bh.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[6])))
                self.table_bh.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[7])))
                self.table_bh.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[3])))

                tablerow += 1

    def tableEvent(self):
        cr = self.table_bh.currentRow()
        self.txt_maBH.setText(self.table_bh.item(cr, 0).text())
        
        self.txt_gioBD.setText(self.table_bh.item(cr, 4).text())
        self.txt_gioKT.setText(self.table_bh.item(cr, 5).text())
        self.txt_tuan.setText(self.table_bh.item(cr, 2).text())
        
        date_str = self.table_bh.item(cr, 7).text()
        try:
            date_obj = QDate.fromString(date_str, "yyyy-MM-dd")
            self.ngayHoc.setDate(date_obj)
        except ValueError:
            messagebox.showinfo("", "Invalid date format")

        text_from_table2 = self.table_bh.item(cr, 1).text()
        index2 = self.cb_mh.findText(text_from_table2)
        if index2 != -1:
            self.cb_mh.setCurrentIndex(index2)
            
    def loadCB(self):
        list_mh = subjectBUS.get_all()
        self.cb_mh.addItem("")
        for rmh in list_mh:
            self.cb_mh.addItem(rmh[1])
       

    def addMH(self):
        if self.txt_maBH.toPlainText() == "":
            gioBD = self.txt_gioBD.toPlainText()
            gioKT = self.txt_gioKT.toPlainText()
            tenMH = self.cb_mh.currentText()
            maMH = subjectBUS.getIDSubject(tenMH)
            ngay = self.ngayHoc.date()
            day = datetime.date(ngay.year(), ngay.month(), ngay.day())
            tuan = self.txt_tuan.toPlainText()

            lession = buoiHoc(None, maMH, gioKT, gioBD, day, tuan)
            lessonBUS.add(lession)
            self.loadList()

        else:
            messagebox.showinfo("", "Bạn cần làm mới trước khi thêm !")

    def clear(self):
        self.txt_gioBD.clear()
        self.txt_gioKT.clear()
        self.txt_maBH.clear()
        self.txt_tuan.clear()
        self.cb_mh.setCurrentIndex(0)
        self.ngayHoc.setDate(QDate.currentDate())

    def editMH(self):
        if not self.table_bh.selectedItems():
            messagebox.showinfo("", "Vui lòng chọn một môn học để chỉnh sửa!")
            return
        else:

            tenMH = self.cb_mh.currentText()
            maMH = subjectBUS.getIDSubject(tenMH)
            ngay = self.ngayHoc.date()
            maBH = self.txt_maBH.toPlainText()
            day = datetime.date(ngay.year(), ngay.month(), ngay.day())
            gioBD = self.txt_gioBD.toPlainText()
            gioKT = self.txt_gioKT.toPlainText()
            tuan = self.txt_tuan.toPlainText()


            if self.txt_gioBD.toPlainText() == "" or self.txt_gioKT.toPlainText() == "" or self.cb_mh.currentText() == "" or self.txt_tuan.toPlainText() == "" or self.ngayHoc.date() == "": 
                messagebox.showinfo("", "Vui lòng không để trống thông tin")

            else:
                
                lession = buoiHoc(maBH, maMH, gioBD, gioKT, day, tuan)

                lessonBUS.update_lession(lession)

                self.loadList()
                self.clear()

    def delete(self):
        try:
            if not self.table_bh.selectedItems():
                messagebox.showinfo("", "Vui lòng chọn một buổi học để xóa!")
                return
            else:
                maBH = int(self.txt_maBH.toPlainText())
                if lessonBUS.delete(maBH) == True:
                    messagebox.showinfo("", "Xóa thành công")
                    self.loadList()
                    self.clear()
                else:
                    messagebox.showinfo("", "Xóa thất bại")
        except mysql.connector.IntegrityError as e:
            messagebox.showinfo("", "Bạn cần xóa các buổi học và điểm danh trước")

    def timKiem(self):
        #  Lấy từ khóa tìm kiếm từ combobox
        keyword = self.cb_timkiem.currentText()

        #  Xác định cột để tìm kiếm dựa trên lựa chọn của người dùng
        if keyword == "Tên môn học":
            column_index = 1  # Cột thứ 2: Tên môn học
        elif keyword == "Giảng viên":
            column_index = 3  # Cột thứ 3: Tên giảng viên

        search_text = self.txt_timkiem.toPlainText().lower()

        for row in range(self.table_bh.rowCount()):
            item = self.table_bh.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                if search_text in cell_text:
                    self.table_bh.setRowHidden(row, False)  # Hiện hàng nếu tìm thấy
                else:
                    self.table_bh.setRowHidden(row, True)

    def update(self):
        pass
