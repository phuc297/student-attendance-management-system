from ui.ui_teacher import *
from bus.teacher_bus import *
from dto.teacher import Teacher
class TeacherWidget(Ui_Teacher):
   
    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tableteacher.itemClicked.connect(lambda: self.tableEvent())
        self.btn_luu.clicked.connect(lambda: self.addgiangvien())
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
                print(row)
    

    def tableEvent(self):
        cr = self.tableteacher.currentRow()
        self.txt_id.setText(self.tableteacher.item(cr, 0).text())
        self.txt_hoten.setText(self.tableteacher.item(cr, 1).text())
        self.txt_sdt.setText(self.tableteacher.item(cr, 2).text())

    def addgiangvien(self):
        maGV=self.txt_id.text()
        hoTen = self.txt_hoten.text()
        SDT = self.txt_sdt.text()
        giangvien = Teacher(maGV,hoTen,SDT)
        TeacherBUS.addlist(giangvien)

    def update(self):
        pass