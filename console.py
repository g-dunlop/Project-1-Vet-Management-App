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

vet1 = Vet('Martina', [])
vet_repository.save(vet1)

owner1 = Owner("Laurie", "08564489732", "laurie.surname@mail.com", "5 The House, Larbert, FK9 2BE")
owner_repository.save(owner1)

animal1 = Animal("Tony", "11/11/2017", "cat", owner1, vet1, [])
animal_repository.save(animal1)

