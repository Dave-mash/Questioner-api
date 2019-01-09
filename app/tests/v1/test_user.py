"""
This module tests the user authentication endpoint
Author: Dave
"""
import unittest
import json
from app import create_app

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app()
        self.app.testing = False
        self.client = self.app.test_client()

        self.user = {
            "first_name": "David",
            "last_name": "Mwangi",
            "username": "Dave",
            "email": "dave@gmail.com",
            "password": "abc123",
            "confirm_password": "abc123"
        }

        self.log_user = {
            "email": self.user['email'],
            "password": self.user['password']
        }

    def post_req(self, path='api/v1/auth/signup', data={}):
        """ This function uses the test client to send POST requests """
        data = data if data else self.user
        res = self.client.post(
            path,
            data=json.dumps(data),
            content_type='application/json'
        )
        return res

    def get_req(self, path):
        """ This function uses the test client to send GET requests """
        res = self.client.get(path)
        return res 

    def test_sign_up_user(self):
        """ Test that an unregistered user can sign up """
        payload = self.post_req(data=self.user)

        self.assertEqual(payload.status_code, 201) # Created
        self.assertEqual(self.user['username'], payload.json['username'])

    def test_get_all_users(self):
        """ Test that all users can be fetched """

        get = self.get_req('/api/v1/users')
        self.assertEqual(get.status_code, 200) # Ok
        self.assertEqual(get.json['users'], [])


    def test_sign_up_user_invalid_input(self):
        """ Test that registering wit invalid input will throw an Error """

        # Invalid email
        user = { **self.user }
        user['email'] = 'davegmail.com'
        payload = self.post_req(data=user)
        self.assertEqual(payload.status_code, 422) # Unprocessable Entity
        self.assertEqual(payload.json['Error'], "Invalid email address")
        
        # Short username
        user2 = { **self.user }
        user2['username'] = 'D'
        payload = self.post_req(data=user2)
        self.assertEqual(payload.status_code, 422) # Unprocessable Entity
        self.assertEqual(payload.json['Error'], "Your username is too short!")

        # Weak password
        user3 = { **self.user }
        user3['password'] = 'ab'
        user3['confirm_password'] = 'ab'
        payload = self.post_req(data=user3)
        self.assertEqual(payload.status_code, 422) # Unprocessable Entity
        self.assertEqual(payload.json['Error'], "Weak password")

        # Unmatching passwords
        user4 = { **self.user }
        user4['password'] = 'abc123'
        user4['confirm_password'] = 'abc'
        payload = self.post_req(data=user4)
        self.assertEqual(payload.status_code, 422) # Unprocessable Entity
        self.assertEqual(payload.json['Error'], "Your passwords don\'t match")
        
        # Missed field
        user5 = { **self.user }
        user5['username'] = ''
        payload = self.post_req(data=user5)
        self.assertEqual(payload.status_code, 422) # Unprocessable Entity
        user4['confirm_password'] = 'abc'
        self.assertEqual(payload.json['Error'], "You missed a required field")

    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()

