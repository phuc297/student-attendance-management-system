# Form implementation generated from reading ui file 'subject.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Subject(object):
    def setupUi(self, Subject):
        Subject.setObjectName("Subject")
        Subject.resize(1399, 762)
        # Subject.setMaximumSize(QtCore.QSize(1445, 810))
        self.bg = QtWidgets.QFrame(parent=Subject)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        # self.bg.setMaximumSize(QtCore.QSize(1445, 800))
        self.bg.setStyleSheet("QPushButton{\n"
"    padding: 5px 5px;\n"
"    background-color: white;\n"
"    border-color: black;\n"
"}\n"
"\n"
"#bg{\n"
"    background-color: rgb(241, 241, 241);\n"
"}"
"#lb_main{\n"
"color:red;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"}"
"QTextEdit{\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton, QComboBox{\n"
"    font-size: 14px;\n"
"}"
)
        self.bg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bg.setObjectName("bg")
        self.lb_main = QtWidgets.QLabel(parent=self.bg)
        self.lb_main.setGeometry(QtCore.QRect(0, 0, 1400, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_main.setFont(font)
        self.lb_main.setStyleSheet("")
        self.lb_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_main.setObjectName("lb_main")
        self.line = QtWidgets.QFrame(parent=self.bg)
        self.line.setGeometry(QtCore.QRect(0, 50, 1400, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.ttmh = QtWidgets.QFrame(parent=self.bg)
        self.ttmh.setGeometry(QtCore.QRect(0, 60, 1431, 751))
        self.ttmh.setStyleSheet("#frame{\n"
"        border: 2px solid grey;\n"
"\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 5px;\n"
"    background-color: white;\n"
"}\n"
"#gridLayout{\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.ttmh.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ttmh.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ttmh.setObjectName("ttmh")
        # self.label_5 = QtWidgets.QLabel(parent=self.ttmh)
        # self.label_5.setGeometry(QtCore.QRect(530, 20, 101, 31))
        # self.label_5.setObjectName("label_5")
        self.cb_search = QtWidgets.QComboBox(parent=self.ttmh)
        self.cb_search.setGeometry(QtCore.QRect(600, 10, 141, 41))
        self.cb_search.setObjectName("cb_search")
        self.txt_search = QtWidgets.QTextEdit(parent=self.ttmh)
        self.txt_search.setGeometry(QtCore.QRect(750, 10, 300, 41))
        self.txt_search.setObjectName("txt_search")
        self.btn_search = QtWidgets.QPushButton(parent=self.ttmh)
        self.btn_search.setGeometry(QtCore.QRect(1060, 10, 100, 41))
        self.btn_search.setObjectName("btn_search")
        self.table_mh = QtWidgets.QTableWidget(parent=self.ttmh)
        self.table_mh.setGeometry(QtCore.QRect(600, 60, 750, 611))
        self.table_mh.setStyleSheet("")
        self.table_mh.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.table_mh.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.table_mh.setLineWidth(1)
        self.table_mh.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_mh.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.table_mh.setObjectName("table_mh")
        self.table_mh.setColumnCount(4)
        self.table_mh.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_mh.setHorizontalHeaderItem(3, item)
        self.table_mh.horizontalHeader().setDefaultSectionSize(200)
        self.table_mh.verticalHeader().setDefaultSectionSize(30)
        self.table_mh.verticalHeader().setMinimumSectionSize(30)
        self.frame = QtWidgets.QFrame(parent=self.ttmh)
        self.frame.setGeometry(QtCore.QRect(10, 10, 561, 661))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.txt_maMH = QtWidgets.QTextEdit(parent=self.frame)
        self.txt_maMH.setGeometry(QtCore.QRect(160, 70, 360, 41))
        self.txt_maMH.setObjectName("txt_maMH")
        # self.txt_maMH.setReadOnly(True)
        self.txt_maMH.setEnabled(False)
        self.label_12 = QtWidgets.QLabel(parent=self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 170, 91, 31))
        self.label_12.setObjectName("label_12")
        self.txt_tenMH = QtWidgets.QTextEdit(parent=self.frame)
        self.txt_tenMH.setGeometry(QtCore.QRect(160, 120, 360, 41))
        self.txt_tenMH.setObjectName("txt_tenMH")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 540, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        self.cb_gv = QtWidgets.QComboBox(parent=self.frame)
        self.cb_gv.setGeometry(QtCore.QRect(160, 170, 360, 41))
        self.cb_gv.setObjectName("cb_gv")
        self.cb_gv.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 280, 500, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_them = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setMinimumHeight(41)
        self.horizontalLayout_2.addWidget(self.btn_them)
        self.btn_sua = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setMinimumHeight(41)
        self.horizontalLayout_2.addWidget(self.btn_sua)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_xoa.setMinimumHeight(41)
        self.horizontalLayout_2.addWidget(self.btn_xoa)
        self.btn_refresh = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setMinimumHeight(41)
        self.horizontalLayout_2.addWidget(self.btn_refresh)
        self.cb_lop = QtWidgets.QComboBox(parent=self.frame)
        self.cb_lop.setGeometry(QtCore.QRect(160, 220, 150, 41))
        self.cb_lop.setObjectName("cb_lop")
        self.cb_lop.addItem("")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Subject)
        QtCore.QMetaObject.connectSlotsByName(Subject)

    def retranslateUi(self, Subject):
        _translate = QtCore.QCoreApplication.translate
        Subject.setWindowTitle(_translate("Subject", "Form"))
        self.lb_main.setText(_translate("Subject", "<html><head/><body><p align=\"center\">QUẢN LÝ THÔNG TIN MÔN HỌC</p></body></html>"))
        # self.label_5.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tìm kiếm theo:</span></p></body></html>"))
        self.btn_search.setText(_translate("Subject", "Tìm kiếm"))
        item = self.table_mh.verticalHeaderItem(0)
        item.setText(_translate("Subject", "1"))
        item = self.table_mh.verticalHeaderItem(1)
        item.setText(_translate("Subject", "2"))
        item = self.table_mh.verticalHeaderItem(2)
        item.setText(_translate("Subject", "3"))
        item = self.table_mh.verticalHeaderItem(3)
        item.setText(_translate("Subject", "4"))
        item = self.table_mh.horizontalHeaderItem(0)
        item.setText(_translate("Subject", "Mã môn học"))
        item = self.table_mh.horizontalHeaderItem(1)
        item.setText(_translate("Subject", "Tên môn học"))
        item = self.table_mh.horizontalHeaderItem(2)
        item.setText(_translate("Subject", "Giảng viên"))
        item = self.table_mh.horizontalHeaderItem(3)
        item.setText(_translate("Subject", "Lớp"))
    
        self.cb_gv.setItemText(0, _translate("Subject", "Giảng viên"))
        self.cb_lop.setItemText(0, _translate("Subject", "Lớp"))
        self.label_12.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Giảng viên</span></p></body></html>"))
        self.label_3.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tên môn học</span></p></body></html>"))
        self.label.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:20px; font-weight:600; color:#000000;\">THÔNG TIN MÔN HỌC</span></p></body></html>"))
        self.label_2.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mã môn học</span></p></body></html>"))
        self.btn_them.setText(_translate("Subject", "Thêm mới"))
        self.btn_sua.setText(_translate("Subject", "Cập nhật"))
        self.btn_xoa.setText(_translate("Subject", "Xóa"))
        self.btn_refresh.setText(_translate("Subject", "Làm mới"))
        self.label_13.setText(_translate("Subject", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Lớp</span></p></body></html>"))
        self.txt_maMH.setPlaceholderText(_translate("Subject", "Mã môn học"))
        self.txt_search.setPlaceholderText(_translate("Subject", "Tìm kiếm"))
        self.txt_tenMH.setPlaceholderText(_translate("Subject", "Nhập tên môn học"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Subject = QtWidgets.QWidget()
    ui = Ui_Subject()
    ui.setupUi(Subject)
    Subject.show()
    sys.exit(app.exec())
