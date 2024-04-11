from dal.teacher_dal import *

class TeacherBUS:
     def getList():
          return TeacherDAL.getList()
     def addlist (giangvien):
          return TeacherDAL.addlist(giangvien)
     def delete(maGV):
          return TeacherDAL.delete(maGV)
     def update(giangvien):
          return TeacherDAL.update(giangvien)