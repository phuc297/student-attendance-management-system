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