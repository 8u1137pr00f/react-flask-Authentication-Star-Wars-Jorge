from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from api.models import db, Users, Personajes, Vehiculos, Planetas, Favoritos_personajes, Favoritos_vehiculos, Favoritos_planetas
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave secreta segura
jwt = JWTManager(app)

api = Blueprint('api', __name__)
CORS(api)

current_user = Users.name

@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    # Aquí deberías validar contra tu base de datos
    users_query = Users.query.filter_by(email=email, password=password).first()
    if email != users_query.email or password != users_query.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user()), 200

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

################# TODOS mis endpoints a partir de aquí
############ métodos GET ALL
@api.route('/users', methods=['GET'])
def handle_users():
    users = Users.query.all()
    users_serialized = list(map(lambda item:item.serialize(), users))
    response_body = {
        "msg": "OK",
        "data": users_serialized
    }
    return jsonify(response_body), 200

@api.route('/personajes', methods=['GET'])
def handle_personajes():
    personajes = Personajes.query.all()
    personajes_serialized = list(map(lambda item:item.serialize(), personajes))
    response_body = {
        "msg": "OK",
        "data": personajes_serialized
    }
    return jsonify(response_body), 200

@api.route('/vehiculos', methods=['GET'])
def handle_vehiculos():
    vehiculos = Vehiculos.query.all()
    vehiculos_serialized = list(map(lambda item:item.serialize(), vehiculos))
    response_body = {
        "msg": "OK",
        "data": vehiculos_serialized
    }
    return jsonify(response_body), 200

@api.route('/planetas', methods=['GET'])
def handle_planetas():
    planetas = Planetas.query.all()
    planetas_serialized = list(map(lambda item:item.serialize(), planetas))
    response_body = {
        "msg": "OK",
        "data": planetas_serialized
    }
    return jsonify(response_body), 200

@api.route('/favoritos_personajes', methods=['GET'])
def handle_favoritos_personajes():
    favoritos_personajes = Favoritos_personajes.query.all()
    favoritos_personajes_serialized = list(map(lambda item:item.serialize(), favoritos_personajes))
    response_body = {
        "msg": "OK",
        "data": favoritos_personajes_serialized
    }
    return jsonify(response_body), 200

@api.route('/favoritos_vehiculos', methods=['GET'])
def handle_favoritos_vehiculos():
    favoritos_vehiculos = Favoritos_vehiculos.query.all()
    favoritos_vehiculos_serialized = list(map(lambda item:item.serialize(), favoritos_vehiculos))
    response_body = {
        "msg": "OK",
        "data": favoritos_vehiculos_serialized
    }
    return jsonify(response_body), 200

@api.route('/favoritos_planetas', methods=['GET'])
def handle_favoritos_planetas():
    favoritos_planetas = Favoritos_planetas.query.all()
    favoritos_planetas_serialized = list(map(lambda item:item.serialize(), favoritos_planetas))
    response_body = {
        "msg": "OK",
        "data": favoritos_planetas_serialized
    }
    return jsonify(response_body), 200

############ métodos para GET específico por ID
@api.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = Users.query.filter_by(id=user_id).first()
    user_serialize = user.serialize()
    response_body = {
        "msg": "Ok",
        "data": user_serialize
    }
    return jsonify(response_body), 200

@api.route('/personajes/<int:personaje_id>', methods=['GET'])
def get_personaje_by_id(personaje_id):
    personaje = Personajes.query.filter_by(id=personaje_id).first()
    personaje_serialize = personaje.serialize()
    response_body = {
        "msg": "Ok",
        "data": personaje_serialize
    }
    return jsonify(response_body), 200

@api.route('/vehiculos/<int:vehiculo_id>', methods=['GET'])
def get_vehiculo_by_id(vehiculo_id):
    vehiculo = Vehiculos.query.filter_by(id=vehiculo_id).first()
    vehiculo_serialize = vehiculo.serialize()
    response_body = {
        "msg": "Ok",
        "data": vehiculo_serialize
    }
    return jsonify(response_body), 200

