import mysql.connector as mdb
from .db_connector import *


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
    
    
    def get(maBH):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from buoihoc where maBH = %s",(maBH,))          

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
            sql="insert into buoihoc(maMH, tuan, tietbatdau, tietketthuc, ngay) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,(lesson.maMH, lesson.tuan, lesson.gioBD, lesson.gioKT, lesson.ngay))
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
            sql = "UPDATE buoihoc SET maMH=%s, tuan=%s, tietbatdau=%s, tietketthuc=%s, ngay=%s WHERE maBH=%s"
            cursor.execute(sql, (lesson.maMH, lesson.tuan, lesson.gioBD, lesson.gioKT, lesson.ngay, lesson.maBH))
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
            
            
    def getInfo():
        result_list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute(
                "SELECT buoihoc.maBH, monhoc.TenMH, giangvien.hoTen, lop.tenLop, buoihoc.tuan, buoihoc.tietbatdau, buoihoc.tietketthuc, buoihoc.ngay "
                "FROM buoihoc "
                "JOIN monhoc ON buoihoc.maMH = monhoc.maMH "
                "JOIN lop ON monhoc.maLop = lop.maLop "
                "JOIN giangvien ON monhoc.maGV = giangvien.maGV"
            )

            for row in cursor:
                result_list.append(row)
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                db.close()
            except Exception as ex:
                print(ex)
        return result_list
