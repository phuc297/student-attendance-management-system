import mysql.connector as mdb

class classDAL:

    def __init__(self, db):
        self.db = db

    def add_class(self, tenLop):
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO lop (tenLop) VALUES (%s)"
            val = (tenLop,)
            cursor.execute(sql, val)
            self.db.commit()
            print("Class added successfully!")
        except mdb.Error as e:
            print("Error adding class:", e)

    def update_class(self, maLop, tenLop):
        try:
            cursor = self.db.cursor()
            sql = "UPDATE lop SET tenLop = %s WHERE maLop = %s"
            val = (tenLop, maLop)
            cursor.execute(sql, val)
            self.db.commit()
            print("Class updated successfully!")
        except mdb.Error as e:
            print("Error updating class:", e)

    def delete_class(self, maLop):
        try:
            cursor = self.db.cursor()
            sql = "DELETE FROM lop WHERE maLop = %s"
            val = (maLop,)
            cursor.execute(sql, val)
            self.db.commit()
            print("Class deleted successfully!")
        except mdb.Error as e:
            print("Error deleting class:", e)

    def get_all(self):
        try:
            cursor = self.db.cursor()
            sql = "SELECT * FROM lop"
            cursor.execute(sql)
            classes = cursor.fetchall()
            return classes
        except mdb.Error as e:
            print("Error fetching classes:", e)
            return []
