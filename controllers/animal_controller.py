from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("animals/new.html", all_owners = owners, all_vets = vets)

@animals_blueprint.route("/animal", methods=['POST'])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type = request.form['type']
    owner = owner_repository.select(request.form['owner_id'])
    vet = vet_repository.select(request.form['vet_id'])
    treatment_notes = request.form['treatment_notes']
    animal = Animal(name, date_of_birth, type, owner, vet, treatment_notes )
    animal_repository.save(animal)
    return redirect('/animals')


@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_owner(id):
    animal_repository.delete(id)
    return redirect('/animals')