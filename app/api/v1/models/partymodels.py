PARTIES = []

class PartiesModel():
    def __init__(self, id, name, hqAddress, logoUrl):
        self.id = id
        self.name = name
        self.hqAddress = hqAddress
        self.logUrl = logoUrl

    @staticmethod
    def view_parties():
        return PARTIES

    
    @staticmethod
    def get_specific_party(id):
        return [party for party in PARTIES if party["id"] == id]


    def save_party(self):
        party = {
            "id": self.id,
            "name": self.name,
            "hqAddress": self.hqAddress,
            "logoUrl": self.logUrl
        }
        PARTIES.append(party)
    @staticmethod
    def delete_party(id):
        found = False
        for party in PARTIES:
            if party.id == id:
                PARTIES.remove(party)
                found = True
        return found
    
    @staticmethod
    def edit_party(id, name):
        edited = False
        for party in PARTIES:
           if(party["id"] == id):
               party["name"] = name
               edited = True
        return edited
