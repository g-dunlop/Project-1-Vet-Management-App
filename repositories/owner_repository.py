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

