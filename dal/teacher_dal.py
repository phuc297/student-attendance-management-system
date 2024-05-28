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
                list.append(x)
        except Exception as e:
            print(e)
        try:
            cursor.close()
            db.close()
        except:
            pass
        return list
    def getHoTen(magv):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select hoTen from giangvien where maGV = %s", (magv,))          

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
    def add(hoTen, gioitinh, cmnd, ngaysinh, email, sdt, maTK):
       
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""INSERT INTO giangvien (hoTen, gioitinh, cmnd, ngaysinh, email, sdt, maTK) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(sql,(hoTen, gioitinh, cmnd, ngaysinh, email, sdt, maTK,))
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
            sql="UPDATE giangvien SET hoTen=%s, gioiTinh=%s, cmnd=%s,  ngaysinh=%s, email=%s, sdt=%s, maTK=%sWHERE maGV=%s"
            cursor.execute(sql,(giangvien.hoTen,giangvien.gioitinh,giangvien.cmnd,giangvien.ngaysinh,giangvien.email,giangvien.sdt,giangvien.maTK,giangvien.maGV,))
            db.commit()
           
            return True
        except Exception as e:
            print('lỗi kết nối: ',e)
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
            
    def checkAccount(maTK):
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql = "SELECT maTK FROM giangvien WHERE maTK = %s"
            cursor.execute(sql, (maTK,))

            result = cursor.fetchall()  # Lấy tất cả các hàng kết quả

            if result:
                return True
            else:
                return False
        except Exception as e:
            print("Error occurred:", e)
            return False
        finally:
            try:
                if cursor:
                    cursor.close()
                if db:
                    db.close()
            except Exception as e:
                print("Error occurred while closing cursor and connection:", e)





