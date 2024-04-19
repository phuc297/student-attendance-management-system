from ui.ui_account import *
from bus.account_bus import *
from PyQt6.QtWidgets import QMessageBox

class AccountWidget(Ui_Account):

    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tbAccount.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(lambda: self.addAccount())
        self.btn_xoa.clicked.connect(self.deleteAccount)
        self.btn_sua.clicked.connect(self.updateAccount)
        
    def loadList(self):
        list = AccountBUS.getList()
        self.tbAccount.setRowCount(len(list))
        tablerow = 0
        if list is not None:
            for row in list:
                self.tbAccount.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbAccount.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tbAccount.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tbAccount.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tablerow += 1
    
    def tableEvent(self):
        cr = self.tbAccount.currentRow()
        self.txtId.setText(self.tbAccount.item(cr, 0).text())
        self.txtUsername.setText(self.tbAccount.item(cr, 1).text())
        self.txtPassword.setText(self.tbAccount.item(cr, 2).text())
        self.txtTeacher.setText(self.tbAccount.item(cr, 3).text())

    def addAccount(self):
        try:
            acc = Account(0, self.txtUsername.toPlainText(), self.txtPassword.toPlainText(), self.txtTeacher.toPlainText())
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 100px;}")
            if AccountBUS.add(acc) == True:
                dlg.setText("Thêm thành công")
                dlg.exec()
                self.loadList()
            else:
                dlg.setText("Thêm thất bại")
                dlg.exec()
        except Exception as e:
            print(e)


    def deleteAccount(self, s):
        try:
            cr = self.tbAccount.currentRow()
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 100px;}")
            if AccountBUS.delete(self.tbAccount.item(cr, 0).text()) == True:
                dlg.setText("Xóa thành công")
                dlg.exec()
                self.loadList()
            else:
                dlg.setText("Xóa thất bại")
                dlg.exec()
        except Exception as e:
            print(e)
        
        

    def updateAccount(self):
        pass