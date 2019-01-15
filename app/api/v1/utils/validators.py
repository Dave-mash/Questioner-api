from werkzeug.exceptions import BadRequest, Conflict
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
                raise BadRequest('{}. This field is required!'.format(key))

    def valid_name(self):
        if self.username:
            if len(self.username) < 3 or len(self.username) > 20:
                raise BadRequest('Your username is too short!')

    def valid_email(self):
        regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        
        if not re.match(regex, self.email):
            raise BadRequest('Invalid email address!')

    def valid_password(self):
        regex = re.compile(r'[a-zA-Z0-9@_+-.]{3,}$')

        if not re.match(regex, self.password):
            raise BadRequest('Weak password!')

    def matching_password(self):
        if self.password != self.confirm_password:
            raise BadRequest('Your passwords don\'t match')


class MeetupValidator:

    def __init__(self, title, name):
        self.title = title
        self.name = name

    def valid_title(self, title):
        if self.title:
            if len(self.title) < 3 or len(self.title) > 20:
                base_model.errorHandler('Your title is too short!')
        else:
            base_model.errorHandler('No meetup to validate. Pass in something')


class QuestionValidator:

    def __init__(self, title, name):
        self.title = title
        self.name = name

    def valid_topic(self):
        if self.title and self.name:
            if len(self.title) < 10 and len(self.name) < 3:
                base_model.errorHandler('Your question is too short')
        else:
            base_model.errorHandler('No question to validate. Pass in something')