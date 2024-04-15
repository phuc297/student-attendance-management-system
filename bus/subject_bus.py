
from dal.subject_dal import *
from dto.subject import *; 


class subjectBUS:
    # def __init__(self, db):
    #     self.subject_dal = subjectDAL(db)

    def add (subject):
          return subjectDAL.add(subject)

    def update_subject(subject):
        return subjectDAL.update(subject)

    def delete(maMH):
        return subjectDAL.delete(maMH)

    def get_all():
        return subjectDAL.getList()
    def getIDSubject (tenMH):
        return subjectDAL.getIDMH(tenMH)