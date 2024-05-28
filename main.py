from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from bus.account_bus import *
import sys
import os
from ui import *
from menu_form import *

class MainProgram(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_login.clicked.connect(self.openMainMenu)
    
    def openMainMenu(self):
        listtk=[]
        listtk=AccountBUS.getList()
        tentk=self.ui.txt_taikhoan.text()
        mk=self.ui.txt_matkhau.text()
        if tentk and mk is not None:
            dangnhap = False
            for tk in listtk:
                if tk[1] == tentk and tk[2] == mk: 
                    self.newwindow = QMainWindow()
                    self.ui_menu = MenuForm()
                    self.ui_menu.setupUi(self.newwindow)
                    self.ui_menu.initialize()
                    self.hide()
                    self.newwindow.show()
                    dangnhap=True
                    break
            if dangnhap is False:
                messagebox.showinfo('Lỗi đăng nhập','Thông tin tài khoản hoặc mật khẩu chưa chính xác !')
        else:
            messagebox.showinfo('Lỗi đăng nhập','Bạn chưa nhập đầy đủ thông tin !')
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainProgram()
    sys.exit(app.exec())

