from dal.class_dal import *

class ClassBUS:
    def __init__(self, db):
        self.class_dal = classDAL(db)

    def add_class(self, tenLop):
        self.class_dal.add_class(tenLop)

    def update_class(self, maLop, tenLop):
        self.class_dal.update_class(maLop, tenLop)

    def delete_class(self, maLop):
        self.class_dal.delete_class(maLop)

    def get_all_classes(self):
        return self.class_dal.get_all()
