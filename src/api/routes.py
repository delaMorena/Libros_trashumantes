"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Packages, Connections, Leandings, Reviews, Ratings
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

############################ ENPOINTS #################################

################################# USERS #################################


@api.route("/users", methods=["POST"])
def handle_create_user():
    
    return jsonify(user), 201

@api.route("/users", methods=["GET"])
def handle_get_all_users():
    
    return jsonify(Users), 201

@api.route("/users/<int:id>", methods=["GET"])
def handle_get_one_user(id):
    
    return jsonify(user), 201

@api.route("/users/<int:id>", methods=["PUT"])
def handle_update_one_user(id):
    
    return jsonify(user), 201

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
    
    return jsonify(Connections), 201

@api.route("/packages/<int:id>", methods=["GET"])
def handle_get_one_connections(id):
    
    return jsonify(connection), 201

################################# LEANDINGS #################################
# POST
# GET all/one
# PUT

################################# REVIEWS #################################
# POST
# GET all/one
# PUT

################################# RATINGS #################################
# POST
# GET all/one
# PUT