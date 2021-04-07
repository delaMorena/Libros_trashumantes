"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import datetime
import hashlib
import hmac
# import jwt

from flask import Flask, request, jsonify, url_for, Blueprint, abort
from api.models import db, Users, Packages, Reservations, Reviews 
from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)

####################################    KEYS    #################################
MAC= 'D9GSf7pVqNXYhSKKE4LLh8ARBrMJGNuH'
JWT_SECRET= 'HGRrM3xhfSEzNY7qDypJK6YMyaTFD76d'

#################################    ENDPOINTS    #################################
################################# REFACTORITATION #################################
# Validación de datos en actualizar.
def validation_and_payload(Models): 
    model = Models.query.get(id)

    if not user:
        return f"{model} not found", 404
        
    payload = request.get_json()

    required = models.notebook(models).keys()

    for field in required:
        if field in payload :
            model.field = payload[field]

    db.session.add(model)
    db.session.commit()

    return jsonify(model.serialize()), 201

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
def authorized_user():
    authorization = request.headers.get('Authorization')

    if not authorization:
        abort(403)

    token = authorization[7:]
    secret = JWT_SECRET.encode('utf-8')
    algo = "HS256"

    payload = jwt.decode(token, secret, algorithms= [algo])
    user = Users.query.filter_by(email=payload["sub"], deleted_at=None).first()

    return user
    
###################################    USERS    #################################
@api.route("/users", methods=["POST"])
def handle_create_user():
    # required = ["first_name", "last_name", "username", "email", "password", "dni"]
    # types = {
    #     "first_name": str,
    #     "last_name": str,
    #     "username": str,
    #     "email": str,
    #     "password": str,
    #     "dni": int
    # }
    payload = request.get_json()

    # for key, value in payload.items():
    #     if key in types and not isinstance(value, types[key]):
    #         abort(400, f"{key} is not {types[key]}")

    # for field in required:
    #     if field not in payload or payload[field] is None:
    #         abort(400, "este es un mensaje en el error 400")

    # key = MAC.encode('utf-8')
    # msg = payload['password'].encode('utf-8')
    # algo = hashlib.sha512

    payload['password'] = hmac.new(key, msg, algo).hexdigest()

    user = Users(**payload)
    db.session.add(user)
    db.session.commit()

    email = {'sub': user.email}
    secret = JWT_SECRET.encode('utf-8')
    algo="HS256"

    token = jwt.encode(email, secret, algorithm=algo)

    return jsonify({"token":token}), 201

@api.route("/login", methods=["POST"])# no es un GET porque el metodo get no deja pasar nada en el body
def login():
    payload= request.get_json()

    email = payload['email']
    password = payload['password']

    user = Users.query.filter_by(email=email, deleted_at=None).first()

    if not user:
        return "Forbidden", 403

    key = MAC.encode('utf-8')
    msg = payload['password'].encode('utf-8')
    algo = hashlib.sha512

    hashed_password = hmac.new(key, msg, algo).hexdigest()

    if hashed_password != user.password:
        return "Forbidden", 403
    
    secret = JWT_SECRET.encode('utf-8')
    payload = {"sub": user.email}
    algo = "HS256"
    token = jwt.encode(payload, secret, algorithm=algo)

    return jsonify({"token": token}), 201

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
    packages = []

    for package in Packages.query.all():
        packages.append(package.serialize())    
    return jsonify(packages), 201

@api.route("/packages/<int:id>", methods=["GET"])
def handle_get_one_package(id):
    package = Packages.query.get(id)

    if not package: 
        return "Package not found", 404
    return jsonify(package.serialize()), 201


################################# VOLUNTEERS #################################
@api.route("/volunteers", methods=["GET"])
def handle_get_all_volunteers():
    volunteers = []

    for volunteer in Volunteers.query.all():
        volunteers.append(volunteer.serialize())
    return jsonify(volunteers), 201


@api.route("/volunteers/<int:id>", methods=["GET"])
def handle_get_one_volunteer(id):
    
    volunteer = Volunteers.query.get(id)

    if not volunteer: 
        return "Volunteer not found", 404
    
    return jsonify(volunteer.serialize()), 201

################################# RESERVATIONS #################################
@api.route("/reservations", methods= ["POST"])
def handle_create_reservation():

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

    reservation = Reservations(**payload)

    db.session.add(reservation)
    db.session.commit()

    return jsonify(reservation.serialize()), 201
# GET all/one
#obtener todas las reservas
@api.route("/reservations", methods=["GET"])
def handle_get_all_reservations():
    reservations = []

    for reservation in Reservations.query.filter_by(deleted_at=None).all():
        reservations.append(reservation.serialize())

    return jsonify(reservations), 200

# obtener las reservas de un usuario específico
@api.route("/users/reservations", methods=["GET"])
def handle_get_reservations():

    user = authorized_user()

    if not user:
        return "User not authorized", 403

    reservations = []

    for reservation in user.reservations:
        reservations.append(reservation.serialize())

    reservations.sort(key=lambda x: x.get("updated_at"),reverse=True)

    if not reservation:
        return "Reservation not found", 404
        
    return jsonify(reservation.serialize()), 200

#obtener las reservas de un paquete específico
@api.route("/packages/reservations/<int:id>", methods=["GET"])
def handle_list_reservations_from_a_package(id):

    package = Packages.query.filter_by(id=id, deleted_at=None).first()
    reservations = []

    if not package:
        return "Package not found", 404

    for reservation in package.reservations:
        reservations.append(reservation.serialize())
        
    # posts.sort(key=lambda x: x.get("updated_at"),reverse=True)

    return jsonify(reservations), 200

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

# GET all reviews from a package
@api.route('/packagess/reviews/<int:package_id>', methods=['GET'])
def handle_get_list_of_reviews(package_id):
    reviews = []

    for review in  Reviews.query.filter_by(package_id = package_id, deleted_at=None):
        reviews.append(review.serialize())

    return jsonify(reviews), 200

# GET one review from a book, pienso que se utilizaría cuando un usuario quiera ver su
@api.route('/books/review/<int:package_id>', methods=['GET'])
def handle_get_one_review(package_id):

    review = Reviews.query.filter_by(package_id = package_id, deleted_at = None).first()
    
    if not review:
        abort(404)

    if review.deleted_at:
        abort(401)

    return jsonify(review.serialize()), 200

################################# BOOKS #################################
#Los agregaremos desde el admin

################################# RATINGS #################################
# POST
# GET all/one