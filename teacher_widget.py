from ui.ui_teacher import *
from bus.teacher_bus import *
from dto.teacher import Teacher
class TeacherWidget(Ui_Teacher):
   
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tableteacher.itemClicked.connect(lambda: self.tableEvent())
        self.btn_luu.clicked.connect(lambda: self.addgiangvien())
        self.btn_xoa.clicked.connect(lambda: self.deletegiangvien())
        self.btn_sua.clicked.connect(lambda: self.updategiangvien())
        self.btn_reset.clicked.connect(lambda: self.cleartxt())
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

    def addgiangvien(self):
        hoTen = self.txt_hoten.toPlainText()
        SDT = self.txt_sdt.toPlainText()
        giangvien = Teacher(hoTen,SDT)
        TeacherBUS.addlist(giangvien)
        self.loadList()

    def deletegiangvien(self):
        maGV=self.txt_id.toPlainText()
        TeacherBUS.delete(maGV)
        self.loadList()
        self.cleartxt()

    def updategiangvien(self):
         maGV=self.txt_id.toPlainText()
         hoTen = self.txt_hoten.toPlainText()
         SDT = self.txt_sdt.toPlainText()
         giangvien = Teacher(maGV,hoTen,SDT)
         TeacherBUS.update(giangvien)
         self.loadList()
         self.cleartxt()

    def update(self):   
        pass
    
    def cleartxt(self):
        self.txt_id.clear()
        self.txt_hoten.clear()
        self.txt_sdt.clear()
    