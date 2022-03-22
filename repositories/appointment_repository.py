import pdb
from db.run_sql import run_sql
from datetime import datetime
from models.appointment import Appointment
from models.animal import Animal
from models.treatment import Treatment
from datetime import datetime

import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository

def save(appointment):
    sql = "INSERT INTO appointments (animal_id, appointment_date, appointment_time, reason, treatment_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [appointment.animal.id, appointment.appointment_date, appointment.appointment_time, appointment.reason, appointment.treatment.id]
    # pdb.set_trace()
    results = run_sql(sql, values)
    # pdb.set_trace()
    appointment.id = results[0]['id']
    # pdb.set_trace()

    # appointment.add_to_treatments(appointment.treatment)
    return appointment

def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)


def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)

    for row in results:
        animal = animal_repository.select(row['animal_id'])
        treatment = treatment_repository.select(row['treatment_id'])
        appointment = Appointment(animal, row['appointment_date'], row['appointment_time'], row['reason'], treatment, row['id'])
        appointments.append(appointment)
    return(appointments)

def delete(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(appointment):
    sql = "UPDATE appointments SET (animal_id, appointment_date, appointment_time, reason, treatment_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [appointment.animal.id, appointment.appointment_date, appointment.appointment_time, appointment.reason, appointment.treatment.id, appointment.id]
    print(values)
    run_sql(sql, values)


def select(id):
    animal = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = animal_repository.select(result['animal_id'])
        treatment = treatment_repository.select(result['treatment_id'])
        appointment = Appointment(animal, result['appointment_date'], result['appointment_time'], result['reason'], treatment, result['id'])           
    return appointment

# def select_by_date(appointment_date):
#     appointments = []
#     sql = "SELECT * FROM appointments WHERE appointment_date LIKE %s"
#     values = ['%' + appointment_date + '%']
#     results = run_sql(sql, values)
    
#     for row in results:
#         animal = animal_repository.select(row['animal_id'])
#         treatment = treatment_repository.select(row['treatment_id'])
#         appointment = Appointment(animal, row['appointment_date'], row['appointment_time'], row['reason'], treatment, row['id'])        
#         appointments.append(appointment)
#     return appointments