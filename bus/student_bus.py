from dal.student_dal import *

class StudentBUS:
    
    def getList():
        return StudentDAL.getList()
    def get(masv):
        return StudentDAL.get(masv)
    def getHoTen(masv):
        return StudentDAL.getHoTen(masv)
    def add(student):
        return StudentDAL.add(student)
    def delete(masv):
        return StudentDAL.delete(masv)
    def update(student):
        return StudentDAL.update(student)