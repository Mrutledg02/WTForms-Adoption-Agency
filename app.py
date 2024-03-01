from flask import Flask, render_template, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'oh_so_secret'
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# Define routes and views
@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
    
        flash('Pet added successfully!', 'success')  # Flash success message
        return redirect(url_for('index'))

    return render_template('add_pet.html', form=form)

@app.route('/edit/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()

        flash('Pet updated successfully!', 'success')  # Flash success message
        return redirect(url_for('index'))
    
    return render_template('edit_pet.html', pet=pet, form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pet_details.html', pet=pet, form=form)


if __name__ == '__main__':
    app.run(debug=True)
