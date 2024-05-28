# Form implementation generated from reading ui file '.\class.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Class(object):
    def setupUi(self, Class):
        Class.setObjectName("Class")
        Class.resize(1431, 800)
        Class.setMaximumSize(QtCore.QSize(1445, 810))
        self.bg = QtWidgets.QFrame(parent=Class)
        self.bg.setGeometry(QtCore.QRect(10, 10, 1400, 800))
        self.bg.setMaximumSize(QtCore.QSize(1445, 800))
        self.bg.setStyleSheet("QPushButton{\n"
"    padding: 15px 5px;\n"
"    background-color: #D5EDF9;\n"
"    border-color: black;\n"
"}\n"
"\n"
"#bg{\n"
"    background-color: rgb(241, 241, 241);\n"
"}")
        self.bg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bg.setObjectName("bg")
        self.lb_main = QtWidgets.QLabel(parent=self.bg)
        self.lb_main.setGeometry(QtCore.QRect(0, -11, 1400, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_main.setFont(font)
        self.lb_main.setStyleSheet("#lb_main{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.lb_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_main.setObjectName("lb_main")
        self.line = QtWidgets.QFrame(parent=self.bg)
        self.line.setGeometry(QtCore.QRect(0, 50, 1400, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.fr_lophoc = QtWidgets.QFrame(parent=self.bg)
        self.fr_lophoc.setGeometry(QtCore.QRect(20, 70, 1361, 701))
        self.fr_lophoc.setStyleSheet("QPushButton{\n"
"    padding: 15px 5px;\n"
"    font-size:14px;\n"
"    background-color: #D5EDF9;\n"
"}\n"
"#lb_tenlop, #lb_malop{\n"
"    font-size:14px\n"
"}")
        self.fr_lophoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_lophoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_lophoc.setObjectName("fr_lophoc")
        self.txt_tklop = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_tklop.setGeometry(QtCore.QRect(1090, 80, 251, 41))
        self.txt_tklop.setObjectName("txt_tklop")
        self.cbx_tklophoc = QtWidgets.QComboBox(parent=self.fr_lophoc)
        self.cbx_tklophoc.setGeometry(QtCore.QRect(1010, 80, 74, 41))
        self.cbx_tklophoc.setObjectName("cbx_tklophoc")
        self.cbx_tklophoc.addItem("")
        self.cbx_tklophoc.addItem("")
        self.tbClass = QtWidgets.QTableWidget(parent=self.fr_lophoc)
        self.tbClass.setGeometry(QtCore.QRect(576, 130, 771, 521))
        self.tbClass.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbClass.setObjectName("tbClass")
        self.tbClass.setColumnCount(2)
        self.tbClass.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(1, item)
        self.tbClass.horizontalHeader().setDefaultSectionSize(99)
        self.lb_thongtin_3 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_thongtin_3.setGeometry(QtCore.QRect(580, 10, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lb_thongtin_3.setFont(font)
        self.lb_thongtin_3.setStyleSheet("\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"")
        self.lb_thongtin_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin_3.setObjectName("lb_thongtin_3")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.fr_lophoc)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 390, 411, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_themlop = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.btn_themlop.setFlat(False)
        self.btn_themlop.setObjectName("btn_themlop")
        self.gridLayout_3.addWidget(self.btn_themlop, 0, 0, 1, 1)
        self.btn_xoalop = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.btn_xoalop.setObjectName("btn_xoalop")
        self.gridLayout_3.addWidget(self.btn_xoalop, 0, 1, 1, 1)
        self.btn_sualop = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.btn_sualop.setObjectName("btn_sualop")
        self.gridLayout_3.addWidget(self.btn_sualop, 0, 2, 1, 1)
        self.btn_resetlop = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.btn_resetlop.setObjectName("btn_resetlop")
        self.gridLayout_3.addWidget(self.btn_resetlop, 0, 3, 1, 1)
        self.txt_malop = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_malop.setEnabled(False)
        self.txt_malop.setGeometry(QtCore.QRect(110, 130, 411, 41))
        font = QtGui.QFont()
        self.txt_malop.setFont(font)
        self.txt_malop.setReadOnly(True)
        self.txt_malop.setObjectName("txt_malop")
        self.lb_hoten = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_hoten.setGeometry(QtCore.QRect(30, 130, 71, 41))
        font = QtGui.QFont()
        self.lb_hoten.setFont(font)
        self.lb_hoten.setObjectName("lb_hoten")
        self.lb_thongtin_4 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_thongtin_4.setGeometry(QtCore.QRect(30, 10, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lb_thongtin_4.setFont(font)
        self.lb_thongtin_4.setStyleSheet("\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"")
        self.lb_thongtin_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin_4.setObjectName("lb_thongtin_4")
        self.lb_hoten_2 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_hoten_2.setGeometry(QtCore.QRect(30, 190, 71, 41))
        font = QtGui.QFont()
        self.lb_hoten_2.setFont(font)
        self.lb_hoten_2.setObjectName("lb_hoten_2")
        self.txt_mon = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_mon.setGeometry(QtCore.QRect(110, 190, 411, 41))
        font = QtGui.QFont()
        self.txt_mon.setFont(font)
        self.txt_mon.setPlaceholderText("")
        self.txt_mon.setObjectName("txt_mon")
        self.lb_hoten_3 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_hoten_3.setGeometry(QtCore.QRect(30, 250, 71, 41))
        font = QtGui.QFont()
        self.lb_hoten_3.setFont(font)
        self.lb_hoten_3.setObjectName("lb_hoten_3")
        self.txt_giangvien = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_giangvien.setGeometry(QtCore.QRect(110, 250, 411, 41))
        font = QtGui.QFont()
        self.txt_giangvien.setFont(font)
        self.txt_giangvien.setPlaceholderText("")
        self.txt_giangvien.setObjectName("txt_giangvien")
        self.txt_soluong = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_soluong.setGeometry(QtCore.QRect(110, 310, 411, 41))
        font = QtGui.QFont()
        self.txt_soluong.setFont(font)
        self.txt_soluong.setPlaceholderText("")
        self.txt_soluong.setObjectName("txt_soluong")
        self.lb_hoten_4 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_hoten_4.setGeometry(QtCore.QRect(30, 310, 71, 41))
        font = QtGui.QFont()
        self.lb_hoten_4.setFont(font)
        self.lb_hoten_4.setObjectName("lb_hoten_4")

        self.retranslateUi(Class)
        QtCore.QMetaObject.connectSlotsByName(Class)

    def retranslateUi(self, Class):
        _translate = QtCore.QCoreApplication.translate
        Class.setWindowTitle(_translate("Class", "Form"))
        self.lb_main.setText(_translate("Class", "<html><head/><body><p align=\"center\">QUẢN LÝ THÔNG TIN LỚP HỌC</p></body></html>"))
        self.txt_tklop.setPlaceholderText(_translate("Class", "Tìm kiếm"))
        self.cbx_tklophoc.setItemText(0, _translate("Class", "Mã lớp"))
        self.cbx_tklophoc.setItemText(1, _translate("Class", "Tên lớp"))
        item = self.tbClass.horizontalHeaderItem(0)
        item.setText(_translate("Class", "Mã lớp"))
        item = self.tbClass.horizontalHeaderItem(1)
        item.setText(_translate("Class", "Tên lớp"))
        self.lb_thongtin_3.setText(_translate("Class", "DANH SÁCH LỚP"))
        self.btn_themlop.setText(_translate("Class", "Thêm mới"))
        self.btn_xoalop.setText(_translate("Class", "Xóa"))
        self.btn_sualop.setText(_translate("Class", "Sửa"))
        self.btn_resetlop.setText(_translate("Class", "Làm mới"))
        self.txt_malop.setHtml(_translate("Class", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3</span></p></body></html>"))
        self.lb_hoten.setText(_translate("Class", "Mã lớp:"))
        self.lb_thongtin_4.setText(_translate("Class", "THÔNG TIN LỚP HỌC"))
        self.lb_hoten_2.setText(_translate("Class", "Môn học"))
        self.lb_hoten_3.setText(_translate("Class", "Giảng viên"))
        self.lb_hoten_4.setText(_translate("Class", "Số lượng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Class = QtWidgets.QWidget()
    ui = Ui_Class()
    ui.setupUi(Class)
    Class.show()
    sys.exit(app.exec())
