
from dal.sesson_dal import *
from dto.lesson import *; 


class lessonBUS:
    

    def add (lesson):
          return lessonDAL.add(lesson)

    def get(maBH):
        return lessonDAL.get(maBH)

    def update_lession(lesson):
        return lessonDAL.update(lesson)

    def delete(maBH):
        return lessonDAL.delete(maBH)

    def get_all():
        return lessonDAL.getList()
    
    def getInfo():
        return lessonDAL.getInfo()
    