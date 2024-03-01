from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<{self.id} {self.name} {self.species} {self.photo_url} {self.age} {self.notes} {self.available}>'
