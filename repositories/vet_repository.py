import pdb
from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

def save(vet):
    sql = "INSERT INTO vets(full_name) VALUES (%s) RETURNING *"
    values = [vet.full_name]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


def select_all():

    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['full_name'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = Vet(result['full_name'], result['id'])
    return vet

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (full_name) = (%s) WHERE id = %s"
    values = [vet.full_name, vet.id]
    run_sql(sql, values)

def animals(vet):
    animals = []
    sql = "SELECT animals.* FROM animals INNER JOIN vets ON animals.vet_id = vets.id WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)
    for row in results:
        animal = Animal(row['name'], row['date_of_birth'], row['type'], row['owner_id'], row['vet_id'], row['treatment_notes'], row['id'])
        animals.append(animal)

    return animals

def select_by_name(name):
    vets = []
    sql = "SELECT * FROM vets WHERE full_name LIKE %s"
    values = ['%' + name + '%']
    results = run_sql(sql, values)
    
    for row in results:
        vet = Vet(row['full_name'], row['id'])
        vets.append(vet)
    return vets

    