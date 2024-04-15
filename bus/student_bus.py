from dal.student_dal import *

class StudentBUS:
    
    def getList():
        return StudentDAL.getList()
    def add(student):
        return StudentDAL.add(student)
    def delete(masv):
        return StudentDAL.delete(masv)
    def update(student):
        return StudentDAL.update(student)