
from dal.subject_dal import *
from dto.subject import *; 


class subjectBUS:
    def add (subject):
        return subjectDAL.add(subject)

    def getTenMH(maMH):
        return subjectDAL.getTenMH(maMH)
    
    def getMaGV(maMH):
        return subjectDAL.getMaGV(maMH)

    def update_subject(subject):
        return subjectDAL.update(subject)

    def delete(maMH):
        return subjectDAL.delete(maMH)

    def get_all():
        return subjectDAL.getList()
    def getIDSubject (tenMH):
        return subjectDAL.getIDMH(tenMH)
    
    
    def getInfo ():
        return subjectDAL.getInfo()