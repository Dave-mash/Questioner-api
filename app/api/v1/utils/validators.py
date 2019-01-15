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
            if len(self.username) < 3 or len(self.username) > 20:
                return base_model.errorHandler('Your username is too short!')

    def valid_email(self):
        regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        
        if not re.match(regex, self.email):
            return base_model.errorHandler('Invalid email address!')

    def valid_password(self):
        regex = re.compile(r'[a-zA-Z0-9@_+-.]{3,}$')

        if not re.match(regex, self.password):
            return base_model.errorHandler('Weak password!')

    def matching_password(self):
        if self.password != self.confirm_password:
            return base_model.errorHandler('Your passwords don\'t match')


class MeetupValidator:

    def __init__(self,
        title='',
        description='',
        tags=[],
        happeningOn='',
        location=''
    ):
        self.title = title
        self.tags = tags
        self.happeningOn = happeningOn
        self.description = description
        self.location = location

    def data_exists(self):
        if not self.title or not self.happeningOn or not self.description or not self.location:
            return 'You missed a required field'

    def valid_topic(self):
        if len(self.title) < 3:
            return 'Your topic is too short!'
        elif len(self.title) > 30:
            return 'Your topic is too long!'

    def valid_description(self):
        if len(self.description) < 5:
            return 'Your description is too short'
        elif len(self.description) > 30:
            return 'Your description is too long'

    def valid_tags(self):
        if len(self.tags) == 0:
            return 'Have at least one tag'

    def valid_date(self):
        try:
            datetime.strptime(self.happeningOn, '%d-%m-%Y')
        except:
            return 'Date format should be YYYY-MM-DD'

    def valid_location(self):
        if len(self.location) < 3:
            return 'Enter a valid location!'

class QuestionValidator(MeetupValidator):

    def __init__(self, title='', description=''):
        self.title = title
        self.description = description

    def data_exists(self):
        if not self.title or not self.description:
            return 'You missed a required field'

    def valid_title(self):
        if len(self.title) < 10 and len(self.description) < 3:
            return 'Your question is too short. Try being abit more descriptive'

# Access valid_description from MeetupValidator