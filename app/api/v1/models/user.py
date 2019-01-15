"""
This module defines the user model class and all it's methods
"""

from werkzeug.security import generate_password_hash
from datetime import datetime
import uuid

from app.api.v1.models.base import Base

class User(Base):
    """ add user a user to a database """

    base_model = Base("user_db")

    # Save data
    def save_user(self, user_item):
        if user_item:
            user = {
                "first_name": user_item['first_name'],
                "last_name": user_item['last_name'],
                "othername": user_item['othername'],
                "email": user_item['email'],
                "phoneNumber": user_item['phoneNumber'],
                "username": user_item['username'],
                "dateRegistered": str(datetime.today()),
                "password": user_item['password'],
                "isAdmin": False,
                "rsvps": []
            }
            
            # Check for duplicate email and username
            db = self.base_model.get_items()
            dup_email = [users for users in db if users['email'] == user_item['email']]
            dup_username = [users for users in db if users['username'] == user_item['username']]
            
            if dup_email:
                return self.errorHandler('This email already exists')
            elif dup_username:
                return self.errorHandler('This username is already taken')
            else:
                return self.base_model.save_data(user)

    # Log in user
    def log_in_user(self, details):

        # Check if user details exists
        db = self.base_model.get_items()
        exists_email = [email for email in db if email['email'] == details['email']]
        match_pass = [p_word for p_word in db if p_word['password'] == details['password']]

        if not exists_email or not match_pass:
            return self.errorHandler('You entered wrong information. Please check your credentials!')


    # Edit data
    def edit_user(self, updates, user_id):
        try:
            if updates and user_id:
                self.base_model.update_data(user_id, updates)
        except:
            return self.errorHandler('No data found')

    # Delete data
    def del_user(self, user_id):
        try:
            if user_id:
                self.base_model.delete_data(user_id)
        except:
            return self.errorHandler('No data found')

    # Fetch users
    def get_users(self):
        self.base_model.get_items()