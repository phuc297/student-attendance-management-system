from . db_connector import *
from dto.diemdanh_dto import *

class DiemdanhDAL:
    def getlist ():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from diemdanh")          

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
    def getlistdimuon():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("SELECT dd.maSV as masv, sv.hoTen as tenSV, bh.ngay as ngay, mh.tenMH as MonHoc, bh.maBH "
                        +"FROM diemdanh dd " 
                        +"JOIN buoihoc bh ON dd.maBH = bh.maBH "
                        +"JOIN sinhvien sv ON dd.maSV = sv.maSV "
                        +"JOIN monhoc mh ON bh.maMH = mh.maMH "
                        +"WHERE dd.trangthai =2 " 
                        +"GROUP BY dd.maSV")          
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
    
    def getListVang(): 
        result_list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("SELECT diemdanh.*, sinhvien.hoTen AS tenSV, buoihoc.ngay, monhoc.tenMH FROM diemdanh JOIN sinhvien ON diemdanh.maSV = sinhvien.maSV JOIN buoihoc ON diemdanh.maBH = buoihoc.maBH JOIN monhoc ON buoihoc.maMH = monhoc.maMH WHERE diemdanh.trangthai = 0")

            for row in cursor:
                result_list.append(row)
        except Exception as e:
            print(e)
        finally:
            try:
                cursor.close()
                db.close()
            except Exception as close_error:
                print("Error while closing cursor or connection:", close_error)
        return result_list
    
    
    
    def getList():
        conn = DatabaseConnector()
        db = conn.connect()
        cursor = db.cursor()
        
        try:
            query = """SELECT diemdanh.maDD, diemdanh.maSV, sinhvien.hoTen, lop.tenLop, diemdanh.gioVao, diemdanh.gioRa ,buoihoc.ngay, diemdanh.chitiet, diemdanh.maBH
                        FROM diemdanh
                        INNER JOIN sinhvien ON diemdanh.maSV = sinhvien.maSV
                        INNER JOIN lop ON sinhvien.maLop = lop.maLop
                        INNER JOIN buoihoc ON diemdanh.maBH = buoihoc.maBH;"""
            cursor.execute(query)
            result = cursor.fetchall()
            
            attendance_list = []
            for row in result:
                attendance_list.append(row)
            return attendance_list
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            db.close()
            
    def update(maDD, gioVao, gioRa, chitiet):
        conn = DatabaseConnector()
        db = conn.connect()
        cursor = db.cursor()
        
        try:
            query = f"""UPDATE diemdanh SET gioVao = '{gioVao}', gioRa = '{gioRa}', chitiet = '{chitiet}' WHERE maDD = {maDD};"""
            cursor.execute(query)
            db.commit()
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
        
        finally:
            cursor.close()
            db.close()