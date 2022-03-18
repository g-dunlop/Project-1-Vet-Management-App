import unittest

from models.vet import Vet

class VetTest(unittest.TestCase):
    
    def setUp(self):
        self.vet1 = Vet("Martina", [])
        

    def test_vet_has_name(self):
        self.assertEqual("Martina", self.vet1.name)

    def test_vet_has_empty_animal_list(self):
        self.assertEqual(0, len(self.vet1.animals))