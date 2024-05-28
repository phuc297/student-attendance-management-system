from . db_connector import *

class AttendDAL:
    def getList(maBH):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql="""select maBH, maSV, giovao, trangthai, chitiet from diemdanh where maBH = %s"""
            cursor.execute(sql,(maBH,))

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
    
    def check(maSV, maBH):
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            sql="""select * from diemdanh where maSV = %s and maBH = %s"""
            cursor.execute(sql,(maSV, maBH,))

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
    
    def add(maBH, maSV, gioVao, trangthai, chitiet):
        try: 
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""INSERT INTO diemdanh (maBH, maSV, gioVao, trangthai, chitiet) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql,(maBH, maSV, gioVao, trangthai, chitiet,))
            db.commit()
           
            return True
        except Exception as e:
            print("AttendDAL add",e)
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return False

    def delete2(maBH, maSV):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""delete from diemdanh where maBH = %s and maSV = %s"""
            cursor.execute(sql,(maBH, maSV, ))
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return False
    
    def delete(maDD):
        try:        
            conn= DatabaseConnector()
            db= conn.connect()
            cursor = db.cursor()
            sql="""delete from diemdanh where maDD = %s"""
            cursor.execute(sql,(maDD,))
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            cursor.close()
            db.close()
        return False




