from flask import Flask, request, jsonify, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import  PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'ohsosecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug=DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    # get all the pets
    pets=Pet.query.all()
    return render_template('listing.html', pets=pets)

@app.route('/add', methods=["GET","POST"])
def add():
    """
    Displays form to add a pet

    """
    form=PetForm()
    if form.validate_on_submit():
        # this is a post route, add to the db
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        available=form.available.data
        pet=Pet(name=name,photo_url=photo_url,species=species,age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} has been added!")
        return redirect('/')
    else:
        # if this is a get route
        return render_template('add.html', form=form)

@app.route('/<int:petid>', methods=["GET","POST"])
def details(petid):
    """
    Displays form to edit or display a pet

    """
    pet=Pet.query.get(petid)
    form=PetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name=form.name.data
        pet.species=form.species.data
        pet.photo_url=form.photo_url.data
        pet.age=form.age.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        # if this is a get route
        return render_template('edit.html', p=pet,form=form)

    
