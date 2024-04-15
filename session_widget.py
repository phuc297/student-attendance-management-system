from ui.ui_session import *
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



class LessonWidget(Ui_Session):

    def __init__(self, page):
        self.setupUi(page)
        self.loadList()  
        self.loadCB()
        self.table_bh.itemClicked.connect(lambda: self.tableEvent())
        # self.btn_them.clicked.connect(lambda: self.addMH())
        # self.btn_lammoi.clicked.connect(lambda: self.clear())
        # self.btn_sua.clicked.connect(lambda: self.editMH())
        # self.btn_xoa.clicked.connect(lambda: self.delete())
        # self.btn_timkiem.clicked.connect(lambda: self.timKiem())
        
        
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
        
            

    # def addMH(self):
    #   if(self.txt_maMH.toPlainText() == ""):
    #     tenMH=self.txt_tenMH.toPlainText()
    #     gv = self.cb_gv.currentText()
    #     magv = None
    #     list_gv = TeacherBUS.getList()
    #     for row in list_gv: 
    #         if str(row[1]) == gv: 
    #             magv = int(row[0])
         
    #     mh = subject(None,tenMH,magv)
    #     subjectBUS.add(mh)
    #     self.loadList()
    #     self.clear()

      
    #   else: 
    #       messagebox.showinfo("", "Bạn cần làm mới trước khi thêm !")
          
    
    
    # def editMH(self):
    #    if not self.table_mh.selectedItems():
    #        messagebox.showinfo("", "Vui lòng chọn một môn học để chỉnh sửa!")
    #        return
    #    else:

    #      maMH = self.txt_maMH.toPlainText()
    #      tenMH = self.txt_tenMH.toPlainText()
    #      gv = self.cb_gv.currentText()
    #      magv = None
    #      list_gv = TeacherBUS.getList()
    #      for row in list_gv:
    #        if str(row[1]) == gv:
    #          magv = int(row[0])
        
    #      if (self.cb_gv.currentText() == ""):
    #          messagebox.showinfo("", "Vui lònng không để trống giảng viên")
        
    #      else:
    #       mh = subject(maMH, tenMH, magv)
    
    #       subjectBUS.update_subject(mh)

    #       self.loadList()
    #       self.clear()

          
    
    
    # def delete(self): 
    #   try: 
    #     maMH=int(self.txt_maMH.toPlainText())
    #     subjectBUS.delete(maMH)
    #     self.loadList()
    #     self.clear()
    #   except mysql.connector.IntegrityError as e:
    #       messagebox.showinfo("", "Bạn cần xóa các buổi học và điểm danh trước")


    
    # def timKiem(self):
    # # Lấy từ khóa tìm kiếm từ combobox
    #     keyword = self.cb_search.currentText()
    
    # # Xác định cột để tìm kiếm dựa trên lựa chọn của người dùng
    #     if keyword == "Tên môn học":
    #         column_index = 1  # Cột thứ 2: Tên môn học
    #     elif keyword == "Giảng viên":
    #         column_index = 2  # Cột thứ 3: Tên giảng viên
        

    #     search_text = self.txt_search.toPlainText().lower()

    #     for row in range(self.table_mh.rowCount()):
    #       item = self.table_mh.item(row, column_index)
    #       if item is not None:
    #         cell_text = item.text().lower()
    #         if search_text in cell_text:
    #             self.table_mh.setRowHidden(row, False)  # Hiện hàng nếu tìm thấy
    #         else:
    #             self.table_mh.setRowHidden(row, True)  

        
            
        



    def update(self):
        pass