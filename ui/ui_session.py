# Form implementation generated from reading ui file 'sesson.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Session(object):
    def setupUi(self, Session):
        Session.setObjectName("Session")
        Session.resize(1399, 762)
        # Session.setMaximumSize(QtCore.QSize(1440, 800))
        self.frame = QtWidgets.QFrame(parent=Session)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.frame.setStyleSheet("\n"
"QPushButton{\n"
"    padding: 5px 5px;\n"
"    background-color: white;\n"
"}\n"
"#gridLayout{\n"
"    border: 1px solid black;\n"
"}"
"QTextEdit{\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton, QComboBox, QDateEdit{\n"
"    font-size: 14px;\n"
"}"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_title = QtWidgets.QLabel(parent=self.frame)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 1400, 61))
        self.label_title.setStyleSheet("")
        self.label_title.setObjectName("label_title")
        self.tt = QtWidgets.QFrame(parent=self.frame)
        self.tt.setGeometry(QtCore.QRect(10 , 60, 500, 601))
        self.tt.setStyleSheet("#tt{\n"
"    border: 2px solid grey;\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 5px;\n"
"    background-color: white;\n"
"}\n"
"#gridLayout{\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.tt.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tt.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tt.setObjectName("tt")
        self.label = QtWidgets.QLabel(parent=self.tt)
        self.label.setGeometry(QtCore.QRect(10, 10, 490, 41))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.tt)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tt)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tt)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 91, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tt)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 51, 41))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.tt)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 51, 41))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.tt)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 91, 41))
        self.label_9.setObjectName("label_9")
        self.txt_maBH = QtWidgets.QTextEdit(parent=self.tt)
        self.txt_maBH.setGeometry(QtCore.QRect(150, 70, 310, 41))
        self.txt_maBH.setObjectName("txt_maBH")
        self.txt_gioBD = QtWidgets.QTextEdit(parent=self.tt)
        self.txt_gioBD.setGeometry(QtCore.QRect(150, 190, 310, 41))
        self.txt_gioBD.setObjectName("txt_gioBD")
        self.txt_gioKT = QtWidgets.QTextEdit(parent=self.tt)
        self.txt_gioKT.setGeometry(QtCore.QRect(150, 250, 310, 41))
        self.txt_gioKT.setObjectName("txt_gioKT")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.tt)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 470, 460, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_them = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setMinimumHeight(41)
        self.horizontalLayout.addWidget(self.btn_them)
        self.btn_sua = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setMinimumHeight(41)
        self.horizontalLayout.addWidget(self.btn_sua)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_xoa.setMinimumHeight(41)
        self.horizontalLayout.addWidget(self.btn_xoa)
        self.btn_lammoi = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_lammoi.setObjectName("btn_lammoi")
        self.btn_lammoi.setMinimumHeight(41)
        self.horizontalLayout.addWidget(self.btn_lammoi)
        self.ngayHoc = QtWidgets.QDateEdit(parent=self.tt)
        self.ngayHoc.setGeometry(QtCore.QRect(150, 310, 310, 41))
        self.ngayHoc.setObjectName("ngayHoc")
        self.cb_mh = QtWidgets.QComboBox(parent=self.tt)
        self.cb_mh.setGeometry(QtCore.QRect(150, 130, 310, 41))
        self.cb_mh.setObjectName("cb_mh")
        self.cb_mh.addItem("")
        self.txt_tuan = QtWidgets.QTextEdit(parent=self.tt)
        self.txt_tuan.setGeometry(QtCore.QRect(150, 370, 310, 41))
        self.txt_tuan.setObjectName("txt_tuan")
        self.frame1 = QtWidgets.QFrame(parent=self.frame)
        self.frame1.setGeometry(QtCore.QRect(520, 60, 860, 601))
        self.frame1.setStyleSheet("#table_bh{\n"
"    background-color: rgb(255, 255, 255);\n"
"}"
"#frame1 {\n"
"    border: 2px solid grey;\n"
"}\n")
        self.frame1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame1.setObjectName("frame1")
        # self.label_10 = QtWidgets.QLabel(parent=self.frame1)
        # self.label_10.setGeometry(QtCore.QRect(10, 20, 91, 31))
        # self.label_10.setObjectName("label_10")
        self.cb_timkiem = QtWidgets.QComboBox(parent=self.frame1)
        self.cb_timkiem.setGeometry(QtCore.QRect(10, 20, 140, 41))
        self.cb_timkiem.setObjectName("cb_timkiem")
        self.cb_timkiem.addItem("")
        self.cb_timkiem.addItem("")
        self.txt_timkiem = QtWidgets.QTextEdit(parent=self.frame1)
        self.txt_timkiem.setGeometry(QtCore.QRect(160, 20, 300, 41))
        self.txt_timkiem.setObjectName("txt_timkiem")
        self.btn_timkiem = QtWidgets.QPushButton(parent=self.frame1)
        self.btn_timkiem.setGeometry(QtCore.QRect(470, 20, 111, 41))
        self.btn_timkiem.setObjectName("btn_timkiem")
        self.table_bh = QtWidgets.QTableWidget(parent=self.frame1)
        self.table_bh.setGeometry(QtCore.QRect(10, 70, 830, 510))
        self.table_bh.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_bh.setObjectName("table_bh")
        self.table_bh.setColumnCount(8)
        self.table_bh.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bh.setHorizontalHeaderItem(7, item)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setGeometry(QtCore.QRect(0, 50, 1400, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Session)
        QtCore.QMetaObject.connectSlotsByName(Session)

    def retranslateUi(self, Session):
        _translate = QtCore.QCoreApplication.translate
        Session.setWindowTitle(_translate("Session", "Form"))
        self.label_title.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\"color:red; font-weight: bold; font-size:25px;\">QUẢN LÝ THÔNG TIN BUỔI HỌC</span></p></body></html>"))
        self.label.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:20px; font-weight:600;\">THÔNG TIN BUỔI HỌC</span></p></body></html>"))
        self.label_2.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mã buổi học</span></p></body></html>"))
        self.label_3.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tiết bắt đầu</span></p></body></html>"))
        self.label_4.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tiết kết thúc</span></p></body></html>"))
        self.label_5.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Ngày</span></p></body></html>"))
        self.label_7.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tuần</span></p></body></html>"))
        self.label_9.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tên môn học</span></p></body></html>"))
        self.btn_them.setText(_translate("Session", "Thêm mới"))
        self.btn_sua.setText(_translate("Session", "Cập nhật"))
        self.btn_xoa.setText(_translate("Session", "Xóa"))
        self.btn_lammoi.setText(_translate("Session", "Làm mới"))
        self.txt_maBH.setEnabled(False)
        self.txt_maBH.setPlaceholderText(_translate("Session", "Mã buổi học"))
        self.txt_gioBD.setPlaceholderText(_translate("Session", "Nhập tiết bắt đầu"))
        self.txt_gioKT.setPlaceholderText(_translate("Session", "Nhập tiết kết thúc"))
        self.txt_tuan.setPlaceholderText(_translate("Session", "Nhập tuần"))
        # self.label_10.setText(_translate("Session", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tìm kiếm theo:</span></p></body></html>"))
        self.cb_mh.setItemText(0, _translate("Session", "Môn học"))
        self.cb_timkiem.setItemText(0, _translate("Session", "Tên môn học"))
        self.cb_timkiem.setItemText(1, _translate("Session", "Giảng viên"))
        self.btn_timkiem.setText(_translate("Session", "Tìm kiếm"))
        item = self.table_bh.horizontalHeaderItem(0)
        item.setText(_translate("Session", "Mã buổi học"))
        item = self.table_bh.horizontalHeaderItem(1)
        item.setText(_translate("Session", "Tên môn học"))
        item = self.table_bh.horizontalHeaderItem(2)
        item.setText(_translate("Session", "Tuần"))
        item = self.table_bh.horizontalHeaderItem(3)
        item.setText(_translate("Session", "Giảng viên"))
        item = self.table_bh.horizontalHeaderItem(4)
        item.setText(_translate("Session", "Tiết bắt đầu"))
        item = self.table_bh.horizontalHeaderItem(5)
        item.setText(_translate("Session", "Tiết kết thúc"))
        item = self.table_bh.horizontalHeaderItem(6)
        item.setText(_translate("Session", "Ngày"))
        item = self.table_bh.horizontalHeaderItem(7)
        item.setText(_translate("Session", "Lớp"))
        self.table_bh.setColumnWidth(1, 130)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Session = QtWidgets.QWidget()
    ui = Ui_Session()
    ui.setupUi(Session)
    Session.show()
    sys.exit(app.exec())
