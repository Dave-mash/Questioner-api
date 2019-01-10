"""
This module tests the user authentication endpoint
Author: Dave
"""
import datetime
import unittest
import json
from app import create_app

class TestMeetups(unittest.TestCase):
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app()
        self.app.testing = False
        self.client = self.app.test_client()
        self.meetups_list = []
        meetup = {
            "id" : len(self.meetups_list),
            "createdOn" : datetime.datetime.now(),
            "location" : "Nairobi",
            "topic" : "Python data structures",
            "happeningOn" : datetime.date.today() + datetime.timedelta(days=1)
        }

    def post_req(self, path='api/v1/meetup/', data={}):
        """ This function utilizes the test client to send POST requests """
        # data = data if data else self.meetups[0]
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

        get = self.get_req('/api/v1/meetups/')
        self.assertEqual(get.status_code, 200)
        self.assertEqual(get.json['meetups'], [])


    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.app.testing = False
        self.app = None
        # self.meetup = []


if __name__ == "__main__":
    unittest.main()

