from dal.account_dal import *

class TeacherBUS:
     def getList():
          return TeacherDAL.getList()
     def addlist (giangvien):
          return TeacherDAL.addlist(giangvien)