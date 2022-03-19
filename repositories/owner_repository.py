from db.run_sql import run_sql

from models.owner import Owner
from models.animal import Animal

def save(owner):
    sql = "INSERT INTO owners(full_name, phone_number, email_address, address) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.full_name, owner.phone_number, owner.email_address, owner.address]
    results = run_sql(sql, values)
    owner.id = results[0]['id']
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['full_name'], row['phone_number'], row['email_address'], row['address'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['full_name'], result['phone_number'], result['email_address'], result['address'], result['id'])
    return owner

    
def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (full_name, phone_number, email_address, address) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.full_name, owner.phone_number, owner.email_address, owner.address, owner.id]
    print(values)
    run_sql(sql, values)


def animals(owner): 
    animals = []
    sql = "SELECT animals.* FROM animals INNER JOIN owners ON animals.owner_id = owners.id WHERE owner_id = %s"
    values = [owner.id]
    results = run_sql(sql, values)
    for row in results:
        animal = Animal(row['name'], row['date_of_birth'], row['type'], row['owner_id'], row['vet_id'], row['treatment_notes'], row['id'])
        animals.append(animal)
    return animals