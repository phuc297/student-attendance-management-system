import mysql.connector as mdb
from . db_connector import *


class subjectDAL:

    

    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from monhoc")          

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
    

    def add(subject):
       
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="insert into monhoc(tenMH,maGV) VALUES (%s, %s)"
            cursor.execute(sql,(subject.tenMH, subject.maGV))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
            
    
    
    def update(subject):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="update monhoc set tenMH=%s, maGV=%s  where maMH=%s"
            cursor.execute(sql,(subject.tenMH, subject.maGV, subject.maMH))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
            
    
    
    def delete(maMH):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="delete from monhoc where maMH=%s"
            cursor.execute(sql,(maMH,))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def getIDMH(tenMH):
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql = "SELECT maMH FROM monhoc WHERE tenMH = %s"
            cursor.execute(sql, (tenMH,))
            maMH = cursor.fetchone()  # Lấy một dòng dữ liệu
            if maMH:
                return maMH[0]  # Trả về mã môn học (phần tử đầu tiên trong tuple)
            else:
                return None  # Trả về None nếu không tìm thấy mã môn học
        except Exception as e:
            print('lỗi kết nối:', e)
            db.rollback()
            return None
        finally:
            cursor.close()
            db.close()

                                        