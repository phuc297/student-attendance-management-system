from dto.account import *
from . db_connector import *

class AccountDAL:
    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select maTK, matKhau from taikhoan")          

            for x in cursor:
                list.append(x)
        except Exception as e:
            print(e)
        try:
            cursor.close()
            db.close()
        except:
            pass
        return list
    def add(account):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="insert into taikhoan(maGV,hoTen,SDT) VALUES (%s, %s)"
            cursor.execute(sql,(account.matk,account.matkhau))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
        




