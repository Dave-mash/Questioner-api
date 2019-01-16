"""
This module contains tests for the base model
"""

import unittest
from app.api.v1.models.base import Base

class TestBaseModelClass(unittest.TestCase):

    def setUp(self):
        self.user = {
            "first_name" : "Dave",
            "last_name" : "Mwangi",
            "othername" : "Dave",
            "email" : "mash@demo.com",
            "phoneNumber" : "0729710290",
            "username" : "Dave",
            "password": "abc123",
            "confirm_password": "abc123"
        }

        self.meetups = {
            "topic": "a meetup",
            "description": "this is a meetup",
            "location": "Nairobi",
            "happeningOn": "12-12-2019",
            "tags": "['Django', 'Flask']"
        }

        self.questions = {
            "title": "Python",
            "createdBy": "Dave",
            "body": "Python is an amazing language"
        }

    def test_check_db(self):

        base = Base('users_db')
        self.assertEqual(base.db_name, 'users_db')

        base = Base('meetups_db')
        self.assertEqual(base.db_name, 'meetups_db')

        base = Base('meetups_db')
        self.assertEqual(base.db_name, 'meetups_db')
