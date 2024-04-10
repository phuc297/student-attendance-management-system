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
        self.txt_username = QtWidgets.QTextEdit(parent=self.frame)
        self.txt_username.setGeometry(QtCore.QRect(430, 70, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.lb_username = QtWidgets.QLabel(parent=self.frame)
        self.lb_username.setGeometry(QtCore.QRect(260, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_username.setFont(font)
        self.lb_username.setObjectName("lb_username")
        self.lb_password = QtWidgets.QLabel(parent=self.frame)
        self.lb_password.setGeometry(QtCore.QRect(260, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_password.setFont(font)
        self.lb_password.setObjectName("lb_password")
        self.txt_password = QtWidgets.QTextEdit(parent=self.frame)
        self.txt_password.setGeometry(QtCore.QRect(430, 120, 321, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_password.setFont(font)
        self.txt_password.setObjectName("txt_password")
        self.btnUpdatte = QtWidgets.QPushButton(parent=self.frame)
        self.btnUpdatte.setGeometry(QtCore.QRect(520, 180, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdatte.sizePolicy().hasHeightForWidth())
        self.btnUpdatte.setSizePolicy(sizePolicy)
        self.btnUpdatte.setStyleSheet("border: 1px solid black;")
        self.btnUpdatte.setObjectName("btnUpdatte")
        self.btnDelete = QtWidgets.QPushButton(parent=self.frame)
        self.btnDelete.setGeometry(QtCore.QRect(650, 180, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setStyleSheet("border: 1px solid black;")
        self.btnDelete.setObjectName("btnDelete")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(190, 270, 991, 371))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "Form"))
        self.lb_main.setText(_translate("Account", "QUẢN LÝ TÀI KHOẢN"))
        self.lb_username.setText(_translate("Account", "Tên tài khoản"))
        self.lb_password.setText(_translate("Account", "Mật khẩu"))
        self.btnUpdatte.setText(_translate("Account", "Cập nhật"))
        self.btnDelete.setText(_translate("Account", "Xóa"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Account", "Tên tài khoản"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Account", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Account", "Mật khẩu"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Account", "Quyền"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QWidget()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())
