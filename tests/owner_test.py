import unittest

from models.owner import Owner

class OwnerTest(unittest.TestCase):
    
    def setUp(self):
        self.owner1 = Owner("Laurie", "08564489732", "laurie.surname@mail.com", "5 The House, Larbert, FK9 2BE")
    
    
    def test_owner_has_name(self):
        self.assertEqual("Laurie", self.owner1.name)

    def test_owner_has_phone_number(self):
        self.assertEqual("08564489732", self.owner1.phone_number)

    def test_owner_has_email_address(self):
        self.assertEqual("laurie.surname@mail.com", self.owner1.email_address)

    def test_owner_has_address(self):
        self.assertEqual("5 The House, Larbert, FK9 2BE", self.owner1.address)