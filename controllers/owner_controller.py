from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    searched = request.args.get('searched') 
    if searched:
        searched = searched.capitalize()
        owners = owner_repository.select_by_name(searched)
        return render_template("owners/searched.html", owners=owners)
    else:
        owners = owner_repository.select_all()
    return render_template("owners/index.html", owners = owners)

@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners", methods=['POST'])
def create_owner():
    full_name = request.form['full_name']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    address = request.form['address']
    registered = True
    owner = Owner(full_name, phone_number, email_address, address, registered)
    owner_repository.save(owner)
    return redirect('/owners')


@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>")
def show_owner(id):
    owner = owner_repository.select(id)
    animals = owner_repository.animals(owner)
    return render_template('owners/show.html', owner = owner, animals = animals)

@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner = owner)

@owners_blueprint.route("/owners/<id>", methods = ['POST'])
def update_owners(id):
    full_name = request.form['full_name']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    address = request.form['address']
    registered = request.form['registered']
    owner = Owner(full_name, phone_number, email_address, address, registered, id)
    owner_repository.update(owner)
    return redirect('/owners')