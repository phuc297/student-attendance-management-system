class Account:
    def __init__(self, matk, matkhau, email, quyen):
        self.matk = matk
        self.matkhau = matkhau
        self.email = email
        self.quyen = quyen

    def show(self):
        print(f"{self.matk} {self.matkhau} {self.email} {self.quyen}")