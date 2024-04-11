
class Teacher:
    def __init__(self, maGV, hoTen, SDT):
        self.maGV = maGV
        self.hoTen = hoTen
        self.SDT = SDT
    def __init__(self, hoTen, SDT):
        self.hoTen = hoTen
        self.SDT = SDT
    
    def print_info(self):
        print("Thông tin giảng viên:")
        print("Mã giảng viên:", self.maGV)
        print("Họ và tên:", self.hoTen)
        print("Số điện thoại:", self.SDT)