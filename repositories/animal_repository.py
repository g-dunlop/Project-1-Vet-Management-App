from db.run_sql import run_sql

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, type, owner_id, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.type, animal.owner.id, animal.vet.id, animal.treatment_notes]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    return animal