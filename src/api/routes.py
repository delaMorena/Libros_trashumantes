"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import datetime
import hashlib
import hmac
# import jwt

from flask import Flask, request, jsonify, url_for, Blueprint, abort
from api.models import db, Users, Packages, Connections, Leandings, Reviews, Ratings
from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)

####################################    KEYS    #################################
# MAC=
# JWT_SECRET=
#################################    ENPOINTS    #################################
################################# REFACTORITATION #################################
def get_one_or_404(model, id):
    row = model.query.filter_by(id=id, deleted_at=None).first()

    if not row:
        abort(404)
        # return "{} not found".format(model), 404 # PENDIENTE DE CONCATENAR EL NOMBRE DE LA TABLA
        
    return jsonify(row.serialize()), 200


def get_all_from_models(model):
    newList = []

    for item in model.query.filter_by(deleted_at=None).all():
        newList.append(item.serialize())

    return jsonify(newList), 200
################################# AUTHORIZED_USERS #################################
# def authorized_user():
#     authorization = request.headers.get('Authorization')

#     if not authorization:
#         abort(403)

#     token = authorization[7:]
#     secret = JWT_SECRET.encode('utf-8')
#     algo = "HS256"

#     payload = jwt.decode(token, secret, algorithms= [algo])
#     user = Users.query.filter_by(email=payload["sub"], deleted_at=None).first()

#     return user
###################################    USERS    #################################

print('Hello World')

@api.route("/users", methods=["POST"])
def handle_create_user():

    payload= request.get_json()

    user = Users(**payload)

    db.session.add(user)
    db.session.commit()
    print(payload, user)

    return jsonify(user.serialize()), 201

@api.route("/login", methods=["POST"])# no es un GET porque el metodo get no deja pasar nada en el body
def login():
    payload= request.get_json()

    email = payload['email']
    password = payload['password']

    user = Users.query.filter_by(email=email, deleted_at=None).first()

    if not user:
        return "Forbidden", 403

    #falta la validación del usuario y obtener el token

    return jsonify(user)

@api.route("/users", methods=["GET"])
def handle_get_all_users():
    users = []

    for user in Users.query.all():
        users.append(user.serialize())
    return jsonify(users), 201

@api.route("/users/<int:id>", methods=["GET"])
def handle_get_one_user(id):
    user = Users.query.get(id)

    if not user: 
        return "User not found", 404
    
    return jsonify(user.serialize()), 201

@api.route("/users/<int:id>", methods=["PUT"])
def handle_update_one_user(id):
    user = Users.query.get(id) 

    if not user: 
        return "User not found", 404
    
    payload = request.get_json()

    user.village = payload["village"]
    user.age = payload["age"]
    
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 200


@api.route("/users/<int:id>", methods=["DELETE"])
def handle_delete_user(id):
    user = Users.query.filter_by(id=id, deleted_at=None).first()

    if not user:
        return "User not found", 404

    user.deleted_at = datetime.datetime.utcnow()

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 200

################################# PACKAGES  #################################
@api.route("/packages", methods=["GET"])
def handle_get_all_packages():
    
    return jsonify(Packages), 201

@api.route("/packages/<int:id>", methods=["GET"])
def handle_get_one_package(id):
    
    return jsonify(package), 201


################################# CONNECTIONS #################################
@api.route("/connections", methods=["GET"])
def handle_get_all_connections():
    connections = []

    for connection in Connections.query.all():
        connections.append(connection.serialize())
    return jsonify(connections), 201


@api.route("/packages/<int:id>", methods=["GET"])
def handle_get_one_connections(id):
    
    connection = Connections.query.get(id)

    if not connection: 
        return "Connection not found", 404
    
    return jsonify(connection.serialize()), 201

################################# LEANDINGS #################################
@api.route("/leandings", methods= ["POST"])
def handle_create_leanding():

    payload = request.get_json()

    user = authorized_user()

    payload['user_id'] = user.id
    required = ['returning_date', 'user_id', 'package_id']
   
   ####Duda: qué es required y como valido el tipo de dato para una fecha??

    types = {
        'returning_date': int,
        'user_id': int,
        'post_id': int
    }
    
    for key, value in payload.items():
        if key in types and not isinstance(value, types[key]):
            abort(400, f"{key} is not {types[key]}")
    
    for field in required:
        if field not in payload or payload[field] is None:
            abort(400)

    leanding = Leandings(**payload)

    db.session.add(leanding)
    db.session.commit()

    return jsonify(leanding.serialize()), 201
# GET all/one
#obtener todas las reservas

# obtener las reservas de un usuario específico
@api.route("/leandings/<int:id>", methods=["GET"])
def handle_get_leandings(id):

    user = authorized_user()

    if not user:
        return "User not authorized", 403

    leanding = Leandings.query.filter_by(id=id, deleted_at=None).first()

    if not leanding:
        return "Leanding not found", 404
        
    return jsonify(leanding.serialize()), 200

#obtener las reservas de un paquete específico
@api.route("/package/<int:id>", methods=["GET"])
def handle_list_leanding_from_a_package(id):

    package = Packages.query.filter_by(id=id, deleted_at=None).first()
    leandings = []

    if not package:
        return "Package not found", 404

    for leanding in package.leanding:
        leandings.append(leanding.serialize())
        
    # posts.sort(key=lambda x: x.get("updated_at"),reverse=True)

    return jsonify(leandings), 200

# PUT or DELETE???? DUDA

################################# REVIEWS #################################
#create a review
@api.route("/reviews", methods=["POST"])
def handle_create_review():
    user = authorized_user()

    payload = request.get_json()
    payload["user_id"] = user.id
    reviews = Reviews(**payload)

    db.session.add(reviews)
    db.session.commit()

    return jsonify(reviews.serialize()), 201

# GET all reviews from a book
@api.route('/books/reviews/<int:book_id>', methods=['GET'])
def handle_get_list_of_reviews(book_id):
    reviews = []

    for review in  Reviews.query.filter_by(book_id = book_id, deleted_at=None):
        reviews.append(review.serialize())

    return jsonify(reviews), 200

# GET one review from a book, pienso que se utilizaría cuando un usuario quiera ver sus comentarios de un libro en específico
@api.route('/books/review/<int:book_id>', methods=['GET'])
def handle_get_one_review(book_id):
    user = authorized_user()

    review = Reviews.query.filter_by(book_id = book_id, user_id = user.id, deleted_at = None).first()
    
    if not review:
        abort(404)

    if review.deleted_at:
        abort(401)

    return jsonify(review.serialize()), 200

# PUT ¿lo necesitamos?
# DELETE ¿lo necesitamos?
################################# BOOKS #################################


################################# RATINGS #################################
# POST
# GET all/one
# PUT