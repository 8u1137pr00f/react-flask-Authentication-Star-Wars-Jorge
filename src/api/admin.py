import os
from flask_admin import Admin
from api.models import db, Users, Personajes, Vehiculos, Planetas, Favoritos_personajes, Favoritos_vehiculos, Favoritos_planetas
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Vehiculos, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Favoritos_personajes, db.session))
    admin.add_view(ModelView(Favoritos_vehiculos, db.session))
    admin.add_view(ModelView(Favoritos_planetas, db.session))