class Appointment:
    def __init__(self, animal, appointment_date, appointment_time, reason, treatment=None, id=None):
        self.animal = animal
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.treatment = treatment
        self.id = id

    # def total_cost(self, treatments):
    #     treatments=self.treatments
    #     for treatment in treatment:
