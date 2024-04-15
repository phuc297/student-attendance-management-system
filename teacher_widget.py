from ui.ui_teacher import *
from bus.teacher_bus import *
from dto.teacher import Teacher
from PyQt6.QtWidgets import QMessageBox
class TeacherWidget(Ui_Teacher):
   
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tableteacher.itemClicked.connect(lambda: self.tableEvent())
        self.btn_luu.clicked.connect(lambda: self.addgiangvien(page))
        self.btn_xoa.clicked.connect(lambda: self.deletegiangvien(page))
        self.btn_sua.clicked.connect(lambda: self.updategiangvien(page))
        self.btn_reset.clicked.connect(lambda: self.cleartxt())
        self.btn_timkiem.clicked.connect(lambda: self.timkiem())
        self.btn_xemtatca.clicked.connect(lambda: self.loadList())

    def loadList(self):
        list = TeacherBUS.getList()
       
        self.tableteacher.setRowCount(len(list))

        tablerow=0
        if list is not None:
            for row in list:
                self.tableteacher.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableteacher.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableteacher.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))        
                tablerow += 1
    

    def tableEvent(self):
        cr = self.tableteacher.currentRow()
        self.txt_id.setText(self.tableteacher.item(cr, 0).text())
        self.txt_hoten.setText(self.tableteacher.item(cr, 1).text())
        self.txt_sdt.setText(self.tableteacher.item(cr, 2).text())

    def addgiangvien(self,page):
        if (self.txt_id.toPlainText()==""):
        
            hoTen = self.txt_hoten.toPlainText()
            SDT = self.txt_sdt.toPlainText()

            # Kiểm tra xem các trường dữ liệu có bị thiếu không
            if not hoTen.strip() or not SDT.strip():
                QMessageBox.warning(page, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
                return

            giangvien = Teacher(None, hoTen, SDT)
            TeacherBUS.addlist(giangvien)
            self.loadList()
        else:
            QMessageBox.warning(page, "Lỗi", "vui lòng làm mới thông tin trước khi thêm!")


    def deletegiangvien(self,page):
        maGV=self.txt_id.toPlainText()

        if not maGV.strip() :
           QMessageBox.warning(page, "Lỗi", "Vui lòng chọn giảng viên cần xoá !")
           return
        
        TeacherBUS.delete(maGV)
        self.loadList()
        self.cleartxt()

    def updategiangvien(self,page):
         maGV=self.txt_id.toPlainText()
         hoTen = self.txt_hoten.toPlainText()
         SDT = self.txt_sdt.toPlainText()

         if not hoTen.strip() or not SDT.strip() or not maGV.strip():
           QMessageBox.warning(page, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
           return
         
         giangvien = Teacher(maGV,hoTen,SDT)
         TeacherBUS.update(giangvien)
         self.loadList()
         self.cleartxt()

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

    def update(self):   
        pass
    
    def cleartxt(self):
        self.txt_id.clear()
        self.txt_hoten.clear()
        self.txt_sdt.clear()
    