import mysql.connector as mdb
from . db_connector import *


class lessonDAL:

    

    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from buoihoc")          

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
    

    def  add(lesson):
       
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="insert into buoihoc(maMH, maLop, gioBD, gioKT, ngay) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,(lesson.maMH, lesson.maLop, lesson.gioBD, lesson.gioKT, lesson.ngay))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
            
    
    
    def update(lesson):
        try:        
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql = "UPDATE buoihoc SET maMH=%s, maLop=%s, gioBD=%s, gioKT=%s, ngay=%s WHERE maBH=%s"
            cursor.execute(sql, (lesson.maMH, lesson.maLop, lesson.gioBD, lesson.gioKT, lesson.ngay, lesson.maBH))
            db.commit()
            return True
        except Exception as e:
            print('lỗi kết nối: ', e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    
    
    def delete(maBH):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="delete from buoihoc where maBH=%s"
            cursor.execute(sql,(maBH,))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()