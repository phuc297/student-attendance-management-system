from dal.teacher_dal import *

class TeacherBUS:
     def getList():
          return TeacherDAL.getList()
     def getHoTen(magv):
          return TeacherDAL.getHoTen(magv)
     def add(hoTen, gioitinh, cmnd, ngaysinh, email, sdt, maTK):
          return TeacherDAL.add(hoTen, gioitinh, cmnd, ngaysinh, email, sdt, maTK)
     def delete(maGV):
          return TeacherDAL.delete(maGV)
     def update(giangvien):
          return TeacherDAL.update(giangvien)
     def checkAccount(maTK):
          return TeacherDAL.checkAccount(maTK)