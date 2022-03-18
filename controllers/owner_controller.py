from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners = owners)

@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners", methods=['POST'])
def create_vet():
    name = request.form['name']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    address = request.form['address']
    owner = Owner(name, phone_number, email_address, address)
    owner_repository.save(owner)
    return redirect('/owners')


@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')