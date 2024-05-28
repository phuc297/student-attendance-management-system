# Form implementation generated from reading ui file '.\student.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Student(object):
    def setupUi(self, Student):
        Student.setObjectName("Student")
        Student.resize(1399, 762)
        self.frame = QtWidgets.QFrame(parent=Student)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.frame.setStyleSheet("QTextEdit{\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"}\n"
"#fr_sinhvien, #fr_lophoc, #fr_thongtin{\n"
"    border: 2px solid grey;\n"
"}\n")
# "QComboBox{\n"
# "    font-size:14px;\n"
# # "    border: 1px solid black;\n"
# "    padding: 5px\n"
# "}\n"
# "QComboBox::drop-down{\n"
# "    border: none;\n"
# "}\n"
# # "QComboBox::down-arrow{\n"
# # "    image: url(:/../assets/icons/droparrow.ico);\n"
# # "    width: 18px;\n"
# # "    background-color: white;\n"
# # "    height: 20px;\n"
# # "    margin-right: 15px\n"
# "}\n"
# "QComboBox:on\n"
# "QComboBox QListView\n"
# "QComboBox QListView::item\n"
# "QComboBox QListView::item:hover\n"
# "QComboBox QListView::item:selected")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lb_main = QtWidgets.QLabel(parent=self.frame)
        self.lb_main.setGeometry(QtCore.QRect(0, 0, 1400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_main.setFont(font)
        self.lb_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_main.setObjectName("lb_main")
        self.lb_main.setStyleSheet("font-size: 25px;\n"
                                     "color: red;\n"
                                     "font-weight: bold;\n"
"")
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setGeometry(QtCore.QRect(0, 50, 1400, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.fr_thongtin = QtWidgets.QFrame(parent=self.frame)
        self.fr_thongtin.setGeometry(QtCore.QRect(10, 60, 561, 661))
        self.fr_thongtin.setStyleSheet("#frame{\n"
"    border: 1px solid black\n"
"}\n"
"QPushButton{\n"
"    padding: 15px 5px;\n"
"}\n"
"#gridLayout{\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.fr_thongtin.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_thongtin.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_thongtin.setObjectName("fr_thongtin")
        self.grbx_canhan = QtWidgets.QGroupBox(parent=self.fr_thongtin)
        self.grbx_canhan.setGeometry(QtCore.QRect(20, 60, 521, 591))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbx_canhan.setFont(font)
        self.grbx_canhan.setStyleSheet("QComboBox,QLabel, QPushButton{\n"
"    font-size: 14px;\n"
"}"
"QDateEdit{\n"
"    font-size: 14px;\n"
"}"
)
        self.grbx_canhan.setObjectName("grbx_canhan")
        self.lb_hoten = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_hoten.setGeometry(QtCore.QRect(10, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_hoten.setFont(font)
        self.lb_hoten.setObjectName("lb_hoten")
        self.lb_namsinh = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_namsinh.setGeometry(QtCore.QRect(10, 120, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_namsinh.setFont(font)
        self.lb_namsinh.setObjectName("lb_namsinh")
        self.lb_cccd = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_cccd.setGeometry(QtCore.QRect(10, 170, 57, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_cccd.setFont(font)
        self.lb_cccd.setObjectName("lb_cccd")
        self.lb_gioitinh = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_gioitinh.setGeometry(QtCore.QRect(10, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_gioitinh.setFont(font)
        self.lb_gioitinh.setObjectName("lb_gioitinh")
        self.lb_email = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_email.setGeometry(QtCore.QRect(10, 270, 56, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_email.setFont(font)
        self.lb_email.setObjectName("lb_email")
        self.lb_sdt = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_sdt.setGeometry(QtCore.QRect(10, 320, 44, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_sdt.setFont(font)
        self.lb_sdt.setObjectName("lb_sdt")
        self.txt_mssv = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_mssv.setEnabled(False)
        self.txt_mssv.setGeometry(QtCore.QRect(90, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_mssv.setFont(font)
        self.txt_mssv.setReadOnly(True)
        self.txt_mssv.setObjectName("txt_mssv")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.grbx_canhan)
        self.dateEdit.setGeometry(QtCore.QRect(90, 120, 411, 41))
        self.dateEdit.setObjectName("birthday")
        # self.txt_namsinh = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        # self.txt_namsinh.setGeometry(QtCore.QRect(90, 120, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        # self.txt_namsinh.setFont(font)
        # # self.txt_namsinh.setObjectName("txt_namsinh")
        self.txt_cccd = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_cccd.setGeometry(QtCore.QRect(90, 170, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_cccd.setFont(font)
        self.txt_cccd.setObjectName("txt_cccd")
        self.txt_email = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_email.setGeometry(QtCore.QRect(90, 270, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.txt_sdt = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_sdt.setGeometry(QtCore.QRect(90, 320, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_sdt.setFont(font)
        self.txt_sdt.setObjectName("txt_sdt")
        self.lb_lophoc = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_lophoc.setGeometry(QtCore.QRect(10, 370, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_lophoc.setFont(font)
        self.lb_lophoc.setObjectName("lb_lophoc")
        self.txt_hoten = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_hoten.setGeometry(QtCore.QRect(90, 70, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_hoten.setFont(font)
        self.txt_hoten.setObjectName("txt_hoten")
        self.lb_hoten_2 = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_hoten_2.setGeometry(QtCore.QRect(10, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_hoten_2.setFont(font)
        self.lb_hoten_2.setObjectName("lb_hoten_2")
        self.cbx_gioitinh = QtWidgets.QComboBox(parent=self.grbx_canhan)
        self.cbx_gioitinh.setGeometry(QtCore.QRect(90, 221, 131, 41))
        self.cbx_gioitinh.setEditable(False)
        self.cbx_gioitinh.setObjectName("cbx_gioitinh")
        self.cbx_gioitinh.addItem("")
        self.cbx_gioitinh.addItem("")
        self.cbx_lophoc = QtWidgets.QComboBox(parent=self.grbx_canhan)
        self.cbx_lophoc.setGeometry(QtCore.QRect(90, 370, 131, 41))
        self.cbx_lophoc.setEditable(False)
        self.cbx_lophoc.setObjectName("cbx_lophoc")
        self.cbx_lophoc.addItem("")
        self.gridBtn = QtWidgets.QFrame(parent=self.grbx_canhan)
        self.gridBtn.setGeometry(QtCore.QRect(20, 470, 491, 118))
        self.gridBtn.setObjectName("gridBtn")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gridBtn)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 7, 481, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_them = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_them.setFlat(False)
        self.btn_them.setObjectName("btn_them")
        self.gridLayout.addWidget(self.btn_them, 0, 0, 1, 1)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.gridLayout.addWidget(self.btn_xoa, 0, 1, 1, 1)
        self.btn_sua = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_sua.setObjectName("btn_sua")
        self.gridLayout.addWidget(self.btn_sua, 0, 2, 1, 1)
        self.btn_reset = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout.addWidget(self.btn_reset, 0, 3, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.gridBtn)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 60, 481, 54))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnViewInfo = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.btnViewInfo.setObjectName("btnViewInfo")
        self.gridLayout_2.addWidget(self.btnViewInfo, 0, 0, 1, 1)
        self.btn_traindata = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.btn_traindata.setObjectName("btn_traindata")
        self.gridLayout_2.addWidget(self.btn_traindata, 0, 1, 1, 1)
        self.lb_thongtin = QtWidgets.QLabel(parent=self.fr_thongtin)
        self.lb_thongtin.setGeometry(QtCore.QRect(4, 10, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lb_thongtin.setFont(font)
        self.lb_thongtin.setStyleSheet("font-size: 20px;\n"
"font-weight: bold;")
        self.lb_thongtin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin.setObjectName("lb_thongtin")
        self.fr_lophoc = QtWidgets.QFrame(parent=self.frame)
        self.fr_lophoc.setGeometry(QtCore.QRect(590, 400, 801, 321))
        self.fr_lophoc.setStyleSheet("QPushButton{\n"
"    padding: 15px 5px;\n"
"    font-size:14px;\n"
"}\n"
"QComboBox, #lb_tenlop, #lb_malop{\n"
"    font-size:14px\n"
"}")
        self.fr_lophoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_lophoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_lophoc.setObjectName("fr_lophoc")
        self.txt_tklop = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_tklop.setGeometry(QtCore.QRect(534, 60, 251, 41))
        self.txt_tklop.setObjectName("txt_tklop")
        self.cbx_tklophoc = QtWidgets.QComboBox(parent=self.fr_lophoc)
        self.cbx_tklophoc.setGeometry(QtCore.QRect(450, 60, 74, 41))
        self.cbx_tklophoc.setObjectName("cbx_tklophoc")
        self.cbx_tklophoc.addItem("")
        self.cbx_tklophoc.addItem("")
        self.tbClass = QtWidgets.QTableWidget(parent=self.fr_lophoc)
        self.tbClass.setGeometry(QtCore.QRect(450, 110, 341, 201))
        self.tbClass.setObjectName("tbClass")
        self.tbClass.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbClass.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbClass.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbClass.setColumnCount(2)
        self.tbClass.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(1, item)
        self.tbClass.horizontalHeader().setDefaultSectionSize(99)
        self.lb_thongtin_3 = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_thongtin_3.setGeometry(QtCore.QRect(20, 10, 771, 41))
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
        self.lb_malop = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_malop.setGeometry(QtCore.QRect(40, 50, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_malop.setFont(font)
        self.lb_malop.setObjectName("lb_malop")
        self.lb_tenlop = QtWidgets.QLabel(parent=self.fr_lophoc)
        self.lb_tenlop.setGeometry(QtCore.QRect(40, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lb_tenlop.setFont(font)
        self.lb_tenlop.setObjectName("lb_tenlop")
        self.txt_malop = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_malop.setGeometry(QtCore.QRect(40, 90, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_malop.setFont(font)
        self.txt_malop.setObjectName("txt_malop")
        self.txt_tenlop = QtWidgets.QTextEdit(parent=self.fr_lophoc)
        self.txt_tenlop.setGeometry(QtCore.QRect(40, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_tenlop.setFont(font)
        self.txt_tenlop.setObjectName("txt_tenlop")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.fr_lophoc)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 250, 411, 51))
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
        self.fr_sinhvien = QtWidgets.QFrame(parent=self.frame)
        self.btn_tksinhvien = QtWidgets.QPushButton(parent=self.fr_sinhvien)
        self.btn_tksinhvien.setGeometry(QtCore.QRect(450, 60, 100, 41))
        self.btn_tksinhvien.setObjectName("btn_tksinhvien")
        self.btn_tksinhvien.setStyleSheet("font-size: 14px;")
        self.btn_resetsinhvien = QtWidgets.QPushButton(parent=self.fr_sinhvien)
        self.btn_resetsinhvien.setGeometry(QtCore.QRect(560, 60, 100, 41))
        self.btn_resetsinhvien.setObjectName("btn_resetsinhvien")
        self.btn_resetsinhvien.setStyleSheet("font-size: 14px;")
        self.fr_sinhvien.setGeometry(QtCore.QRect(589, 60, 801, 331))
        self.fr_sinhvien.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_sinhvien.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_sinhvien.setObjectName("fr_sinhvien")
        self.tbStudents = QtWidgets.QTableWidget(parent=self.fr_sinhvien)
        self.tbStudents.setGeometry(QtCore.QRect(10, 110, 781, 211))
        self.tbStudents.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbStudents.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbStudents.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbStudents.setObjectName("tbStudents")
        self.tbStudents.setColumnCount(8)
        self.tbStudents.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudents.setHorizontalHeaderItem(7, item)
        self.lb_thongtin_2 = QtWidgets.QLabel(parent=self.fr_sinhvien)
        self.lb_thongtin_2.setGeometry(QtCore.QRect(10, 10, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lb_thongtin_2.setFont(font)
        self.lb_thongtin_2.setStyleSheet("font-size: 20px;\n"
"font-weight: bold;\n"
"")
        self.lb_thongtin_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin_2.setObjectName("lb_thongtin_2")
        self.cbx_tksinhvien = QtWidgets.QComboBox(parent=self.fr_sinhvien)
        self.cbx_tksinhvien.setGeometry(QtCore.QRect(10, 60, 74, 41))
        self.cbx_tksinhvien.setObjectName("cbx_tksinhvien")
        self.cbx_tksinhvien.addItem("")
        self.cbx_tksinhvien.addItem("")
        self.cbx_tksinhvien.addItem("")
        self.cbx_tksinhvien.setStyleSheet("font-size: 14px;")
        self.txt_tksinhvien = QtWidgets.QTextEdit(parent=self.fr_sinhvien)
        self.txt_tksinhvien.setGeometry(QtCore.QRect(93, 60, 348, 41))
        self.txt_tksinhvien.setObjectName("txt_tksinhvien")

        self.retranslateUi(Student)
        QtCore.QMetaObject.connectSlotsByName(Student)

    def retranslateUi(self, Student):
        _translate = QtCore.QCoreApplication.translate
        Student.setWindowTitle(_translate("Student", "Form"))
        self.lb_main.setText(_translate("Student", "QUẢN LÝ THÔNG TIN SINH VIÊN"))
        self.grbx_canhan.setTitle(_translate("Student", "Thông tin cá nhân"))
        self.lb_hoten.setText(_translate("Student", "Mã SV:"))
        self.lb_namsinh.setText(_translate("Student", "Năm sinh:"))
        self.lb_cccd.setText(_translate("Student", "CCCD:"))
        self.lb_gioitinh.setText(_translate("Student", "Giới tính:"))
        self.lb_email.setText(_translate("Student", "Email:"))
        self.lb_sdt.setText(_translate("Student", "SĐT:"))
        self.txt_mssv.setHtml(_translate("Student", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>"))
        self.txt_mssv.setPlaceholderText(_translate("Student", "Mã sinh viên"))
        # self.txt_namsinh.setPlaceholderText(_translate("Student", "Nhập năm sinh"))
        self.txt_cccd.setPlaceholderText(_translate("Student", "Nhập căn cước công dân"))
        self.txt_email.setPlaceholderText(_translate("Student", "Nhập email"))
        self.txt_sdt.setPlaceholderText(_translate("Student", "Nhập số điện thoại"))
        self.lb_lophoc.setText(_translate("Student", "Lớp"))
        self.txt_hoten.setPlaceholderText(_translate("Student", "Nhập họ tên sinh viên"))
        self.lb_hoten_2.setText(_translate("Student", "Họ tên:"))
        self.cbx_gioitinh.setItemText(0, _translate("Student", "Nam"))
        self.cbx_gioitinh.setItemText(1, _translate("Student", "Nữ"))
        self.btn_them.setText(_translate("Student", "Thêm mới"))
        self.btn_xoa.setText(_translate("Student", "Xóa"))
        self.btn_sua.setText(_translate("Student", "Sửa"))
        self.btn_reset.setText(_translate("Student", "Làm mới"))
        self.btnViewInfo.setText(_translate("Student", "Xem ảnh"))
        self.btn_traindata.setText(_translate("Student", "Training Data"))
        self.lb_thongtin.setText(_translate("Student", "THÔNG TIN SINH VIÊN"))
        self.txt_tklop.setPlaceholderText(_translate("Student", "Tìm kiếm"))
        self.cbx_tklophoc.setItemText(0, _translate("Student", "Mã lớp"))
        self.cbx_tklophoc.setItemText(1, _translate("Student", "Tên lớp"))
        self.btn_tksinhvien.setText(_translate("Student", "Tìm kiếm"))
        self.btn_resetsinhvien.setText(_translate("Student", "Làm mới"))
        item = self.tbClass.horizontalHeaderItem(0)
        item.setText(_translate("Student", "Mã lớp"))
        item = self.tbClass.horizontalHeaderItem(1)
        item.setText(_translate("Student", "Tên lớp"))
        self.lb_thongtin_3.setText(_translate("Student", "DANH SÁCH LỚP"))
        self.lb_malop.setText(_translate("Student", "Mã lớp:"))
        self.lb_tenlop.setText(_translate("Student", "Tên lớp:"))
        self.txt_malop.setHtml(_translate("Student", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.txt_malop.setPlaceholderText(_translate("Student", "Nhập mã lớp"))
        self.txt_tenlop.setPlaceholderText(_translate("Student", "Nhập tên lớp"))
        self.btn_themlop.setText(_translate("Student", "Thêm mới"))
        self.btn_xoalop.setText(_translate("Student", "Xóa"))
        self.btn_sualop.setText(_translate("Student", "Sửa"))
        self.btn_resetlop.setText(_translate("Student", "Làm mới"))
        self.tbStudents.setSortingEnabled(True)
        self.tbClass.setSortingEnabled(True)
        self.tbClass.horizontalHeader().setDefaultSectionSize(155)
        item = self.tbStudents.horizontalHeaderItem(0)
        item.setText(_translate("Student", "Mã SV"))
        item = self.tbStudents.horizontalHeaderItem(1)
        item.setText(_translate("Student", "Họ tên"))
        item = self.tbStudents.horizontalHeaderItem(2)
        item.setText(_translate("Student", "Mã lớp"))
        item = self.tbStudents.horizontalHeaderItem(3)
        item.setText(_translate("Student", "CMND"))
        item = self.tbStudents.horizontalHeaderItem(4)
        item.setText(_translate("Student", "Giới tính"))
        item = self.tbStudents.horizontalHeaderItem(5)
        item.setText(_translate("Student", "Ngày sinh"))
        item = self.tbStudents.horizontalHeaderItem(6)
        item.setText(_translate("Student", "Email"))
        item = self.tbStudents.horizontalHeaderItem(7)
        item.setText(_translate("Student", "SDT"))
        self.lb_thongtin_2.setText(_translate("Student", "DANH SÁCH SINH VIÊN"))

        self.cbx_tksinhvien.setItemText(0, _translate("Student", "Mã SV"))
        self.cbx_tksinhvien.setItemText(1, _translate("Student", "Họ tên"))
        self.cbx_tksinhvien.setItemText(2, _translate("Student", "Mã lớp"))
        self.cbx_lophoc.setItemText(0, _translate("Student", "Lớp"))
        self.txt_tksinhvien.setPlaceholderText(_translate("Student", "Tìm kiếm"))
        self.dateEdit.setDate(QtCore.QDate.currentDate())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student = QtWidgets.QWidget()
    ui = Ui_Student()
    ui.setupUi(Student)
    Student.show()
    sys.exit(app.exec())
