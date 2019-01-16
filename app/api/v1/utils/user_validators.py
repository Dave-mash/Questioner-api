"""
This module takes care of validating input from the endpoints
"""

from datetime import datetime
import re

from app.api.v1.models.base import Base

base_model = Base()

class UserValidator:
    
    def __init__(
        self,
        Fname="",
        Lname="",
        username="",
        email="",
        password="",
        confirm_password=""
    ):
        self.Fname = Fname
        self.Lname = Lname
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def data_exists(self):

        data = {
            "Fname": self.Fname,
            "Lname": self.Lname,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }

        for key, value in data.items():
            if not value:
                return base_model.errorHandler('You missed a required field {}.'.format(key))

    def valid_name(self):
        if self.username:
            if len(self.username) < 3:
                return base_model.errorHandler('Your username is too short!')
            elif len(self.username) > 20:
                return base_model.errorHandler('Your username is too long!')

    def valid_email(self):
        reg_email = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        
        if not re.match(reg_email, self.email):
            return base_model.errorHandler('Invalid email address!')

    def validate_password(self):
        reg_password = re.compile(r'[a-zA-Z0-9@_+-.]{3,}$')

        if not re.match(reg_password, self.password):
            return base_model.errorHandler('Weak password!')

    def matching_password(self):
        if self.password != self.confirm_password:
            return base_model.errorHandler('Your passwords don\'t match')

