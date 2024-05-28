# -*- coding: utf-8 -*-
from bus.diemdanh_bus import *
from dto.diemdanh_dto import *
from PyQt6.QtWidgets import QMessageBox
from ui.ui_diemdanh2 import *
import pandas as pd
from PyQt6.QtWidgets import QFileDialog
import os
from bus.attend_bus import *

class diemdanhWidget(Ui_Form):
    def __init__(self,page):
        self.setupUi(page)
        
        self.loadList()
        self.tb_diemdanh.itemClicked.connect(lambda: self.tableEvent())
        self.btn_timkiem.clicked.connect(lambda: self.searchEvent())
        self.btn_reset2.clicked.connect(lambda: self.clear())
        self.btn_capnhat.clicked.connect(lambda: self.update(page))
        self.btn_xuatexel.clicked.connect(lambda: self.toExcel())
        self.btn_xoa_3.clicked.connect(lambda: self.delete(page))

    def loadList(self):
        self.listDiemDanh = DiemdanhBUS.getList()
        self.tb_diemdanh.setRowCount(self.listDiemDanh.__len__())
        tablerow = 0
        if self.listDiemDanh is not None:
            for row in self.listDiemDanh:
                self.tb_diemdanh.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tb_diemdanh.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tb_diemdanh.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tb_diemdanh.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tb_diemdanh.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tb_diemdanh.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tb_diemdanh.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.tb_diemdanh.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                self.tb_diemdanh.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                tablerow += 1
    
    def tableEvent(self):
        cr = self.tb_diemdanh.currentRow()
        diemdanh = self.listDiemDanh[cr]
        self.txt_IDdiemdanh.setText(str(diemdanh[0]))
        self.txt_IDsinhvien.setText(str(diemdanh[1]))
        self.txt_tensinhvien.setText(str(diemdanh[2]))
        self.txt_lophoc.setText(str(diemdanh[3]))
        self.txt_giovao.setText(str(diemdanh[4]))
        self.txt_giora.setText(str(diemdanh[5]))
        self.txt_ngay.setText(str(diemdanh[6]))
        self.txtchitiet.setText(str(diemdanh[7]))
        self.txt_buoihoc.setText(str(diemdanh[8]))
        
    def toExcel(self):
        try:
            rowCount = self.tb_diemdanh.rowCount()
            columnCount = 8
            data = []

            for row in range(rowCount):
                rowData = []
                for column in range(columnCount):
                    widgetItem = self.tb_diemdanh.item(row, column)
                    if widgetItem and widgetItem.text:
                        rowData.append(widgetItem.text())
                    else:
                        rowData.append('NULL')
                data.append(rowData)
            df = pd.DataFrame(data)
            dir_path = QFileDialog.getSaveFileName(
                caption="Save Excel",
                directory=os.getcwd(),
                options=QFileDialog.Option.DontUseNativeDialog,
            )
            df.to_excel(dir_path[0] + ".xlsx", header=False, index=False)
        except Exception as e:
            print(e)
        
    def searchEvent(self):
        selected_text = self.comboBox.currentText()
        column_index = 0
        if selected_text == "Mã Điểm Danh":
            column_index = 0
        elif selected_text == "Họ tên ":
            column_index = 1
        elif selected_text == "Mã lớp":
            column_index = 2
            
        if column_index is not None:
            search_text = self.txt_timkiem.toPlainText()
            
        for row in range(self.tb_diemdanh.rowCount()):
            item = self.tb_diemdanh.item(row, column_index)
            if item is not None:
                cell_text = item.text().lower()
                if search_text.lower() in cell_text:
                    self.tb_diemdanh.setRowHidden(row, False)
                else:
                    self.tb_diemdanh.setRowHidden(row, True)
                    
    def clear(self):
        self.loadList()
        self.txt_IDdiemdanh.clear()
        self.txt_IDsinhvien.clear()
        self.txt_tensinhvien.clear()
        self.txt_lophoc.clear()
        self.txt_giovao.clear()
        self.txt_giora.clear()
        self.txt_ngay.clear()
        self.txtchitiet.clear()
        self.txt_buoihoc.clear()
        self.txt_timkiem.clear()
        self.searchEvent()
    
    def update(self,page):
        try:
            if self.txt_IDdiemdanh.toPlainText() == "":
                QMessageBox.information(page,"Chú ý", "Lỗi! Vui lòng chọn trước khi cập nhật!", QMessageBox.StandardButton.Ok)
                return
            maDD = self.txt_IDdiemdanh.toPlainText()
            gioVao = self.txt_giovao.toPlainText()
            gioRa = self.txt_giora.toPlainText()
            chitiet = self.txtchitiet.toPlainText()
            if DiemdanhBUS.update(maDD, gioVao, gioRa, chitiet):
                QMessageBox.information(page, "Thông báo", "Cập nhật thành công!")
                self.listDiemDanh = DiemdanhBUS.getList()
                self.loadList()
                self.clear()
        except Exception as e:
            print(e)
            
    def delete(self,s):
        try:
            cr = self.tb_diemdanh.currentRow()
            madd = self.tb_diemdanh.item(cr, 0).text()
            if (AttendBUS.delete(madd)):
                self.loadList()
                QMessageBox.information(s, "Thông báo", "Xóa thành công!")
        except Exception as e:
            print(e)
            
        
                