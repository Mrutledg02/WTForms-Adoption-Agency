from app import app
from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of pets
woodly = Pet(name='Woodly', species='dog', age=1)
porchetta = Pet(name='Porchetta', species='porcupine')
snargle = Pet(name='Snargle', species='cat')

db.session.add_all([woodly, porchetta, snargle])

db.session.commit()