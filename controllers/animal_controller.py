from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
from datetime import datetime

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    
    animals = animal_repository.select_all()
    searched = request.args.get('searched')
    if searched:
        searched = searched.capitalize()
        animals = animal_repository.select_by_name(searched)
        return render_template("animals/searched.html", animals=animals)
    else:
        animals = animal_repository.select_all()
    
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("animals/new.html", all_owners = owners, all_vets = vets)

@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type = request.form['type']
    owner = owner_repository.select(request.form['owner_id'])
    vet = vet_repository.select(request.form['vet_id'])
    animal = Animal(name, date_of_birth, type, owner, vet)
    animal_repository.save(animal)
    return redirect('/animals')


@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_owner(id):
    animal_repository.delete(id)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>")
def show_animal(id):
    animal = animal_repository.select(id)
    appointments = animal_repository.appointments(animal)
    today_date = animal_repository.inject_today_date()

    return render_template('animals/show.html', animal = animal, appointments = appointments, today_date = today_date)



@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/edit.html', animal = animal, all_owners = owners, all_vets = vets)

@animals_blueprint.route("/animals/<id>", methods = ['POST'])
def update_animal(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type = request.form['type']
    owner = owner_repository.select(request.form['owner_id'])
    vet = vet_repository.select(request.form['vet_id'])
    animal = Animal(name, date_of_birth, type, owner, vet,id )
    animal_repository.update(animal)
    return redirect('/animals')