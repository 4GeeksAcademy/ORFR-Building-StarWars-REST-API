from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship('Favorites', uselist=False, back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(150), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }
    

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(150), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(150), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), unique=True, nullable=False)
    user = db.relationship('User', back_populates='favorite')


    def serialize(self):
        return {
            "id": self.id
        }
