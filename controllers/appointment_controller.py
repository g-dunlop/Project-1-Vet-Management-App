from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
from models.treatment import Treatment
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository
import repositories.appointment_repository as appointment_repository

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments = appointments)


