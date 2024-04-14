
from dal.lesson_dal import *
from dto.lesson import *; 


class lessonBUS:
    

    def add (lesson):
          return lessonDAL.add(lesson)

    def update_subject(lesson):
        return lessonDAL.update(lesson)

    def delete(lesson):
        return lessonDAL.delete(lesson)

    def get_all():
        return lessonDAL.getList()