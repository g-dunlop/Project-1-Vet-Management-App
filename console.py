
import pdb

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

animal_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet1 = Vet('Martina', 'Simplowicz')
vet_repository.save(vet1)

vet2 = Vet('James', 'Herriot')
vet_repository.save(vet2)

# vet1.first_name = 'Bob'
# vet_repository.update(vet1)

owner1 = Owner("Laurie", "08564489732", "laurie.surname@mail.com", "5 The House, Larbert, FK9 2BE")
owner_repository.save(owner1)

owner2 = Owner("Graeme", "08564489733", "graeme.surname@mail.com", "5 The House, Larbert, FK9 2BE")
owner_repository.save(owner2)

# owner2.phone_number = "099999999999"
# owner_repository.update(owner2)

animal1 = Animal("Tony", "11/11/2017", "cat", owner1, vet1, [])
animal_repository.save(animal1)
# pdb.set_trace()
animal1.name = "Toni"
# pdb.set_trace()
animal_repository.update(animal1)

animal2 = Animal("Collin", "15/12/2018", "cat", owner2, vet1, ["17/02/2020", "Martina", "Diarrhea", "antibiotics"])
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