class Student:
    def __init__(self, masv, hoten, malop, cmnd, gioitinh, ngaysinh, email, sdt):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.cmnd = cmnd
        self.gioitinh = gioitinh
        self.ngaysinh = ngaysinh
        self.email = email
        self.sdt = sdt

    def show(self):
        print(f"{self.masv} {self.hoten} {self.malop} {self.cmnd} {self.gioitinh} {self.ngaysinh} {self.email} {self.sdt}")