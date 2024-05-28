from dto.account import *
from . db_connector import *

class AccountDAL:
    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from taikhoan")          

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
            sql="insert into taikhoan(tenTK, matKhau, loaiTK) VALUES (%s, %s, %s)"
            cursor.execute(sql,(account.tenTK, account.matkhau, account.loaiTK))
            db.commit()
           
            return True
        except Exception as e:
            print("Lỗi",e)
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return False
    
    def update(account):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""update taikhoan set tenTK=%s ,matKhau=%s ,loaiTK=%s where maTK=%s """
            cursor.execute(sql,(account.tenTK, account.matkhau, account.loaiTK,account.maTK))
            db.commit()
           
            return True
        except Exception as e:
            print("Lỗi",e) 
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return False

    def delete(maTK):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="delete from taikhoan where maTK=%s"
            cursor.execute(sql,(maTK,))
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
        




