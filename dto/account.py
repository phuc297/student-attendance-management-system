class Account:
    def __init__(self, matk, email, matkhau, maGV):
        self.matk = matk
        self.email = email
        self.matkhau = matkhau
        self.maGV = maGV

    def show(self):
        print(f"{self.matk} {self.email} {self.matkhau} {self.maGV}")