@api.route('/planetas/<int:planeta_id>', methods=['GET'])
def get_planeta_by_id(planeta_id):
    planeta = Planetas.query.filter_by(id=planeta_id).first()
    planeta_serialize = planeta.serialize()
    response_body = {
        "msg": "Ok",
        "data": planeta_serialize
    }
    return jsonify(response_body), 200

@api.route('/favoritos_personajes/<int:favorito_personaje_id>', methods=['GET'])
def get_favorito_personaje_by_id(favorito_personaje_id):
    favorito_personaje = Favoritos_personajes.query.filter_by(id=favorito_personaje_id).first()
    favorito_personaje_serialize = favorito_personaje.serialize()
    response_body = {
        "msg": "Ok",
        "data": favorito_personaje_serialize
    }
    return jsonify(response_body), 200

@api.route('/favoritos_vehiculos/<int:favorito_vehiculo_id>', methods=['GET'])
def get_favorito_vehiculo_by_id(favorito_vehiculo_id):
    favorito_vehiculo = Favoritos_vehiculos.query.filter_by(id=favorito_vehiculo_id).first()
    favorito_vehiculo_serialize = favorito_vehiculo.serialize()
    response_body = {
        "msg": "Ok",
        "data": favorito_vehiculo_serialize
    }
    return jsonify(response_body), 200

@api.route('/favoritos_planetas/<int:favorito_planeta_id>', methods=['GET'])
def get_favorito_planeta_by_id(favorito_planeta_id):
    favorito_planeta = Favoritos_planetas.query.filter_by(id=favorito_planeta_id).first()
    favorito_planeta_serialize = favorito_planeta.serialize()

    response_body = {
        "msg": "Ok",
        "data": favorito_planeta_serialize
    }

    return jsonify(response_body), 200

