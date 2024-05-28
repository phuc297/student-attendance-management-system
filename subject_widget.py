from PyQt6 import QtWidgets
from ui.ui_subject import Ui_Subject
from bus.subject_bus import subjectBUS
from dto.subject import *
from bus.teacher_bus import TeacherBUS
from bus.class_bus import ClassBUS
import tkinter as tk
from tkinter import messagebox


class SubjectWidget(Ui_Subject):
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()  
        self.loadCB()
        self.table_mh.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(lambda: self.addMH())
        self.btn_refresh.clicked.connect(lambda: self.clear())
        self.btn_sua.clicked.connect(lambda: self.editMH())
        self.btn_xoa.clicked.connect(lambda: self.delete())
        self.btn_search.clicked.connect(lambda: self.timKiem())
        
        
    def loadList(self):
        list = subjectBUS.getInfo()
        self.table_mh.setRowCount(list.__len__())
        tablerow=0
        if list is not None:
            for row in list:
                self.table_mh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.table_mh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.table_mh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
                self.table_mh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[5])))
                     
                tablerow += 1
    
    def tableEvent(self):
        cr = self.table_mh.currentRow()
        self.txt_maMH.setText(self.table_mh.item(cr, 0).text())
        self.txt_tenMH.setText(self.table_mh.item(cr, 1).text())
        
        text_from_table1 = self.table_mh.item(cr, 2).text()
        index1 = self.cb_gv.findText(text_from_table1)  
        if index1 != -1:  
          self.cb_gv.setCurrentIndex(index1)  
        
        text_from_table2 = self.table_mh.item(cr, 3).text()
        index2 = self.cb_lop.findText(text_from_table2)  
        if index2 != -1:  
          self.cb_lop.setCurrentIndex(index2)  
        
       

    def clear(self): 
        self.txt_maMH.clear() 
        self.txt_tenMH.clear()
        self.cb_gv.setCurrentIndex(0)
        self.cb_lop.setCurrentIndex(0)
    
    
    def loadCB(self): 
        self.cb_search.addItem("Tên môn học")
        self.cb_search.addItem("Giảng viên")
        list_gv = TeacherBUS.getList(); 
        list_lop = ClassBUS.get_all()
        for rgv in list_gv: 
            self.cb_gv.addItem(rgv[1])
            
        for rlop in list_lop:
            self.cb_lop.addItem(rlop[1])
            

    def addMH(self):
      if(self.txt_maMH.toPlainText() == ""):
        tenMH=self.txt_tenMH.toPlainText()
        gv = self.cb_gv.currentText()
        magv = None
        malop = None
        list_gv = TeacherBUS.getList()
        for row in list_gv: 
            if str(row[1]) == gv: 
                magv = int(row[0])
        
        list_lop = ClassBUS.get_all()
        for row in list_lop:
            if str(row[1]) == self.cb_lop.currentText():
                malop = int(row[0])
        
        
        mh = subject(None,tenMH,magv,malop)
        subjectBUS.add(mh)
        self.loadList()
        self.clear()

      
      else: 
          messagebox.showinfo("", "Bạn cần làm mới trước khi thêm !")
          
    
    
    def editMH(self):
       if not self.table_mh.selectedItems():
           messagebox.showinfo("", "Vui lòng chọn một môn học để chỉnh sửa!")
           return
       else:

         maMH = self.txt_maMH.toPlainText()
         tenMH = self.txt_tenMH.toPlainText()
         gv = self.cb_gv.currentText()
         magv = None
         malop = None
         list_gv = TeacherBUS.getList()
         for row in list_gv:
           if str(row[1]) == gv:
             magv = int(row[0])
             
         list_lop = ClassBUS.get_all()
         for row in list_lop:
              if str(row[1]) == self.cb_lop.currentText():
                 malop = int(row[0])
        
         if (self.cb_gv.currentText() == "" or self.cb_lop.currentText() == ""  or self.txt_tenMH.toPlainText() == ""):
             messagebox.showinfo("", "Vui lònng không để trống thông tin")
        
         else:
          mh = subject(maMH, tenMH, magv, malop)
    
          subjectBUS.update_subject(mh)

          self.loadList()
          self.clear()
    
    def delete(self): 
        try: 
            if not self.table_mh.selectedItems():
                messagebox.showinfo("", "Vui lòng chọn một môn học để xóa!")
                return
            else:
                maMH=int(self.txt_maMH.toPlainText())
                if subjectBUS.delete(maMH) == True:
                    messagebox.showinfo("","Xóa thành công")
                    self.loadList()
                    self.clear()
                else:
                    messagebox.showinfo("","Xóa thất bại")
        except Exception as e:
                print(e)
                messagebox.showinfo("", "Bạn cần xóa các buổi học và điểm danh trước")


    
    def timKiem(self):
    # Lấy từ khóa tìm kiếm từ combobox
        keyword = self.cb_search.currentText()
    
    # Xác định cột để tìm kiếm dựa trên lựa chọn của người dùng
        if keyword == "Tên môn học":
            column_index = 1  # Cột thứ 2: Tên môn học
        elif keyword == "Giảng viên":
            column_index = 2  # Cột thứ 3: Tên giảng viên
        

        search_text = self.txt_search.toPlainText().lower()

        for row in range(self.table_mh.rowCount()):
          item = self.table_mh.item(row, column_index)
          if item is not None:
            cell_text = item.text().lower()
            if search_text in cell_text:
                self.table_mh.setRowHidden(row, False)  
            else:
                self.table_mh.setRowHidden(row, True)  

        
            
        



    def update(self):
        pass