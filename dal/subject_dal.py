import mysql.connector as mdb
from . db_connector import *


class subjectDAL:

    # def __init__(self, db):
    #     self.db = db

    # def add_subject(self, subject_dto):
    #     try:
    #         cursor = self.db.cursor()
    #         sql = "INSERT INTO monhoc (tenMH, maLop, maGV) VALUES (%s, %s, %s)"
    #         val = (subject_dto.tenMH, subject_dto.maLop, subject_dto.maGV)
    #         cursor.execute(sql, val)
    #         self.db.commit()
    #         print("Subject added successfully!")
    #     except mdb.Error as e:
    #         print("Error adding subject:", e)

    # def update_subject(self, maMH, tenMH, maGV):
    #     try:
    #         cursor = self.db.cursor()
    #         sql = "UPDATE monhoc SET tenMH = %s, maGV = %s WHERE maMH = %s"
    #         val = (tenMH, maGV, maMH)
    #         cursor.execute(sql, val)
    #         self.db.commit()
    #         print("Subject updated successfully!")
    #     except mdb.Error as e:
    #         print("Error updating subject:", e)

    # def delete_subject(self, maMH):
    #     try:
    #         cursor = self.db.cursor()
    #         sql = "DELETE FROM monhoc WHERE maMH = %s"
    #         val = (maMH,)
    #         cursor.execute(sql, val)
    #         self.db.commit()
    #         print("Subject deleted successfully!")
    #     except mdb.Error as e:
    #         print("Error deleting subject:", e)

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
            sql="insert into giangvien(maGV,hoTen,SDT) VALUES (%s, %s, %s)"
            cursor.execute(sql,(subject.tenMH,subject.maLop,subject.maGV))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()