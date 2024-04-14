import mysql.connector as mdb
from . db_connector import *

class classDAL:

    def getList():
        list = []
        try:
            conn = DatabaseConnector()
            db = conn.connect()
            cursor = db.cursor()
            cursor.execute("select * from lop")          

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