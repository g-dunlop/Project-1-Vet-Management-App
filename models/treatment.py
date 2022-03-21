class Treatment:
    def __init__(self, description, price, id=None):
        self.description = description
        self.price = round(price, 3)
        self.id = id