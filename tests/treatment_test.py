import unittest

from models.treatment import Treatment

class OwnerTest(unittest.TestCase):
    
    def setUp(self):
        self.treatment1 = Treatment("Vet consult", 15.25)

    def test_treatment_has_description(self):
        self.assertEqual("Vet consult", self.treatment1.description)

    def test_treatment_has_price(self):
        self.assertEqual(15.25, self.treatment1.price)