############## métodos para POST
@api.route('/users', methods=['POST'])
def create_user():
    body = request.json
    me = Users(name=body["name"], email=body["email"], password=body["password"], is_active=body["is_active"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/personajes', methods=['POST'])
def create_personaje():
    body = request.json
    me = Personajes(name=body["name"], eye_color=body["eye_color"], hair_color=body["hair_color"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    body = request.json
    me = Vehiculos(name=body["name"], model=body["model"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/planetas', methods=['POST'])
def create_planeta():
    body = request.json
    me = Planetas(name=body["name"], population=body["population"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/favoritos_personajes', methods=['POST'])
def create_favorito_personaje():
    body = request.json
    me = Favoritos_personajes(personajes_relacion=body["personajes_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/favoritos_vehiculos', methods=['POST'])
def create_favorito_vehiculo():
    body = request.json
    me = Favoritos_vehiculos(vehiculos_relacion=body["vehiculos_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/favoritos_planetas', methods=['POST'])
def create_favorito_planeta():
    body = request.json
    me = Favoritos_planetas(planetas_relacion=body["planetas_relacion"], usuarios_relacion=body["usuarios_relacion"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

############### métodos para PUT por ID
@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.get(user_id)
    if user:
        body = request.json
        user.name = body.get("name", user.name)
        user.email = body.get("email", user.email)
        user.password = body.get("password", user.password)
        user.is_active = body.get("is_active", user.is_active)
        db.session.commit()
        return jsonify({"msg": "User updated", "data": user.serialize()}), 200
    else:
        return jsonify({"msg": "User not found"}), 404

@api.route('/personajes/<int:personaje_id>', methods=['PUT'])
def update_personaje(personaje_id):
    personaje = Personajes.query.get(personaje_id)
    if personaje:
        body = request.json
        personaje.name = body.get("name", personaje.name)
        personaje.eye_color = body.get("eye_color", personaje.eye_color)
        personaje.hair_color = body.get("hair_color", personaje.hair_color)
        db.session.commit()
        return jsonify({"msg": "Personaje updated", "data": personaje.serialize()}), 200
    else:
        return jsonify({"msg": "Personaje not found"}), 404

@api.route('/vehiculos/<int:vehiculo_id>', methods=['PUT'])
def update_vehiculo(vehiculo_id):
    vehiculo = Vehiculos.query.get(vehiculo_id)
    if vehiculo:
        body = request.json
        vehiculo.name = body.get("name", vehiculo.name)
        vehiculo.model = body.get("model", vehiculo.model)
        db.session.commit()
        return jsonify({"msg": "Vehiculo updated", "data": vehiculo.serialize()}), 200
    else:
        return jsonify({"msg": "Vehiculo not found"}), 404

@api.route('/planetas/<int:planeta_id>', methods=['PUT'])
def update_planeta(planeta_id):
    planeta = Planetas.query.get(planeta_id)
    if planeta:
        body = request.json
        planeta.name = body.get("name", planeta.name)
        planeta.population = body.get("population", planeta.population)
        db.session.commit()
        return jsonify({"msg": "Planeta updated", "data": planeta.serialize()}), 200
    else:
        return jsonify({"msg": "Planeta not found"}), 404

############### métodos para DELETE por ID
@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if user:
        Favoritos_personajes.query.filter_by(usuarios_relacion=user_id).delete()
        Favoritos_vehiculos.query.filter_by(usuarios_relacion=user_id).delete()
        Favoritos_planetas.query.filter_by(usuarios_relacion=user_id).delete()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User and related favoritos deleted"}), 200
    else:
        return jsonify({"msg": "User not found"}), 404

@api.route('/personajes/<int:personaje_id>', methods=['DELETE'])
def delete_personaje(personaje_id):
    personaje = Personajes.query.get(personaje_id)
    if personaje:
        Favoritos_personajes.query.filter_by(personajes_relacion=personaje_id).delete()
        db.session.delete(personaje)
        db.session.commit()
        return jsonify({"msg": "Personaje and related favoritos deleted"}), 200
    else:
        return jsonify({"msg": "Personaje not found"}), 404

@api.route('/vehiculos/<int:vehiculo_id>', methods=['DELETE'])
def delete_vehiculo(vehiculo_id):
    vehiculo = Vehiculos.query.get(vehiculo_id)
    if vehiculo:
        Favoritos_vehiculos.query.filter_by(vehiculos_relacion=vehiculo_id).delete()
        db.session.delete(vehiculo)
        db.session.commit()
        return jsonify({"msg": "Vehiculo and related favoritos deleted"}), 200
    else:
        return jsonify({"msg": "Vehiculo not found"}), 404

@api.route('/planetas/<int:planeta_id>', methods=['DELETE'])
def delete_planeta(planeta_id):
    planeta = Planetas.query.get(planeta_id)
    if planeta:
        Favoritos_planetas.query.filter_by(planetas_relacion=planeta_id).delete()
        db.session.delete(planeta)
        db.session.commit()
        return jsonify({"msg": "Planeta and related favoritos deleted"}), 200
    else:
        return jsonify({"msg": "Planeta not found"}), 404
    
################ métodos para DELETE Favoritos por ID
@api.route('/favoritos_personajes/<int:favorito_personaje_id>', methods=['DELETE'])
def delete_favorito_personaje(favorito_personaje_id):
    favorito_personaje = Favoritos_personajes.query.get(favorito_personaje_id)
    if favorito_personaje:
        db.session.delete(favorito_personaje)
        db.session.commit()
        return jsonify({"msg": "Favorito personaje deleted"}), 200
    else:
        return jsonify({"msg": "Favorito personaje not found"}), 404

@api.route('/favoritos_vehiculos/<int:favorito_vehiculo_id>', methods=['DELETE'])
def delete_favorito_vehiculo(favorito_vehiculo_id):
    favorito_vehiculo = Favoritos_vehiculos.query.get(favorito_vehiculo_id)
    if favorito_vehiculo:
        db.session.delete(favorito_vehiculo)
        db.session.commit()
        return jsonify({"msg": "Favorito vehiculo deleted"}), 200
    else:
        return jsonify({"msg": "Favorito vehiculo not found"}), 404

@api.route('/favoritos_planetas/<int:favorito_planeta_id>', methods=['DELETE'])
def delete_favorito_planeta(favorito_planeta_id):
    favorito_planeta = Favoritos_planetas.query.get(favorito_planeta_id)
    if favorito_planeta:
        db.session.delete(favorito_planeta)
        db.session.commit()
        return jsonify({"msg": "Favorito planeta deleted"}), 200
    else:
        return jsonify({"msg": "Favorito planeta not found"}), 404

################# Terminan mis endpoints


if __name__ == "__main__":
    app.run()
