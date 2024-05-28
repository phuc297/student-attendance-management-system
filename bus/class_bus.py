from dal.class_dal import *

class ClassBUS:
    
    def get_all():
        return classDAL.getList()
    def getTenLop(maLop):
        return classDAL.getTenLop(maLop)
    def getIdLop(tenLop):
        return classDAL.getIDLop(tenLop)
    def addClass(maLop,tenLop):
        return classDAL.addClass(maLop,tenLop)
    def delete(maLop):
        return classDAL.deleteClass(maLop)
    def add(tenlop):
        return classDAL.addClass(tenlop)
    def update(classDTO):
        return classDAL.updateClass(classDTO)