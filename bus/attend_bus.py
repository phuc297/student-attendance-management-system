
from dal.attend_dal import *
from dto.attendence import *


class AttendBUS:
    def getList(maBH):
        return AttendDAL.getList(maBH)
    
    def check(maSV, maBH):
        return AttendDAL.check(maSV, maBH)
    
    def add(maBH, maSV, gioVao, trangthai, chitiet):
        return AttendDAL.add(maBH, maSV, gioVao, trangthai, chitiet)

    def delete2(maBH, maSV):
        return AttendDAL.delete2(maBH, maSV)

    def delete(maDD):
        return AttendDAL.delete(maDD)
        