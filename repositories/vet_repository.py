from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

def save(vet):
    sql = "INSERT INTO vets(name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    vet.id = results[0]['id']
    return vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)