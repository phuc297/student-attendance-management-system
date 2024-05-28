import mysql.connector as mdb
from dto.class_dto import *
from . db_connector import *

class classDAL:

    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from lop")          

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
    
    def getTenLop(maLop):
        try:
            conn= DatabaseConnector()
            db= conn.connect()
            cursor =db.cursor()
            sql="SELECT tenLop FROM lop WHERE maLop =%s"
            cursor.execute(sql,(maLop,))
            maLop=cursor.fetchone()
            if maLop:
                return maLop[0]
            else:
                return None
        except Exception as e:
            print("lỗi kết nối: ",e)
            return False
        finally:
            cursor.close()
            db.close()
    
    def getIDLop(tenLop):
        try:
            conn= DatabaseConnector()
            db= conn.connect()
            cursor =db.cursor()
            sql="SELECT maLop FROM lop WHERE tenLop =%s"
            cursor.execute(sql,(tenLop,))
            maLop=cursor.fetchone()
            if maLop:
                return maLop[0]
            else:
                return None
        except Exception as e:
            print("lỗi kết nối: ",e)
            return False
        finally:
            cursor.close()
            db.close()
    
    def addClass(tenlop):
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql = "INSERT INTO lop(tenLop) VALUES(%s)"
            # print(sql)
            cursor.execute(sql, (tenlop,))
            db.commit()
            return True
        except Exception as e:
            print("Lỗi kết nối: ", e)
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'db' in locals():
                db.close()
        


    def deleteClass(maLop):
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()

            # Sử dụng các truy vấn riêng biệt thay vì kết hợp chúng trong một chuỗi
            query_monhoc = "UPDATE monhoc SET malop = NULL WHERE malop = %s"
            query_sinhvien = "UPDATE sinhvien SET malop = NULL WHERE malop = %s"
            query_lop = "DELETE FROM lop WHERE maLop = %s"

            # Thực thi từng truy vấn một
            cursor.execute(query_monhoc, (maLop,))
            cursor.execute(query_sinhvien, (maLop,))
            cursor.execute(query_lop, (maLop,))

            db.commit()
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False
            
        finally:
            # Đảm bảo rằng cursor và kết nối được đóng trong mệnh đề finally
            if cursor:
                cursor.close()
            if db:
                db.close()
                
    def updateClass(classDTO):
        try:
            conn= DatabaseConnector()
            db= conn.connect()
            cursor =db.cursor()
            sql="UPDATE lop SET tenLop = %s WHERE maLop = %s"
            cursor.execute(sql,(classDTO.tenLop, classDTO.maLop))
            db.commit()
            return True
        except Exception as e:
            print("lỗi kết nối: ",e)
            return False
        finally:
            cursor.close()
            db.close()