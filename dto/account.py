class Account:
    def __init__(self,maTK, tenTK, matkhau,loaiTK):
        self.maTK =maTK
        self.tenTK = tenTK
        self.matkhau = matkhau
        self.loaiTK = loaiTK

    def show(self):
        print(f"{self.maTK} {self.tenTK} {self.matkhau} {self.loaiTK}")