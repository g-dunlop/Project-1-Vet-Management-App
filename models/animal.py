from datetime import datetime

class Animal:
    def __init__(self, name, date_of_birth, type, owner, vet, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type = type
        self.owner = owner
        self.vet = vet
        self.id = id

        

        