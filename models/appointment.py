class Appointment:
    def __init__(self, animal, vet, appointment_date, appointment_time, reason, treatment=None, notes=None, id=None):
        self.animal = animal
        self.vet = vet
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.treatment = treatment
        self.notes = notes
        self.id = id

    # def total_cost(self, treatments):
    #     treatments=self.treatments
    #     for treatment in treatment:

    def add_to_treatments(self, treatment):
        self.treatments.append(treatment)