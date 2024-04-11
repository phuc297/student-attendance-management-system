from dal.lesson_dal import *

class LessonBUS:
    def __init__(self, db):
        self.lesson_dal = lessonDAL(db)

    def add_lesson(self, lesson_dto):
        self.lesson_dal.add_lesson(lesson_dto)

    def update_lesson(self, maBH, maMH, maLop, gioBD, gioKT, ngay):
        self.lesson_dal.update_lesson(maBH, maMH, maLop, gioBD, gioKT, ngay)

    def delete_lesson(self, maBH):
        self.lesson_dal.delete_lesson(maBH)

    def get_all_lessons(self):
        return self.lesson_dal.get_all()
