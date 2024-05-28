class Attendence:
    def __init__(self, maBH, maSV, hoTen, gioVao):
        self.maSV= maSV
        self.gioVao= gioVao
        self.maBH= maBH
        self.hoTen= hoTen

    def show(self):
        print(f"{self.maDD} {self.maSV} {self.gioVao} {self.gioRa} {self.maBH}")