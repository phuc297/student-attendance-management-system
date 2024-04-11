from dto.teacher import *
from . db_connector import *
from dto.teacher import Teacher
class TeacherDAL:
    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from giangvien")          

            for x in cursor:
                # list.append(Student(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
                list.append(x)
        except Exception as e:
            print(e)
        try:
            cursor.close()
            db.close()
        except:
            pass
        return list
    def addlist (giangvien):
       
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="insert into giangvien(hoTen,SDT) VALUES (%s, %s)"
            cursor.execute(sql,(giangvien.hoTen,giangvien.SDT))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def delete(maGV):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="delete from giangvien where maGV=%s"
            cursor.execute(sql,(maGV,))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def update(giangvien):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="update giangvien set hoTen=%s, SDT=%s  where maGV=%s"
            cursor.execute(sql,(giangvien.hoTen,giangvien.SDT,giangvien.maGV,))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

        




