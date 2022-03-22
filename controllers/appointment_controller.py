import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
from models.treatment import Treatment
from models.appointment import Appointment
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository
import repositories.appointment_repository as appointment_repository

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    today_date = animal_repository.inject_today_date()
    # calendar = appointment_repository.create_calendar()
    return render_template("appointments/index.html", appointments = appointments, today_date = today_date)

@appointments_blueprint.route("/appointments/new", methods=['GET'])
def new_appointment():
    animals = animal_repository.select_all()
    treatments = treatment_repository.select_all()
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    today_date = appointment_repository.inject_today_date()
    return render_template("appointments/new.html", all_animals = animals, all_treatments = treatments, all_owners = owners, all_vets = vets, today_date = today_date)


@appointments_blueprint.route("/appointments", methods=['POST'])
def create_appointment():
    animal = animal_repository.select(request.form['animal_id'])
    # pdb.set_trace()
    vet = vet_repository.select(request.form['vet_id'])
    appointment_date = request.form['appointment_date']
    # pdb.set_trace()
    appointment_time = request.form['appointment_time']
    # pdb.set_trace()
    reason = request.form['reason']
    # pdb.set_trace()
    treatment = treatment_repository.select(request.form['treatment_id'])

    notes= request.form['notes']
    # pdb.set_trace()
    appointment = Appointment(animal, vet, appointment_date, appointment_time, reason, treatment, notes)
   
    appointment_repository.save(appointment)
    return redirect('/appointments')


@appointments_blueprint.route("/appointments/<id>/delete", methods=['POST'])
def delete_appointment(id):
    appointment_repository.delete(id)
    return redirect('/appointments')


@appointments_blueprint.route("/appointments/<id>")
def show_appointment(id):
    appointment = appointment_repository.select(id)
    return render_template('appointments/show.html', appointment = appointment)

@appointments_blueprint.route("/appointments/<id>/edit")
def edit_appointment(id):
    appointment = appointment_repository.select(id)
    animals = animal_repository.select_all()
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    treatments = treatment_repository.select_all()
    today_date = appointment_repository.inject_today_date()
    return render_template('appointments/edit.html', all_animals = animals, all_treatments = treatments, all_owners = owners, all_vets = vets, appointment = appointment, today_date = today_date)

@appointments_blueprint.route("/appointments/<id>", methods = ['POST'])
def update_appointment(id):
    animal = animal_repository.select(request.form['animal_id'])
    # pdb.set_trace()
    vet = animal_repository.select(request.form['vet_id'])
    appointment_date = request.form['appointment_date']
    # pdb.set_trace()
    appointment_time = request.form['appointment_time']
    # pdb.set_trace()
    reason = request.form['reason']
    # pdb.set_trace()
    treatment = treatment_repository.select(request.form['treatment_id'])
    notes= request.form['notes']
    # pdb.set_trace()
    appointment = Appointment(animal, vet, appointment_date, appointment_time, reason, treatment, notes, id)
    appointment_repository.update(appointment)
    return redirect('/appointments')


@appointments_blueprint.route("/appointments/calendar")
def show_calendar():
    return render_template('appointments/calendar.html')