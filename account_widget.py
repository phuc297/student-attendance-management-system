from ui.ui_account import *
from bus.account_bus import *
from PyQt6.QtWidgets import QMessageBox

class AccountWidget(Ui_Account):

    def __init__(self, page):
        self.setupUi(page)
        self.list = AccountBUS.getList()
        self.loadList()
        self.tbAccount.itemClicked.connect(lambda: self.tableEvent())
        self.btn_them.clicked.connect(lambda: self.addAccount())
        self.btn_xoa.clicked.connect(self.deleteAccount)
        self.btn_sua.clicked.connect(self.updateAccount)
        self.btn_search.clicked.connect(self.search)
        
    def loadList(self):
        if list is not None:
            self.tbAccount.setRowCount(len(self.list))
            tablerow = 0
            for row in self.list:
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
                self.clear()
            else:
                dlg.setText("Thêm thất bại")
                self.clear()
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
                self.clear()
            else:
                dlg.setText("Xóa thất bại")
                self.clear()
                dlg.exec()
        except Exception as e:
            print(e)
        
    def clear (self):
       self.txtId.clear()
       self.txtPassword.clear()
       self.txtTeacher.clear()
       self.txtUsername.clear()
       

    def updateAccount(self):
        try:
            acc = Account(self.txtId.toPlainText(), self.txtUsername.toPlainText(), self.txtPassword.toPlainText(), self.txtTeacher.toPlainText())
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo!")
            dlg.setStyleSheet("QLabel{min-width: 100px;}")
            if AccountBUS.update(acc) == True:
                dlg.setText("Sửa thành công")
                dlg.exec()
                self.loadList()
                self.clear()
            else:
                dlg.setText("Sửa thất bại")
                self.clear()
                dlg.exec()
        except Exception as e:
            print(e)
        pass
    
    def search(self, s):
        search_text = self.txt_search.toPlainText()

        for row in range(self.tbAccount.rowCount()):
            item = self.tbAccount.item(row, 1)
            if item is not None:
                cell_text = item.text().lower()
                if search_text.lower() in cell_text:
                    self.tbAccount.setRowHidden(row, False)
                else:
                    self.tbAccount.setRowHidden(row, True)