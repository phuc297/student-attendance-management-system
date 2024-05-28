from ui.ui_stat import *
from bus.student_bus import StudentBUS
from bus.diemdanh_bus import *

class StatsWidget(Ui_Stat):
    
    def __init__(self, page):
        self.setupUi(page)
        self.load()
        self.loadVang()
        self.loadlistdimuon()
        self.btn_dimuon.clicked.connect(lambda: self.timkiemmuon())
        self.btn_vang.clicked.connect(lambda: self.timkiemvang())

    def loadlistdimuon (self):
        listdimuon= DiemdanhBUS.getlistdimuon()
        tablerow=0
        for list in listdimuon :
             self.tableWidget.insertRow(tablerow)
             self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(list[0])))
             self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(str(list[1])))
             self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(str(list[2])))
             self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(list[3])))
             self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(list[4])))
             
             tablerow+=1

    def loadVang(self):
     result_list = DiemdanhBUS.getListVang()

     tablerow = 0

     for row in result_list:
        self.tableWidget_2.insertRow(tablerow)  # Thêm một hàng mới

        self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[2])))
        self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[7])))
        self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[8])))
        self.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[9])))
        self.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[1])))
       
        tablerow += 1  # Tăng chỉ số hàng
    def load(self): 
        sosv = len(StudentBUS.getList())  
        current_text = self.lb_sosv.text()  
        new_text = current_text + f"{sosv}"  
        self.lb_sosv.setText(new_text)   
        
        list_dd = DiemdanhBUS.getlist()
        list_vang = []
        list_ditre = []
        list_dadd = []
        print(len(list_dd))
        
        for dd in list_dd: 
            if str(dd[5]) == '0': 
                list_vang.append(dd)
            elif str(dd[5]) == '2':
                list_ditre.append(dd)
            elif str(dd[5]) == '1':
                 list_dadd.append(dd)
        
        sv_vang = len(list_vang) 
        sv_tre = len(list_ditre)
        sv_dd = len(list_dadd)
        
        self.lb_dimuon.setText(self.lb_dimuon.text() + f"{sv_tre}")
        self.lb_vang.setText(self.lb_vang.text() + f"{sv_vang}")
        self.lb_sodd.setText(self.lb_sodd.text() + f"{sv_dd}")

    def timkiemmuon(self):
        keyword = self.cb_dimuon.currentText()
       

        if keyword == "Tên sinh viên":
             column_index = 1
        elif keyword == "Tên môn học":
             column_index = 3
        

        if column_index is not None:
            search_text = self.txt_dimuon.toPlainText().lower()

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                # Kiểm tra xem ô có chứa từ khóa tìm kiếm hay không
                if search_text in cell_text:
                    self.tableWidget.setRowHidden(row, False)  # Hiện hàng nếu tìm thấy
                else:
                    self.tableWidget.setRowHidden(row, True)

    def timkiemvang(self):
        keyword = self.cb_vang.currentText()
       

        if keyword == "Tên sinh viên":
             column_index = 1
        elif keyword == "Tên môn học":
             column_index = 3
        

        if column_index is not None:
            search_text = self.txt_vang.toPlainText().lower()

        for row in range(self.tableWidget_2.rowCount()):
            item = self.tableWidget_2.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                # Kiểm tra xem ô có chứa từ khóa tìm kiếm hay không
                if search_text in cell_text:
                    self.tableWidget_2.setRowHidden(row, False)  # Hiện hàng nếu tìm thấy
                else:
                    self.tableWidget_2.setRowHidden(row, True)