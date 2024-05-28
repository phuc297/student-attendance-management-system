from . db_connector import *
from dto.student import *

class StudentDAL:

    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from sinhvien")          

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
    
    def get(masv):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from sinhvien where maSV = %s", (masv,))          

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
    
    def getHoTen(masv):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select hoTen from sinhvien where maSV = %s", (masv,))          

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

    def add(student: Student):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""insert into sinhvien(hoTen, maLop, cmnd, gioiTinh, ngaySinh, email, SDT) value (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql,(student.hoten, student.malop, student.cmnd, student.gioitinh, student.ngaysinh, student.email, student.sdt))
            db.commit()
           
            return True
        except Exception as e:
            print('Student DAL: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def delete(masv):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""delete from sinhvien where maSV = %s"""
            cursor.execute(sql,(masv,))
            db.commit()
           
            return True
        except Exception as e:
            print('Student DAL: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def update(student: Student):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql = """UPDATE sinhvien SET hoTen = %s, maLop = %s, gioitinh = %s, ngaysinh = %s, email = %s, sdt = %s, cmnd = %s WHERE maSV=%s"""
            cursor.execute(sql,(student.hoten, student.malop, student.gioitinh, student.ngaysinh, student.email, student.sdt, student.cmnd, student.masv))
            db.commit()
           
            return True
        except Exception as e:
            print('Student DAL: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()