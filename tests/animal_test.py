import unittest

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

class AnimalTest(unittest.TestCase):

    def setUp(self):
        
        self.owner1 = Owner("Laurie", "08564489732", "laurie.surname@mail.com", "5 The House, Larbert, FK9 2BE")
        self.vet1 = Vet("Martina", [])
        self.animal1 = Animal("Tony", "11/11/2017", "cat", self.owner1, self.vet1, [{"date":"05/05/2021", "vet": "Martina", "Problem": "Irregular Movements", "Treatment Provided":"Laxatives"}])

    def test_animal_has_name(self):
        self.assertEqual("Tony", self.animal1.name)

    def test_animal_has_dob(self):
        self.assertEqual("11/11/2017", self.animal1.date_of_birth)

    def test_animal_has_type(self):
        self.assertEqual("cat", self.animal1.type)

    def test_animal_owner_has_name(self):
        self.assertEqual("Laurie", self.animal1.owner.full_name)

    def test_animal_has_vet(self):
        self.assertEqual("Martina", self.animal1.vet.full_name)

    def test_animal_has_clear_treament_notes(self):
        self.assertEqual("Martina", self.animal1.treatment_notes[0]["vet"])