
class Teacher:
    def __init__(self, maGV, hoTen, gioitinh,cmnd,ngaysinh,email,sdt,maTK):
        self.maGV = maGV
        self.hoTen = hoTen
        self.gioitinh= gioitinh
        self.cmnd = cmnd
        self.ngaysinh= ngaysinh
        self.email = email
        self.sdt= sdt
        self.maTK= maTK
  
    
    def print_info(self):
        print("Thông tin giảng viên:")
        print("Mã giảng viên:", self.maGV)
        print("Họ và tên:", self.hoTen)
        