"""
This module tests the user authentication endpoint
Author: Dave
"""
import datetime
import unittest
import json
from app import create_app

class TestMeetups(unittest.TestCase):
    db = []
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.meetup = {
            "happeningOn" : "12/12/2018",
            "location" : "Nairobi",
            "createdOn": "{}".format(datetime.datetime.now()),
            "tags": ["Machine learning", "Neural networks"],
            "topic" : "Python data structures",
        }

    def post_req(self, path='api/v1/meetups', data={}):
        """ This function utilizes the test client to send POST requests """
        data = data if data else self.meetup
        res = self.client.post(
            path,
            data=json.dumps(data),
            content_type='application/json'
        )
        return res

    def get_req(self, path):
        """ This function utilizes the test client to send GET requests """
        
        res = self.client.get(path)
        return res 

    def test_get_all_meetups(self):
        """ Test that all meetups can be fetched """

        get = self.get_req('/api/v1/meetups')
        self.assertEqual(get.status_code, 200)
        # self.assertEqual(get.json['meetups'], self.db)

    def test_create_meetup_record(self):
        """ Test that a user can create a meetup """
    
        payload = self.post_req(data=self.meetup)
        self.assertEqual(payload.status_code, 201)
        self.assertEqual(payload.json['message'], "You have successfully posted a meetup")

        """ Test that meetup topic must be unique """

        # self.post_req()
        # self.assertEqual(payload.status_code, 422) # Unprocessable entity
        # self.assertEqual(payload.json['Error'], "Please make your topic unique.")

    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.db = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()

