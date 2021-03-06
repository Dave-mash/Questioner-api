"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response, Blueprint
from app.api.v1.utils.user_validators import UserValidator
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
    try:
        validate_user = UserValidator(
            data['first_name'],
            data['last_name'],
            data['username'],
            data['email'],
            data['password'],
            data['confirm_password']
        )
    except:
        return jsonify({
            "error": "You missed a field"
        })

    def errorHandler(error):
        return make_response(jsonify({
            "error": error
        }), 422) 
    
    if validate_user.data_exists():
        return errorHandler(validate_user.data_exists())
    elif validate_user.valid_name():
        return errorHandler(validate_user.valid_name())
    elif validate_user.valid_email():
        return errorHandler(validate_user.valid_email())
    elif validate_user.validate_password():
        return errorHandler(validate_user.validate_password())
    elif validate_user.matching_password():
        return errorHandler(validate_user.matching_password())
    else:    
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

    try:
        validate_user = UserValidator(email=data['email'], password=data['password'])
        validate_user.valid_email()
        validate_user.validate_password()

        credentials = {
            "email": data['email'],
            "password": data['password']
        }
    except:
        return jsonify({
            "error": "You missed a field"
        })

    if user.log_in_user(credentials) == 'You entered wrong information. Please check your credentials!':
        return make_response(jsonify({
            "error": "You entered wrong information. Please check your credentials!"
        }), 401) # unauthorised
    else:
        return jsonify({
            "status": 201,
            "message": "{} has been successfully logged in".format(data['email'])
        }), 201
