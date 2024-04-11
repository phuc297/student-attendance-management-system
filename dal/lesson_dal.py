import mysql.connector as mdb

class lessonDAL:

    def __init__(self, db):
        self.db = db

    def add_lesson(self, lesson_dto):
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO buoihoc (maMH, maLop ,gioBD, gioKT, ngay) VALUES (%s, %s, %s, %s, %s)"
            val = (lesson_dto.maMH, lesson_dto.maLop ,lesson_dto.gioBD, lesson_dto.gioKT, lesson_dto.ngay)
            cursor.execute(sql, val)
            self.db.commit()
            print("Lesson added successfully!")
        except mdb.Error as e:
            print("Error adding lesson:", e)

    def update_lesson(self, maBH, maMH, maLop, gioBD, gioKT, ngay):
        try:
            cursor = self.db.cursor()
            sql = "UPDATE buoihoc SET maMH = %s, maLop = %s, gioBD = %s, gioKT = %s, ngay = %s WHERE maBH = %s"
            val = (maMH, maLop, gioBD, gioKT, ngay, maBH)
            cursor.execute(sql, val)
            self.db.commit()
            print("Lesson updated successfully!")
        except mdb.Error as e:
            print("Error updating lesson:", e)

    def delete_lesson(self, maBH):
        try:
            cursor = self.db.cursor()
            sql = "DELETE FROM buoihoc WHERE maBH = %s"
            val = (maBH,)
            cursor.execute(sql, val)
            self.db.commit()
            print("Lesson deleted successfully!")
        except mdb.Error as e:
            print("Error deleting lesson:", e)

    def get_all(self):
        try:
            cursor = self.db.cursor()
            sql = "SELECT * FROM buoihoc"
            cursor.execute(sql)
            lessons = cursor.fetchall()
            return lessons
        except mdb.Error as e:
            print("Error fetching lessons:", e)
            return []
