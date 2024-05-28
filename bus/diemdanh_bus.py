from dal.diemdanh_dal import *

class DiemdanhBUS:
    def getlist():
        return DiemdanhDAL.getlist()    
    def getlistdimuon():
        return DiemdanhDAL.getlistdimuon()
    def getListVang(): 
        return DiemdanhDAL.getListVang()
       
    def getList():
        return DiemdanhDAL.getList()   
    
    def update(maDD, gioVao, gioRa, chitiet):
        return DiemdanhDAL.update(maDD, gioVao, gioRa, chitiet)
    def delete(maDD):
        return DiemdanhDAL.delete(maDD)