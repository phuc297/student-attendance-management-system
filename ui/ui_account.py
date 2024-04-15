# Form implementation generated from reading ui file '.\account.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(1400, 800)
        self.frame = QtWidgets.QFrame(parent=Account)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.frame.setStyleSheet("QPushButton{\n"
"    padding: 15px 5px;\n"
"    background-color: #D5EDF9;\n"
"    border-color: black;\n"
"}")
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
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setGeometry(QtCore.QRect(0, 50, 1400, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 70, 431, 691))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    border: 1px solid black\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 340, 381, 47))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_them = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_them.setObjectName("btn_them")
        self.horizontalLayout_2.addWidget(self.btn_them)
        self.btn_sua = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_sua.setObjectName("btn_sua")
        self.horizontalLayout_2.addWidget(self.btn_sua)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.horizontalLayout_2.addWidget(self.btn_xoa)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(110, 20, 191, 51))
        self.label.setObjectName("label")
        self.txtPassword = QtWidgets.QTextEdit(parent=self.frame_2)
        self.txtPassword.setGeometry(QtCore.QRect(180, 230, 191, 31))
        self.txtPassword.setObjectName("txtPassword")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 101, 31))
        self.label_4.setObjectName("label_4")
        self.txtTeacher = QtWidgets.QTextEdit(parent=self.frame_2)
        self.txtTeacher.setGeometry(QtCore.QRect(180, 280, 191, 31))
        self.txtTeacher.setObjectName("txtTeacher")
        self.txtUsername = QtWidgets.QTextEdit(parent=self.frame_2)
        self.txtUsername.setGeometry(QtCore.QRect(180, 180, 191, 31))
        self.txtUsername.setObjectName("txtUsername")
        self.txtId = QtWidgets.QTextEdit(parent=self.frame_2)
        self.txtId.setGeometry(QtCore.QRect(180, 130, 191, 31))
        self.txtId.setReadOnly(True)
        self.txtId.setObjectName("txtId")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 101, 31))
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(480, 70, 891, 691))
        self.frame_3.setStyleSheet("#frame_3{\n"
"    border: 1px solid black\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_search = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_search.setGeometry(QtCore.QRect(520, 20, 91, 41))
        self.btn_search.setObjectName("btn_search")
        self.txt_search = QtWidgets.QTextEdit(parent=self.frame_3)
        self.txt_search.setGeometry(QtCore.QRect(320, 30, 181, 31))
        self.txt_search.setObjectName("txt_search")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(50, 30, 101, 31))
        self.label_5.setObjectName("label_5")
        self.cbx_tksinhvien = QtWidgets.QComboBox(parent=self.frame_3)
        self.cbx_tksinhvien.setGeometry(QtCore.QRect(160, 30, 101, 31))
        self.cbx_tksinhvien.setObjectName("cbx_tksinhvien")
        self.tbAccount = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tbAccount.setGeometry(QtCore.QRect(30, 90, 831, 561))
        self.tbAccount.setStyleSheet("")
        self.tbAccount.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tbAccount.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbAccount.setLineWidth(1)
        self.tbAccount.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbAccount.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tbAccount.setObjectName("tbAccount")
        self.tbAccount.setColumnCount(4)
        self.tbAccount.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAccount.setHorizontalHeaderItem(3, item)
        self.tbAccount.horizontalHeader().setDefaultSectionSize(200)
        self.tbAccount.verticalHeader().setDefaultSectionSize(30)
        self.tbAccount.verticalHeader().setMinimumSectionSize(30)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "Form"))
        self.lb_main.setText(_translate("Account", "QUẢN LÝ TÀI KHOẢN"))
        self.btn_them.setText(_translate("Account", "Thêm mới"))
        self.btn_sua.setText(_translate("Account", "Cập nhật"))
        self.btn_xoa.setText(_translate("Account", "Xóa"))
        self.label_2.setText(_translate("Account", "<html><head/><body><p align=\"left\"><span style=\" font-size:10pt; font-weight:600;\">Tên tài khoản</span></p></body></html>"))
        self.label.setText(_translate("Account", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Thông tin tài khoản</span></p></body></html>"))
        self.label_3.setText(_translate("Account", "<html><head/><body><p align=\"left\"><span style=\" font-size:10pt; font-weight:600;\">Mật khẩu</span></p></body></html>"))
        self.label_4.setText(_translate("Account", "<html><head/><body><p align=\"left\"><span style=\" font-size:10pt; font-weight:600;\">Giảng viên</span></p></body></html>"))
        self.label_6.setText(_translate("Account", "<html><head/><body><p align=\"left\"><span style=\" font-size:10pt; font-weight:600;\">Mã tài khoản</span></p></body></html>"))
        self.btn_search.setText(_translate("Account", "Tìm kiếm"))
        self.label_5.setText(_translate("Account", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Tìm kiếm theo:</span></p></body></html>"))
        item = self.tbAccount.verticalHeaderItem(0)
        item.setText(_translate("Account", "1"))
        item = self.tbAccount.verticalHeaderItem(1)
        item.setText(_translate("Account", "2"))
        item = self.tbAccount.verticalHeaderItem(2)
        item.setText(_translate("Account", "3"))
        item = self.tbAccount.verticalHeaderItem(3)
        item.setText(_translate("Account", "4"))
        item = self.tbAccount.horizontalHeaderItem(0)
        item.setText(_translate("Account", "Mã tài khoản"))
        item = self.tbAccount.horizontalHeaderItem(1)
        item.setText(_translate("Account", "Tên tài khoản"))
        item = self.tbAccount.horizontalHeaderItem(2)
        item.setText(_translate("Account", "Mật khẩu"))
        item = self.tbAccount.horizontalHeaderItem(3)
        item.setText(_translate("Account", "Mã giảng viên"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QWidget()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())
