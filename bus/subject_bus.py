
from dal.subject_dal import *


class subjectBUS:
    # def __init__(self, db):
    #     self.subject_dal = subjectDAL(db)

    # def add_subject(self, subject_dto):
    #     self.subject_dal.add_subject(subject_dto)

    # def update_subject(self, maMH, tenMH, maGV):
    #     self.subject_dal.update_subject(maMH, tenMH, maGV)

    # def delete_subject(self, maMH):
    #     self.subject_dal.delete_subject(maMH)

    def get_all():
        return subjectDAL.getList()