from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#elimino el modelo existente de User y pego mi código a partir de aquí

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color
        }
    
class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model
        }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }
    
class Favoritos_personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    personajes_relacion = db.Column(db.Integer, db.ForeignKey(Personajes.id, ondelete='CASCADE'), nullable=False)
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "personajes_relacion": self.personajes_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }
    
class Favoritos_vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    vehiculos_relacion = db.Column(db.Integer, db.ForeignKey(Vehiculos.id, ondelete='CASCADE'), nullable=False)
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "vehiculos_relacion": self.vehiculos_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }

class Favoritos_planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    planetas_relacion = db.Column(db.Integer, db.ForeignKey(Planetas.id, ondelete='CASCADE'), nullable=False)
    usuarios_relacion = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planetas_relacion": self.planetas_relacion,
            "usuarios_relacion": self.usuarios_relacion
        }