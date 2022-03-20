import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
from models.animal import Animal
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets", methods = ['GET'])
def vets():

    vets = vet_repository.select_all()
    searched = request.args.get('searched')
    print(searched)
    if searched:
        vets = vet_repository.select_by_name(searched)
        return render_template("vets/searched.html", vets=vets)
    else:
        vets = vet_repository.select_all()
        return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    return render_template("vets/new.html")

@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    vet = Vet(first_name, last_name)
    vet_repository.save(vet)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>")
def show_vet(id):
    vet = vet_repository.select(id)
    animals = vet_repository.animals(vet)
    return render_template('vets/show.html', vet = vet, animals = animals)

@vets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

@vets_blueprint.route("/vets/<id>", methods = ['POST'])
def update_vet(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    vet = Vet(first_name, last_name, id)
    vet_repository.update(vet)
    return redirect("/vets")