from db.run_sql import run_sql
from models.treatment import Treatment

def save(treatment):
    sql = "INSERT INTO treatments (description, price) VALUES (%s, %s) RETURNING *"
    values = [treatment.description, treatment.price]
    results = run_sql(sql, values)
    treatment.id = results[0]['id']
    return treatment

def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def select_all():
    treatments = []

    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for row in results:
        treatment = Treatment(row['description'], row['price'])
        treatments.append(treatment)
    return treatments


def select(id):
    treatment = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        treatment = Treatment(result['description'], result['price'], result['id'])
    return treatment

def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(treatment):
    sql = "UPDATE treatments SET (description, price) = (%s, %s) WHERE id = %s"
    values = [treatment.description, treatment.price,  treatment.id]
    print(values)
    run_sql(sql, values)

def select_by_name(name):
    treatments = []
    sql = "SELECT * FROM treatments WHERE description LIKE %s"
    values = ['%' + name + '%']
    results = run_sql(sql, values)
    
    for row in results:
        treatment = Treatment(row['description'], row['price'], row['id'])
        treatments.append(treatment)
    return treatments