from ui.ui_account import *
from bus.account_bus import *

class AccountWidget(Ui_Account):

    def __init__(self, page):
        self.setupUi(page)
        self.loadList()
        self.tbAccount.itemClicked.connect(lambda: self.tableEvent())
        
    def loadList(self):
        list = AccountBUS.getList()
        self.tbAccount.setRowCount(len(list))
        tablerow = 0
        if list is not None:
            for row in list:
                self.tbAccount.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tbAccount.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                tablerow += 1
        print(list)
    
    def tableEvent(self):
        cr = self.tbAccount.currentRow()
        self.txt_username.setText(self.tbAccount.item(cr, 0).text())
        self.txt_password.setText(self.tbAccount.item(cr, 1).text())

    def update(self):
        pass