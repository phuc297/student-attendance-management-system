# Form implementation generated from reading ui file 'stat.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Stat(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1399, 762)
        self.ui_stat = QtWidgets.QFrame(parent=Form)
        self.ui_stat.setGeometry(QtCore.QRect(20, 20, 1399, 711))
        self.ui_stat.setStyleSheet("QPushButton{\n"
"    padding: 5px 5px;\n"
"    background-color: #D5EDF9;\n"
"}\n"
"\n"
"QLabel{\n"
"border: 1px solid black;\n"
"border-radius: 20px;\n"
"\n"
"}"
"QComboBox, QTextEdit, QPushButton{\n"
" font-size: 14px;\n"
"}\n"
)
        self.ui_stat.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ui_stat.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui_stat.setObjectName("ui_stat")
        self.lb_thongke = QtWidgets.QLabel(parent=self.ui_stat)
        self.lb_thongke.setGeometry(QtCore.QRect(0, 0, 1399, 51))
        self.lb_thongke.setStyleSheet("border: 1px solid black\n"
"")
        self.lb_thongke.setObjectName("lb_thongke")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.ui_stat)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 1365, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_tk = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_tk.setContentsMargins(0, 0, 0, 0)
        self.layout_tk.setSpacing(20)
        self.layout_tk.setObjectName("layout_tk")
        self.lb_sosv = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lb_sosv.setStyleSheet("background-color: rgb(202, 67, 0);\n"
"color:white;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding-left:20px;")
        self.lb_sosv.setObjectName("lb_sosv")
        self.layout_tk.addWidget(self.lb_sosv)
        self.lb_sodd = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lb_sodd.setStyleSheet("background-color: rgb(126, 126, 189);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"padding-left:20px;")
        self.lb_sodd.setObjectName("lb_sodd")
        self.layout_tk.addWidget(self.lb_sodd)
        self.lb_vang = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lb_vang.setStyleSheet("background-color: rgb(85, 181, 79);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"padding-left:20px;")
        self.lb_vang.setObjectName("lb_vang")
        self.layout_tk.addWidget(self.lb_vang)
        self.lb_dimuon = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lb_dimuon.setStyleSheet("background-color: rgb(220, 147, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"padding-left:20px;")
        self.lb_dimuon.setObjectName("lb_dimuon")
        self.layout_tk.addWidget(self.lb_dimuon)
        self.groupBox = QtWidgets.QGroupBox(parent=self.ui_stat)
        self.groupBox.setGeometry(QtCore.QRect(30, 180, 631, 531))
        self.groupBox.setObjectName("groupBox")
        self.cb_dimuon = QtWidgets.QComboBox(parent=self.groupBox)
        self.cb_dimuon.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.cb_dimuon.setObjectName("cb_dimuon")
        self.cb_dimuon.addItem("")
        self.cb_dimuon.addItem("")
        self.txt_dimuon = QtWidgets.QTextEdit(parent=self.groupBox)
        self.txt_dimuon.setGeometry(QtCore.QRect(140, 20, 200, 41))
        self.txt_dimuon.setObjectName("txt_dimuon")
        self.btn_dimuon = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_dimuon.setGeometry(QtCore.QRect(350, 20, 100, 41))
        self.btn_dimuon.setObjectName("btn_dimuon")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 611, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.ui_stat)
        self.groupBox_2.setGeometry(QtCore.QRect(720, 180, 631, 531))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_vang = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btn_vang.setGeometry(QtCore.QRect(350, 20, 100, 41))
        self.btn_vang.setObjectName("btn_vang")
        self.txt_vang = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.txt_vang.setGeometry(QtCore.QRect(140, 20, 200, 41))
        self.txt_vang.setObjectName("txt_vang")
        self.cb_vang = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cb_vang.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.cb_vang.setObjectName("cb_vang")
        self.cb_vang.addItem("")
        self.cb_vang.addItem("")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 80, 611, 441))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_thongke.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">THỐNG KÊ</span></p></body></html>"))
        self.lb_sosv.setText(_translate("Form", "<html><head/><body><p>Số sinh viên</p></body></html>"))
        self.lb_sodd.setText(_translate("Form", "<html><head/><body><p>Số bản điểm danh </p></body></html>"))
        self.lb_vang.setText(_translate("Form", "<html><head/><body><p>Số lần vắng </p></body></html>"))
        self.lb_dimuon.setText(_translate("Form", "<html><head/><body><p>Số lần đi muộn</p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Sinh viên đi muộn"))
        self.cb_dimuon.setItemText(0, _translate("Form", "Tên sinh viên"))
        self.cb_dimuon.setItemText(1, _translate("Form", "Tên môn học"))
        self.btn_dimuon.setText(_translate("Form", "Tìm kiếm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã sinh viên"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tên sinh viên"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ngày"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Môn học "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mã buổi học"))
        self.groupBox_2.setTitle(_translate("Form", "Sinh viên vắng"))
        self.btn_vang.setText(_translate("Form", "Tìm kiếm"))
        self.cb_vang.setItemText(0, _translate("Form", "Tên sinh viên"))
        self.cb_vang.setItemText(1, _translate("Form", "Tên môn học"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã sinh viên"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tên sinh viên"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ngày"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Môn học"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mã buổi học"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Stat()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
