import mysql.connector
class DatabaseConnector:
    def connect(self):    
        db = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="",
            database="diemdanhsv"
        )
        return db