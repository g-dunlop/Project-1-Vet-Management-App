
import pdb

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
from models.appointment import Appointment

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository
import repositories.appointment_repository as appointment_repository

animal_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()
treatment_repository.delete_all()

vet1 = Vet('Martina Plowicz')
vet_repository.save(vet1)

vet2 = Vet('James Herriot')
vet_repository.save(vet2)

# vet1.first_name = 'Bob'
# vet_repository.update(vet1)

owner1 = Owner("Laurie", "08564489732", "laurie.surname@mail.com", "5 The House, Larbert, FK9 2BE")
owner_repository.save(owner1)

owner2 = Owner("Graeme", "08564489733", "graeme.surname@mail.com", "5 The House, Larbert, FK9 2BE")
owner_repository.save(owner2)

# owner2.phone_number = "099999999999"
# owner_repository.update(owner2)

animal1 = Animal("Tony", "2017-11-11", "cat", owner1, vet1)
animal_repository.save(animal1)
# pdb.set_trace()
# animal1.name = "Toni"

# animal_repository.update(animal1)

animal2 = Animal("Collin", "2018-12-15", "cat", owner2, vet1)
animal_repository.save(animal2)

# animal2.name = "Colin"
# animal_repository.update(animal2)

# vets = vet_repository.select_all()
# for vet in vets:
#     print(vet.__dict__)

# owners = owner_repository.select_all()
# for owner in owners:
#     print(owner.__dict__)

# owner = owner_repository.select(21)
# print(owner.__dict__)

# vet = vet_repository.select(40)
# print(vet.__dict__)

# animals = animal_repository.select_all()
# for animal in animals:
#     print(animal.__dict__)

# animal_repository.delete(11)
# vet_repository.delete(12)
# owner_repository.delete(11)

# vet = vet_repository.select_by_name('James')
# print(vet.__dict__)

# owner=owner_repository.select_by_name('Laurie')
# print(owner.__dict__)

# animal=animal_repository.select_by_name('Collin')
# print(animal.__dict__)

treatment1 = Treatment("Vet consultation", 15.25)
treatment_repository.save(treatment1)

treatment2 = Treatment("Rabies Vaccination", 80.00)
treatment_repository.save(treatment2)

treatment3 = Treatment("None", 0.00)
treatment_repository.save(treatment3)

# treatments = treatment_repository.select_all()
# for treatment in treatments:
#     print(treatment.__dict__)

# treatment = treatment_repository.select(9)
# print(treatment.__dict__)

# treatment_repository.delete(11)

# treatment1.price = 15.00
# treatment_repository.update(treatment1)

treatments = treatment_repository.select_by_name("Vet consult")
for treatment in treatments:
    print(treatment.__dict__)

appointment1 = Appointment(animal1, vet1, '2022-08-21', '15:00', 'He is acting like a person', treatment1)
appointment_repository.save(appointment1)

appointments = appointment_repository.select_all()
for appointment in appointments:
    print(appointment.__dict__)

appointment1.reason = "She is acting like a person"
appointment_repository.update(appointment1)

# appointment = appointment_repository.select(7)
# print(appointment.__dict__)

# appointments = appointment_repository.select_by_date("21")
# for appointment in appointments:
#     print(appointment.__dict__)