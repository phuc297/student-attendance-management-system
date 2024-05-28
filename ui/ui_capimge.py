# Form implementation generated from reading ui file '.\student_image.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StudentImage(object):
    def setupUi(self, StudentImage):
        StudentImage.setObjectName("StudentImage")
        StudentImage.resize(1017, 568)
        self.frame = QtWidgets.QFrame(parent=StudentImage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1021, 571))
        self.frame.setStyleSheet("#frame{\n"
"    background-color: #D5EDF9;\n"
"}\n"
"#grbx_thongtin{\n"
"    background-color: white;\n"
"    color: #5442B1;\n"
"    font-size: 25px;\n"
"    border: 3px solid #5442B1;\n"
"    border-radius: 10px\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.grbx_thongtin = QtWidgets.QGroupBox(parent=self.frame)
        self.grbx_thongtin.setGeometry(QtCore.QRect(40, 30, 931, 521))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.grbx_thongtin.setFont(font)
        self.grbx_thongtin.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.grbx_thongtin.setAutoFillBackground(False)
        self.grbx_thongtin.setStyleSheet("font-size:14px")
        self.grbx_thongtin.setTitle("")
        self.grbx_thongtin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grbx_thongtin.setFlat(False)
        self.grbx_thongtin.setCheckable(False)
        self.grbx_thongtin.setObjectName("grbx_thongtin")
        self.lb_hinhanh = QtWidgets.QLabel(parent=self.grbx_thongtin)
        self.lb_hinhanh.setGeometry(QtCore.QRect(370, 100, 250, 250))
        self.lb_hinhanh.setStyleSheet("border: 1px solid black;\n"
"")
        self.lb_hinhanh.setText("")
        self.lb_hinhanh.setObjectName("lb_hinhanh")
        self.splitter = QtWidgets.QSplitter(parent=self.grbx_thongtin)
        self.splitter.setGeometry(QtCore.QRect(650, 370, 241, 51))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_2.setStyleSheet("font-size: 14px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lb_hinhanh_2 = QtWidgets.QLabel(parent=self.grbx_thongtin)
        self.lb_hinhanh_2.setGeometry(QtCore.QRect(640, 100, 250, 250))
        self.lb_hinhanh_2.setStyleSheet("border: 1px solid black;\n"
"")
        self.lb_hinhanh_2.setText("")
        self.lb_hinhanh_2.setObjectName("lb_hinhanh_2")
        self.label = QtWidgets.QLabel(parent=self.grbx_thongtin)
        self.label.setGeometry(QtCore.QRect(370, 360, 251, 20))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.grbx_thongtin)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 470, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.grbx_thongtin)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 450, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(parent=self.grbx_thongtin)
        self.listWidget.setGeometry(QtCore.QRect(60, 100, 291, 341))
        self.listWidget.setStyleSheet("font-size:20px")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.grbx_thongtin)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 470, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(parent=self.grbx_thongtin)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 921, 61))
        self.label_2.setStyleSheet("font-size:25px;\n"
"font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(StudentImage)
        QtCore.QMetaObject.connectSlotsByName(StudentImage)

    def retranslateUi(self, StudentImage):
        _translate = QtCore.QCoreApplication.translate
        StudentImage.setWindowTitle(_translate("StudentImage", "Form"))
        self.pushButton.setText(_translate("StudentImage", "Mở/ Đóng camera"))
        self.pushButton_2.setText(_translate("StudentImage", "Chụp ảnh"))
        self.label.setText(_translate("StudentImage", "Xem trước hình ảnh"))
        self.pushButton_3.setText(_translate("StudentImage", "Đóng"))
        self.pushButton_4.setText(_translate("StudentImage", "Xóa"))
        self.pushButton_5.setText(_translate("StudentImage", "Xác nhận"))
        self.label_2.setText(_translate("StudentImage", "HÌNH ẢNH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentImage = QtWidgets.QWidget()
    ui = Ui_StudentImage()
    ui.setupUi(StudentImage)
    StudentImage.show()
    sys.exit(app.exec())
