from dal.student_dal import *

class StudentBUS:
    
    def getList():
        return StudentDAL.getList()