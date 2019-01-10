"""
This module defines all the user endpoints
"""

from flask import request, jsonify, make_response
from app.api.v1.utils.validators import RegistrationForm
from app.api.v1.models.user_model import UserModel
from .. import version1 as v1

user_model = UserModel()

""" This route fetches all users """
@v1.route("/users/", methods=['GET'])
def get():
    return make_response(jsonify({
        "users": user_model.db
    }), 200)

""" This route allows unregistered users to sign up """
@v1.route("/auth/signup/", methods=['POST'])
def registration():
    data = request.get_json()

    # Create user
    user1 = RegistrationForm(
        data['first_name'],
        data['last_name'],
        data['username'],
        data['email'],
        data['password'],
        data['confirm_password']
    )
    def json(error, status=422):
        return make_response(jsonify({
            "status": status,
            "Error": error
        }), status)

    # prompt user fields
    if not user1.data_exists():
        return json('You missed a required field')
    elif not user1.valid_name():
        return json('Your username is too short!')
    elif not user1.valid_email(data['email']):
        return json('Invalid email address')
    elif not user1.valid_confirm_password():
        return json('Your passwords don\'t match')
    elif not user1.valid_password(data['password']):
        return json('Weak password')
    
    # Register user
    user_model.create_account(
        {
            "username": data['username'],
            "email": data['email'],
            "password": data['password'],
            "logged on": user_model.logged[0]
        }
    )

    if user_model.dup_email:
        return json(user_model.dup_email['Error'], 409)
    elif user_model.dup_username:
        return json(user_model.dup_username['Error'], 409)

    return make_response(jsonify({
        "status": "ok",
        "message": "{} registered successfully".format(data['email']),
        "username": data['username']
    }), 201)


