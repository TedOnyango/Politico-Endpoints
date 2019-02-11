OFFICES = []

class OfficeModel():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        
    @staticmethod
    def view_all_offices():
        return [vars(office) for office in OFFICES]

    def save_office(self):
        OFFICES.append(self)

    @staticmethod
    def edit_office(id, name):
        edited = False
        for office in OFFICES:
           if(office["id"] == id):
               office["name"] = name
               edited = True
        return edited

    @staticmethod
    def get_specific_office(id):
        return [vars(office) for office in OFFICES if office.id == id]