import mysql.connector as mdb
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


