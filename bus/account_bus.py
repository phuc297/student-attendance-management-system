from dal.account_dal import *

class AccountBUS:
     def getList():
          return AccountDAL.getList()
     def add(account):
          return AccountDAL.add(account)
     def delete(matk):
          return AccountDAL.delete(matk)
     def update(account):
          return AccountDAL.update(account)