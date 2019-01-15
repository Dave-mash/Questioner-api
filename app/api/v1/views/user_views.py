"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response, Blueprint
from app.api.v1.utils.validators import UserValidator
from app.api.v1.models.user import User
import uuid

v1 = Blueprint('userv1', __name__, url_prefix='/api/v1/')

user = User('user_db')

""" This route fetches all users """
@v1.route("/users")
def get():
    users = user.get_items()

    return make_response(jsonify({
        "status": 200,
        "users": users
    }), 200)

""" This route allows unregistered users to sign up """
@v1.route("/auth/signup", methods=['POST'])
def registration():
    data = request.get_json()
    meetups = user.get_items()

    # Validate user
    validate_user = UserValidator(
        data['first_name'],
        data['last_name'],
        data['username'],
        data['email'],
        data['password'],
        data['confirm_password']
    )

    validate_user.data_exists()
    validate_user.valid_name()
    validate_user.valid_email()
    validate_user.valid_password()
    validate_user.matching_password()
    
    # Register user
    user_data = {
        "id": len(meetups), # str(uuid.uuid4()),
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "othername": data['othername'],
        "email": data['email'],
        "phoneNumber": data['phoneNumber'],
        "username": data['username'],
        "password": data['password'],
    }

    if user.save_user(user_data) == 'This email already exists':
        return make_response(jsonify({
            "error": 'This email already exists'
        }), 409)
    elif user.save_user(user_data) == 'This username is already taken':
        return make_response(jsonify({
            "error": 'This username is already taken'
        }), 409)
    else:
        user.save_user(user_data)

        return make_response(jsonify({
            "status": "ok",
            "message": "{} registered successfully".format(data['email']),
            "username": data['username']
        }), 201)


""" This route allows registered users to sign in """
@v1.route("/auth/login", methods=['POST'])
def login():
    data = request.get_json()

    validate_user = UserValidator(email=data['email'], password=data['password'])
    validate_user.valid_email()
    validate_user.valid_password()

    credentials = {
        "email": data['email'],
        "password": data['password']
    }

    if user.log_in_user(credentials) == 'You entered wrong information. Please check your credentials!':
        return make_response(jsonify({
            "error": "You entered wrong information. Please check your credentials!"
        }), 401) # unauthorised
    else:
        return jsonify({
            "status": 201,
            "message": "{} has been successfully logged in".format(data['email'])
        }), 201
