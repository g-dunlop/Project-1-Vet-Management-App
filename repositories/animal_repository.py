from db.run_sql import run_sql
import datetime
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.appointment import Appointment

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, type, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.type, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    # owners = owner_repository.select_all()
    # for owner in owners:
    #     if owner.id == animal.owner.id:
    #         owner.pets.append(animal)
    return animal


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def select_all():
    unsorted_animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['date_of_birth'], row['type'], owner, vet, row['id'])
        # animal.date_of_birth = datetime.strptime(animal.date_of_birth, ("%Y-%m-%d"))
        # animal.date_of_birth = animal.date_of_birth.strftime("%d/%m/%Y")
        unsorted_animals.append(animal)
    animals = sorted(unsorted_animals, key=lambda animal: animal.name)
    return(animals)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, type, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.type, animal.owner.id, animal.vet.id, animal.id]
    print(values)
    run_sql(sql, values)

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['date_of_birth'], result['type'], owner, vet, result['id'])
        # animal.date_of_birth = datetime.strptime(animal.date_of_birth, ("%Y-%m-%d"))
        # animal.date_of_birth = animal.date_of_birth.strftime("%d/%m/%Y")
    return animal


def select_by_name(name):
    animals = []
    sql = "SELECT * FROM animals WHERE name LIKE %s"
    values = ['%' + name + '%']
    results = run_sql(sql, values)
    
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['date_of_birth'], row['type'], owner, vet, row['id'])
        animals.append(animal)

    return animals

def appointments(animal):
    unsorted_appointments = []
    sql = "SELECT appointments.* from appointments INNER JOIN animals ON appointments.animal_id = animals.id WHERE animal_id = %s"
    values = [animal.id]
    results = run_sql(sql, values)
    for row in results:
        treatment = treatment_repository.select(row['treatment_id'])
        vet = vet_repository.select(row['vet_id'])
        appointment = Appointment(animal, vet, row['appointment_date'], row['appointment_time'], row['reason'], treatment, row['id'])
        unsorted_appointments.append(appointment)
    appointments = sorted(unsorted_appointments, key=lambda appointment: appointment.appointment_time)
    appointments = sorted(appointments, key=lambda appointment: appointment.appointment_date)
    return appointments


def inject_today_date():
    today_date = datetime.date.today()
    return today_date