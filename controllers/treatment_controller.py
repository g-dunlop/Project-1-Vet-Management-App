import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.treatment import Treatment 

import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route("/treatments", methods = ['GET'])
def treatments():
    treatments = treatment_repository.select_all()
    searched = request.args.get('searched')
    
    
    if searched:
        searched = searched.capitalize()
        treatments = treatment_repository.select_by_name(searched)
        return render_template("treatments/searched.html", treatments=treatments)

    return render_template("treatments/index.html", treatments=treatments)

@treatments_blueprint.route("/treatments/new", methods=['GET'])
def new_treatment():
    return render_template("treatments/new.html")

@treatments_blueprint.route("/treatments", methods=['POST'])
def create_treatment(): 
    description = request.form['description']
    price = request.form['price']
    treatment = Treatment(description, price)
    treatment_repository.save(treatment)
    return redirect('/treatments')

@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect('/treatments')


@treatments_blueprint.route("/treatments/<id>")
def show_treatment(id):
    treatment = treatment_repository.select(id)
    
    return render_template('treatments/show.html', treatment = treatment)

@treatments_blueprint.route("/treatments/<id>/edit", methods=['GET'])
def edit_treatment(id):
    treatment = treatment_repository.select(id)
    return render_template('treatments/edit.html', treatment = treatment)

@treatments_blueprint.route("/treatments/<id>", methods = ['POST'])
def update_treatments(id):
    description = request.form['description']
    price = request.form['price']
    treatment = Treatment(description, price, id)
    treatment_repository.update(treatment)
    return redirect('/treatments')