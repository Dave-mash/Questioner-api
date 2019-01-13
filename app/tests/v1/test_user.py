"""
This module tests the user authentication endpoint
Author: Dave
"""

import unittest
from werkzeug._compat import text_type
from werkzeug.exceptions import BadRequest 
import json
from app import create_app

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.user_list = []

        self.user = {
            "first_name": "David",
            "last_name": "Mwangi",
            "othername": "Mash",
            "email": "dave@gmail.com",
            "phoneNumber": "0729710290",
            "username": "Dave",
            "isAdmin": False,
            "password": "abc123",
            "confirm_password": "abc123"
        }

    def post_req(self, path='api/v1/auth/signup', data={}):
        """ This function utilizes the test client to send POST requests """
        data = data if data else self.user
        res = self.client.post(
            path,
            data=json.dumps(data),
            content_type='application/json'
        )
        return res

    def get_req(self, path):
        """ This function utilizes the test client to send GET requests """
        self.user_list = []
        res = self.client.get(path)
        return res 

    # def test_sign_up_user(self):
    #     """ Test that an unregistered user can sign up """

    #     self.user_list.append(self.user)
    #     payload = self.post_req(data=self.user_list[0])

    #     self.assertEqual(payload.status_code, 201) # Created
    #     self.assertEqual(self.user['username'], payload.json['username'])
    #     self.assertEqual(payload.json['message'], "{} registered successfully".format(self.user['email']))

    def test_get_all_users(self):
        """ Test that all users can be fetched """

        get = self.get_req('/api/v1/users')
        self.assertEqual(get.status_code, 200)
        self.assertEqual(get.json['users'], [])


    def test_sign_up_user_invalid_input(self):
        """ Test that registering wit invalid input will throw an error """
        # Invalid email
        user = { **self.user }
        user['email'] = 'davegmail.com'
        payload = self.post_req(data=user)
        self.assertEqual(payload.status_code, 400)
        # assert text_type(invalid_email) == "<BadRequest '400: Invalid email address!'>"
        
        # Short username
        user2 = { **self.user }
        user2['username'] = 'D'
        payload = self.post_req(data=user2)
        self.assertEqual(payload.status_code, 400)
        # self.assertEqual(payload.json['Error'], "Your username is too short!")

        # Weak password
        user3 = { **self.user }
        user3['password'] = 'ab'
        user3['confirm_password'] = 'ab'
        payload = self.post_req(data=user3)
        self.assertEqual(payload.status_code, 400)
        # self.assertEqual(payload.json['Error'], "Weak password!")

        # Unmatching passwords
        user4 = { **self.user }
        user4['password'] = 'abc123'
        user4['confirm_password'] = 'abc'
        payload = self.post_req(data=user4)
        self.assertEqual(payload.status_code, 400)
        # self.assertEqual(payload.json['Error'], "Your passwords don\'t match")
        
        # Missed field
        user5 = { **self.user }
        user5['username'] = ''
        payload = self.post_req(data=user5)
        self.assertEqual(payload.status_code, 400)
        user4['confirm_password'] = 'abc'
        # self.assertEqual(payload.json['Error'], {}. This field is required!'.format(key))

    def test_sign_up_user_existing_account(self):
        """ Test that registering with an already taken username or email, will throw an error """

        self.post_req(data=self.user)

        user = self.user
        payload = self.post_req(data=user)

        self.assertEqual(payload.status_code, 409) # Conflict

        user2 = self.user
        user2['email'] = "mash@gmail.com"
        payload = self.post_req(data=user2)

        user3 = {}
        payload = self.post_req(data=user3)

        self.assertEqual(payload.status_code, 409) # Conflict

    def test_log_in_user(self):
        """ Test that user can log in with correct credintials """

        self.post_req(data=self.user)

        user = {
            "email": self.user['email'],
            "password": self.user['password']
        }

        payload = self.post_req(path="api/v1/auth/login", data=user)
        self.assertEqual(payload.status_code, 201)


    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.user_list = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()

