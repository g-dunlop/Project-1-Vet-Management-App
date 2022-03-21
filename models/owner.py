class Owner:
    def __init__(self, full_name, phone_number, email_address, address, registered=True,  id=None):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.registered = registered
        self.id = id