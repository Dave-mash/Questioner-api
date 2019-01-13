"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response, Blueprint
from app.api.v1.utils.validators import Validator
from app.api.v1.models.user_model import UserModel
import uuid

v1 = Blueprint('userv1', __name__, url_prefix='/api/v1/')

user_model = UserModel('user_db')

""" This route fetches all users """
@v1.route("/users")
def get():
    users = user_model.get_items()

    return make_response(jsonify({
        "status": 200,
        "users": users
    }), 200)

""" This route allows unregistered users to sign up """
@v1.route("/auth/signup", methods=['POST'])
def registration():
    data = request.get_json()
    meetups = user_model.get_items()

    # Validate user
    user1 = Validator(
        data['first_name'],
        data['last_name'],
        data['username'],
        data['email'],
        data['password'],
        data['confirm_password']
    )

    user1.data_exists()
    user1.valid_name()
    user1.valid_email()
    user1.valid_password()
    user1.matching_password()
    
    # Register user
    user_item = {
        "id": len(meetups), # str(uuid.uuid4()),
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "othername": data['othername'],
        "email": data['email'],
        "phoneNumber": data['phoneNumber'],
        "username": data['username'],
        "password": data['password'],
    }

    user_model.save_user(user_item)

    return make_response(jsonify({
        "status": "ok",
        "message": "{} registered successfully".format(data['email']),
        "username": data['username']
    }), 201)


""" This route allows registered users to sign in """
@v1.route("/auth/login", methods=['POST'])
def login():
    data = request.get_json()

    user1 = Validator(email=data['email'], password=data['password'])
    user1.valid_email()
    user1.valid_password()

    credentials = {
        "email": data['email'],
        "password": data['password']
    }

    user_model.log_in_user(credentials)

    return jsonify({
        "status": 201,
        "message": "{} has been successfully logged in".format(data['email'])
    }), 201