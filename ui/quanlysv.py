# Form implementation generated from reading ui file '.\quanlysv.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_student(object):
    def setupUi(self, student):
        student.setObjectName("student")
        student.resize(1445, 796)
        student.setStyleSheet("#centralwidget{\n"
"    background-color: #D5EDF9\n"
"}\n"
"#centralwidget #widgetmain{\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"    border: 5px solid #5442B1;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=student)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetmain = QtWidgets.QWidget(parent=self.centralwidget)
        self.widgetmain.setGeometry(QtCore.QRect(20, 20, 1445, 796))
        self.widgetmain.setObjectName("widgetmain")
        self.lb_main = QtWidgets.QLabel(parent=self.widgetmain)
        self.lb_main.setGeometry(QtCore.QRect(10, 10, 1381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lb_main.setFont(font)
        self.lb_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_main.setObjectName("lb_main")
        self.line = QtWidgets.QFrame(parent=self.widgetmain)
        self.line.setGeometry(QtCore.QRect(20, 70, 1360, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(parent=self.widgetmain)
        self.frame.setGeometry(QtCore.QRect(40, 80, 561, 661))
        self.frame.setStyleSheet("#frame{\n"
"    border: 1px solid black\n"
"}\n"
"QPushButton{\n"
"    padding: 15px 5px;\n"
"    background-color: #D5EDF9;\n"
"}\n"
"#gridLayout{\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.grbx_canhan = QtWidgets.QGroupBox(parent=self.frame)
        self.grbx_canhan.setGeometry(QtCore.QRect(20, 170, 521, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.grbx_canhan.setFont(font)
        self.grbx_canhan.setObjectName("grbx_canhan")
        self.lb_hoten = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_hoten.setGeometry(QtCore.QRect(20, 30, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_hoten.setFont(font)
        self.lb_hoten.setObjectName("lb_hoten")
        self.lb_namsinh = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_namsinh.setGeometry(QtCore.QRect(20, 80, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_namsinh.setFont(font)
        self.lb_namsinh.setObjectName("lb_namsinh")
        self.lb_cccd = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_cccd.setGeometry(QtCore.QRect(20, 130, 57, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_cccd.setFont(font)
        self.lb_cccd.setObjectName("lb_cccd")
        self.lb_gioitinh = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_gioitinh.setGeometry(QtCore.QRect(20, 180, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_gioitinh.setFont(font)
        self.lb_gioitinh.setObjectName("lb_gioitinh")
        self.lb_email = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_email.setGeometry(QtCore.QRect(20, 230, 56, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_email.setFont(font)
        self.lb_email.setObjectName("lb_email")
        self.lb_sdt = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_sdt.setGeometry(QtCore.QRect(20, 280, 44, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_sdt.setFont(font)
        self.lb_sdt.setObjectName("lb_sdt")
        self.txt_hoten = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_hoten.setGeometry(QtCore.QRect(100, 30, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_hoten.setFont(font)
        self.txt_hoten.setObjectName("txt_hoten")
        self.txt_namsinh = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_namsinh.setGeometry(QtCore.QRect(100, 80, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_namsinh.setFont(font)
        self.txt_namsinh.setObjectName("txt_namsinh")
        self.txt_cccd = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_cccd.setGeometry(QtCore.QRect(100, 130, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_cccd.setFont(font)
        self.txt_cccd.setObjectName("txt_cccd")
        self.txt_gioitinh = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_gioitinh.setGeometry(QtCore.QRect(100, 180, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_gioitinh.setFont(font)
        self.txt_gioitinh.setObjectName("txt_gioitinh")
        self.txt_email = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_email.setGeometry(QtCore.QRect(90, 230, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.txt_sdt = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_sdt.setGeometry(QtCore.QRect(100, 280, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_sdt.setFont(font)
        self.txt_sdt.setObjectName("txt_sdt")
        self.lb_diachi = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_diachi.setGeometry(QtCore.QRect(20, 330, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_diachi.setFont(font)
        self.lb_diachi.setObjectName("lb_diachi")
        self.txt_diachi = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_diachi.setGeometry(QtCore.QRect(100, 330, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_diachi.setFont(font)
        self.txt_diachi.setObjectName("txt_diachi")
        self.grbx_khoahoc = QtWidgets.QGroupBox(parent=self.frame)
        self.grbx_khoahoc.setGeometry(QtCore.QRect(20, 50, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.grbx_khoahoc.setFont(font)
        self.grbx_khoahoc.setObjectName("grbx_khoahoc")
        self.lb_khoahoc = QtWidgets.QLabel(parent=self.grbx_khoahoc)
        self.lb_khoahoc.setGeometry(QtCore.QRect(20, 30, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_khoahoc.setFont(font)
        self.lb_khoahoc.setObjectName("lb_khoahoc")
        self.cbx_khoahoc = QtWidgets.QComboBox(parent=self.grbx_khoahoc)
        self.cbx_khoahoc.setGeometry(QtCore.QRect(100, 30, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbx_khoahoc.setFont(font)
        self.cbx_khoahoc.setObjectName("cbx_khoahoc")
        self.cbx_khoahoc.addItem("")
        self.cbx_lop = QtWidgets.QComboBox(parent=self.grbx_khoahoc)
        self.cbx_lop.setGeometry(QtCore.QRect(100, 70, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbx_lop.setFont(font)
        self.cbx_lop.setObjectName("cbx_lop")
        self.lb_lop = QtWidgets.QLabel(parent=self.grbx_khoahoc)
        self.lb_lop.setGeometry(QtCore.QRect(20, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_lop.setFont(font)
        self.lb_lop.setObjectName("lb_lop")
        self.lb_thongtin = QtWidgets.QLabel(parent=self.frame)
        self.lb_thongtin.setGeometry(QtCore.QRect(4, 10, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_thongtin.setFont(font)
        self.lb_thongtin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin.setObjectName("lb_thongtin")
        self.gridBtn = QtWidgets.QFrame(parent=self.frame)
        self.gridBtn.setGeometry(QtCore.QRect(10, 550, 541, 118))
        self.gridBtn.setObjectName("gridBtn")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gridBtn)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 7, 541, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_luu = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_luu.setFlat(False)
        self.btn_luu.setObjectName("btn_luu")
        self.gridLayout.addWidget(self.btn_luu, 0, 0, 1, 1)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.gridLayout.addWidget(self.btn_xoa, 0, 1, 1, 1)
        self.btn_xoa_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_xoa_2.setObjectName("btn_xoa_2")
        self.gridLayout.addWidget(self.btn_xoa_2, 0, 2, 1, 1)
        self.btn_reset = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout.addWidget(self.btn_reset, 0, 3, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.gridBtn)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 50, 541, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_luu_2 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_luu_2.setObjectName("btn_luu_2")
        self.gridLayout_2.addWidget(self.btn_luu_2, 0, 0, 1, 1)
        self.btn_reset_2 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_reset_2.setObjectName("btn_reset_2")
        self.gridLayout_2.addWidget(self.btn_reset_2, 0, 1, 1, 1)
        student.setCentralWidget(self.centralwidget)

        self.retranslateUi(student)
        QtCore.QMetaObject.connectSlotsByName(student)

    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "MainWindow"))
        self.lb_main.setText(_translate("student", "QUẢN LÝ THÔNG TIN SINH VIÊN"))
        self.grbx_canhan.setTitle(_translate("student", "Thông tin cá nhân"))
        self.lb_hoten.setText(_translate("student", "Họ tên:"))
        self.lb_namsinh.setText(_translate("student", "Năm sinh:"))
        self.lb_cccd.setText(_translate("student", "CCCD:"))
        self.lb_gioitinh.setText(_translate("student", "Giới tính:"))
        self.lb_email.setText(_translate("student", "Email:"))
        self.lb_sdt.setText(_translate("student", "SĐT:"))
        self.lb_diachi.setText(_translate("student", "Địa chỉ:"))
        self.grbx_khoahoc.setTitle(_translate("student", "Thông tin khóa học"))
        self.lb_khoahoc.setText(_translate("student", "Khóa học:"))
        self.cbx_khoahoc.setItemText(0, _translate("student", "New Item"))
        self.lb_lop.setText(_translate("student", "Lớp:"))
        self.lb_thongtin.setText(_translate("student", "THÔNG TIN SINH VIÊN"))
        self.btn_luu.setText(_translate("student", "Lưu"))
        self.btn_xoa.setText(_translate("student", "Xóa"))
        self.btn_xoa_2.setText(_translate("student", "Sửa"))
        self.btn_reset.setText(_translate("student", "Làm mới"))
        self.btn_luu_2.setText(_translate("student", "Lấy ảnh"))
        self.btn_reset_2.setText(_translate("student", "Training Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student = QtWidgets.QMainWindow()
    ui = Ui_student()
    ui.setupUi(student)
    student.show()
    sys.exit(app.exec())
