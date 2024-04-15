from dal.class_dal import *

class ClassBUS:
    
    def get_all():
        return classDAL.getList()
    def getIdLop(tenLop):
        return classDAL.getIDLop(tenLop)
