# Form implementation generated from reading ui file '.\quanlygv.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Teacher(object):
    def setupUi(self, Teacher):
        Teacher.setObjectName("Teacher")
        Teacher.resize(1385, 769)
        self.widgetmain = QtWidgets.QWidget(parent=Teacher)
        self.widgetmain.setGeometry(QtCore.QRect(0, 0, 1445, 796))
        self.widgetmain.setObjectName("widgetmain")
        self.lb_main = QtWidgets.QLabel(parent=self.widgetmain)
        self.lb_main.setGeometry(QtCore.QRect(10, 10, 1381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_main.setFont(font)
        self.lb_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_main.setObjectName("lb_main")
        self.line = QtWidgets.QFrame(parent=self.widgetmain)
        self.line.setGeometry(QtCore.QRect(20, 70, 1360, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(parent=self.widgetmain)
        self.frame.setGeometry(QtCore.QRect(40, 80, 491, 531))
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
        self.grbx_canhan.setGeometry(QtCore.QRect(10, 70, 471, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbx_canhan.setFont(font)
        self.grbx_canhan.setTitle("")
        self.grbx_canhan.setObjectName("grbx_canhan")
        self.lb_hoten = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_hoten.setGeometry(QtCore.QRect(20, 30, 81, 41))
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
        self.lb_sdt = QtWidgets.QLabel(parent=self.grbx_canhan)
        self.lb_sdt.setGeometry(QtCore.QRect(20, 130, 44, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_sdt.setFont(font)
        self.lb_sdt.setObjectName("lb_sdt")
        self.txt_id = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_id.setEnabled(True)
        self.txt_id.setGeometry(QtCore.QRect(120, 30, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_id.setFont(font)
        self.txt_id.setReadOnly(True)
        self.txt_id.setAcceptRichText(False)
        self.txt_id.setObjectName("txt_id")
        self.txt_hoten = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_hoten.setGeometry(QtCore.QRect(120, 80, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_hoten.setFont(font)
        self.txt_hoten.setObjectName("txt_hoten")
        self.txt_sdt = QtWidgets.QTextEdit(parent=self.grbx_canhan)
        self.txt_sdt.setGeometry(QtCore.QRect(120, 130, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_sdt.setFont(font)
        self.txt_sdt.setObjectName("txt_sdt")
        self.lb_thongtin = QtWidgets.QLabel(parent=self.frame)
        self.lb_thongtin.setGeometry(QtCore.QRect(4, 10, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_thongtin.setFont(font)
        self.lb_thongtin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin.setObjectName("lb_thongtin")
        self.gridBtn = QtWidgets.QFrame(parent=self.frame)
        self.gridBtn.setGeometry(QtCore.QRect(10, 420, 541, 118))
        self.gridBtn.setObjectName("gridBtn")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gridBtn)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 7, 461, 98))
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
        self.btn_sua = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_sua.setObjectName("btn_sua")
        self.gridLayout.addWidget(self.btn_sua, 0, 2, 1, 1)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.gridLayout.addWidget(self.btn_xoa, 0, 1, 1, 1)
        self.btn_reset = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout.addWidget(self.btn_reset, 0, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.widgetmain)
        self.frame_2.setGeometry(QtCore.QRect(540, 80, 841, 531))
        self.frame_2.setStyleSheet("#frame_2{\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.grbx_canhan_2 = QtWidgets.QGroupBox(parent=self.frame_2)
        self.grbx_canhan_2.setGeometry(QtCore.QRect(10, 20, 821, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grbx_canhan_2.setFont(font)
        self.grbx_canhan_2.setTitle("")
        self.grbx_canhan_2.setObjectName("grbx_canhan_2")
        self.lb_thongtin_2 = QtWidgets.QLabel(parent=self.grbx_canhan_2)
        self.lb_thongtin_2.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_thongtin_2.setFont(font)
        self.lb_thongtin_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_thongtin_2.setObjectName("lb_thongtin_2")
        self.comboBoxtimkiem = QtWidgets.QComboBox(parent=self.grbx_canhan_2)
        self.comboBoxtimkiem.setGeometry(QtCore.QRect(140, 10, 131, 31))
        self.comboBoxtimkiem.setObjectName("comboBoxtimkiem")
        self.comboBoxtimkiem.addItem("")
        self.comboBoxtimkiem.addItem("")
        self.comboBoxtimkiem.addItem("")
        self.txt_timkiem = QtWidgets.QTextEdit(parent=self.grbx_canhan_2)
        self.txt_timkiem.setGeometry(QtCore.QRect(290, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_timkiem.setFont(font)
        self.txt_timkiem.setObjectName("txt_timkiem")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.grbx_canhan_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 0, 231, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_timkiem = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_timkiem.setFlat(False)
        self.btn_timkiem.setObjectName("btn_timkiem")
        self.horizontalLayout.addWidget(self.btn_timkiem)
        self.btn_xemtatca = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btn_xemtatca.setFlat(False)
        self.btn_xemtatca.setObjectName("btn_xemtatca")
        self.horizontalLayout.addWidget(self.btn_xemtatca)
        self.tableteacher = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableteacher.setGeometry(QtCore.QRect(5, 71, 831, 451))
        self.tableteacher.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableteacher.setObjectName("tableteacher")
        self.tableteacher.setColumnCount(3)
        self.tableteacher.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableteacher.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableteacher.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableteacher.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Teacher)
        QtCore.QMetaObject.connectSlotsByName(Teacher)

    def retranslateUi(self, Teacher):
        _translate = QtCore.QCoreApplication.translate
        Teacher.setWindowTitle(_translate("Teacher", "Form"))
        self.lb_main.setText(_translate("Teacher", "QUẢN LÝ THÔNG TIN GIẢNG VIÊN"))
        self.lb_hoten.setText(_translate("Teacher", "ID giảng viên"))
        self.lb_namsinh.setText(_translate("Teacher", "Họ tên"))
        self.lb_sdt.setText(_translate("Teacher", "SĐT"))
        self.lb_thongtin.setText(_translate("Teacher", "THÔNG TIN GIẢNG VIÊN"))
        self.btn_luu.setText(_translate("Teacher", "Lưu"))
        self.btn_sua.setText(_translate("Teacher", "Sửa"))
        self.btn_xoa.setText(_translate("Teacher", "Xóa"))
        self.btn_reset.setText(_translate("Teacher", "Làm mới"))
        self.lb_thongtin_2.setText(_translate("Teacher", "Tìm kiếm theo :"))
        self.comboBoxtimkiem.setItemText(0, _translate("Teacher", "Id"))
        self.comboBoxtimkiem.setItemText(1, _translate("Teacher", "Họ tên"))
        self.comboBoxtimkiem.setItemText(2, _translate("Teacher", "SĐT"))
        self.btn_timkiem.setText(_translate("Teacher", "Tìm kiếm"))
        self.btn_xemtatca.setText(_translate("Teacher", "Xem tất cả"))
        item = self.tableteacher.horizontalHeaderItem(0)
        item.setText(_translate("Teacher", "ID"))
        item = self.tableteacher.horizontalHeaderItem(1)
        item.setText(_translate("Teacher", "Họ tên"))
        item = self.tableteacher.horizontalHeaderItem(2)
        item.setText(_translate("Teacher", "SDT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Teacher = QtWidgets.QWidget()
    ui = Ui_Teacher()
    ui.setupUi(Teacher)
    Teacher.show()
    sys.exit(app.exec())
