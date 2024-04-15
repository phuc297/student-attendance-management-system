<<<<<<< HEAD:session_widget.py
from ui.ui_session import *
=======
import datetime
from ui.ui_lesson import *
>>>>>>> 5c754b8c457cd64151a4da85cb3e939a7412a93f:lesson_widget.py
from dal.lesson_dal import *
from bus.lesson_bus import *
from bus.class_bus import *
from bus.subject_bus import *
from bus.teacher_bus import *
from dto.lesson import * 
from dto.subject import *
from dto.teacher import *
import tkinter as tk
from tkinter import messagebox
from ui.ui_lesson import *



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
        list = lessonBUS.get_all()
        self.table_bh.setRowCount(list.__len__())
        tablerow=0
        list_gv = TeacherBUS.getList() 
        list_lop = ClassBUS.get_all()
        list_mh = subjectBUS.get_all()
        if list is not None:
            for row in list:
                self.table_bh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.table_bh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[3])))
                self.table_bh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[4])))
                self.table_bh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[5])))
                
                for rowlop in list_lop: 
                   if str(row[2]) == str(rowlop[0]): 
                      self.table_bh.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(rowlop[1])))
                    
                for rowmh in list_mh: 
                   if str(row[1]) == str(rowmh[0]): 
                      self.table_bh.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(rowmh[1])))
                      monhoc = rowmh[0]
                
                for rowm in list_mh: 
                   if str(monhoc) == str(rowm[0]): 
                       for rowgv in list_gv:
                           if str(rowgv[0]) == str(rowm[2]):
                              self.table_bh.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(rowgv[1])))

                       
                        
                tablerow += 1
        
    
    def tableEvent(self):
        cr = self.table_bh.currentRow()
        self.txt_maBH.setText(self.table_bh.item(cr, 0).text())
        self.txt_gioBD.setText(self.table_bh.item(cr, 1).text())
        self.txt_gioKT.setText(self.table_bh.item(cr, 2).text())
        
        date_str = self.table_bh.item(cr, 3).text()
        date = QtCore.QDate.fromString(date_str, "yyyy-MM-dd")
        self.ngayHoc.setDate(date)  
        
            
        text_from_table1 = self.table_bh.item(cr, 4).text()
        index1 = self.cb_lop.findText(text_from_table1)  
        if index1 != -1:  
          self.cb_lop.setCurrentIndex(index1)  
          
        self.txt_GV.setText(self.table_bh.item(cr, 6).text())
        
        
        text_from_table2 = self.table_bh.item(cr, 5).text()
        index2 = self.cb_mh.findText(text_from_table2)  
        if index2 != -1:  
          self.cb_mh.setCurrentIndex(index2)

        

        
       

    # def clear(self): 
    #     self.txt_maMH.clear() 
    #     self.txt_tenMH.clear()
    #     self.cb_gv.setCurrentIndex(0)
    
    
    def loadCB(self): 
        list_lop = ClassBUS.get_all()
        list_mh = subjectBUS.get_all()
        self.cb_mh.addItem("")
        self.cb_lop.addItem("")
        for rmh in list_mh: 
            self.cb_mh.addItem(rmh[1])
        for rl in list_lop: 
            self.cb_lop.addItem(rl[1])
        
            

    def addMH(self):
       if(self.txt_maBH.toPlainText() == ""):
         gioBD=self.txt_gioBD.toPlainText()
         gioKT=self.txt_gioKT.toPlainText()
         tenLop=self.cb_lop.currentText()
         tenMH=self.cb_mh.currentText()
         
         ngay = self.chonNgayHoc.date()
         day = datetime.date(ngay.year(), ngay.month(), ngay.day())

         maMH= subjectBUS.getIDSubject(tenMH)
         maLop=ClassBUS.getIdLop(tenLop)
        
         lession=buoiHoc(None,maMH,maLop,gioKT,gioBD,day)
         lessonBUS.add(lession)
         self.loadList()
          
       else: 
           messagebox.showinfo("", "Bạn cần làm mới trước khi thêm !")
          
    def clear (self):
       self.txt_gioBD.clear()
       self.txt_gioBD.clear()
       self.txt_gioKT.clear()
       self.txt_GV.clear()
       self.txt_maBH.clear()
       self.chonNgayHoc.clear()
    
    def editMH(self):
        if not self.table_bh.selectedItems():
            messagebox.showinfo("", "Vui lòng chọn một môn học để chỉnh sửa!")
            return
        else:

          tenMH = self.cb_mh.currentText()
          tenLop = self.cb_lop.currentText()
          maMH= subjectBUS.getIDSubject(tenMH)
          maLop=ClassBUS.getIdLop(tenLop)
          gv = self.txt_GV.toPlainText()
          ngay = self.chonNgayHoc.date()
          maBH=self.txt_maBH.toPlainText()
          day = datetime.date(ngay.year(), ngay.month(), ngay.day())
          
          gioBD=self.txt_gioBD.toPlainText()
          gioKT=self.txt_gioKT.toPlainText()

          list_gv = TeacherBUS.getList()
          
        
          if (self.txt_GV.toPlainText() == ""):
              messagebox.showinfo("", "Vui lònng không để trống giảng viên")
        
          else:
            current_row = self.table_bh.currentRow()
            print(current_row)
            for row in list_gv:
                if str(row[1]) == gv:
                    ten_gv = str(row[1])  # Lấy tên giáo viên từ danh sách
                         # Thực hiện hành động mong muốn, ví dụ: đổ tên giáo viên lên bảng
                    # Ví dụ:
                    self.table_bh.setItem(current_row, 6, QtWidgets.QTableWidgetItem(ten_gv))        
            lession= buoiHoc(maBH,maMH,maLop,gioBD,gioKT,day)
    
            lessonBUS.update_lession(lession)

            self.loadList()
            self.clear()
         

          
    
    
    def delete(self): 
       try: 
         maBH=int(self.txt_maBH.toPlainText())
         lessonBUS.delete(maBH)
         self.loadList()
         self.clear()
       except mysql.connector.IntegrityError as e:
           messagebox.showinfo("", "Bạn cần xóa các buổi học và điểm danh trước")


    
    def timKiem(self):
    #  Lấy từ khóa tìm kiếm từ combobox
         keyword = self.cb_timkiem.currentText()
    
    #  Xác định cột để tìm kiếm dựa trên lựa chọn của người dùng
         if keyword == "Tên môn học":
             column_index = 5  # Cột thứ 2: Tên môn học
         elif keyword == "Giảng viên":
             column_index = 6  # Cột thứ 3: Tên giảng viên
        

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