from dal.teacher_dal import *

class TeacherBUS:
     def getList():
          return TeacherDAL.getList()
     def add(giangvien):
          return TeacherDAL.add(giangvien)
     def delete(maGV):
          return TeacherDAL.delete(maGV)
     def update(giangvien):
          return TeacherDAL.update(giangvien)