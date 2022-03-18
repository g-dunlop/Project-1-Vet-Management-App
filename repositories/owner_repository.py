from db.run_sql import run_sql

from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners(name, phone_number, email_address, address) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.phone_number, owner.email_address, owner.address]
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
        owner = Owner(row['name'], row['phone_number'], row['email_address'], row['address'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['phone_number'], result['email_address'], result['address'], result['id'])
    return owner

    
def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name, phone_number, email_address, address) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.phone_number, owner.email_address, owner.address, owner.id]
    print(values)
    run_sql(sql, values)