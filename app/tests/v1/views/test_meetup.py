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
            "happeningOn" : "12-12-2018",
            "location" : "Nairobi",
            "tags": ["Machine learning", "Neural networks"],
            "topic": "Python data structures",
            "description": "Deep dive into python",
        }

    def post_req(self, path='api/v1/meetups', data={}):
        """ This function utilizes the test client to send POST requests """
        data = data if data else self.meetup
        data['id'] = len(self.db)
        self.db.append(data)
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

    def test_get_all_upcoming_meetups(self):
        """ Test that all meetups can be fetched """

        get = self.get_req('/api/v1/meetups/upcoming')
        self.assertEqual(get.status_code, 200)

    def test_create_meetup_record(self):
        """ Test that a user can create a meetup """
    
        payload = self.post_req(data=self.meetup)
        self.assertEqual(payload.status_code, 201)
        self.assertEqual(payload.json['message'], "You have successfully posted a meetup")

    def test_create_meetup_invalid_input(self):

        # Invalid description
        meetup = { **self.meetup }
        meetup['description'] = 'py'
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)

        # None-existing data
        meetup = { **self.meetup }
        meetup['description'] = ''
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)
        
        # Invalid topic
        meetup = { **self.meetup }
        meetup['topic'] = 'p'
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)
        
        # Invalid tags
        meetup = { **self.meetup }
        meetup['tags'] = []
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)
        
        # Invalid date
        meetup = { **self.meetup }
        meetup['happeningOn'] = '2018/12/12'
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)
        
        # Invalid location
        meetup = { **self.meetup }
        meetup['location'] = 'na'
        payload = self.post_req(data=meetup)
        self.assertEqual(payload.status_code, 422)
        
    def test_fetch_specific_meetup(self):
        """ Test that a user can fetch specific meetup """
        self.db = []

        self.post_req()
        self.post_req()

        meetup = [meetup for meetup in self.db if meetup['id'] == 1]
        res = self.get_req('api/v1/meetups/1')
        self.assertEqual(res.status_code, 200)

        meetup = [meetup for meetup in self.db if meetup['id'] == 5]
        res2 = self.get_req('api/v1/meetups/5')
        self.assertEqual(res2.status_code, 404)

    def test_meetup_rsvps(self):
        """ This method tests that a user can rsvp on a meeting """
        rsvp = {
            "meetup": 0,
            "topic": "PYTHON",
            "status": "yes"
        }

        self.db = []

        # tests for existing meetup
        self.post_req()

        meetup = [meetup for meetup in self.db if meetup['id'] == rsvp['meetup']]

        payload = self.post_req(path="/api/v1/meetups/0/rsvp", data=rsvp)
        self.assertEqual(payload.status_code, 201)
        topic = meetup[0]['topic'].upper()

        rsvp2 = { "id": 0, "status": "yes" }
        rsvp.update(rsvp2)
        payload = self.post_req(path="/api/v1/meetups/0/rsvp", data=rsvp)
        self.assertEqual(payload.json['message'], "You have successfully RSVP'd on {} meetup".format(topic))
        
        rsvp3 = { "id": 0, "status": "no" }
        rsvp.update(rsvp3)
        payload = self.post_req(path="/api/v1/meetups/0/rsvp", data=rsvp)
        self.assertEqual(payload.json['message'], "You have confirmed you're not attending the {} meetup".format(topic))

        rsvp4 = { "id": 0, "status": "maybe" }
        rsvp.update(rsvp4)
        payload = self.post_req(path="/api/v1/meetups/0/rsvp", data=rsvp)
        self.assertEqual(payload.json['message'], "You have confirmed you might attend the {} meetup".format(topic))

        # Test for non-existing meetup
        rsvp5 = { "id": 5, "status": "maybe" }
        rsvp.update(rsvp5)
        payload = self.post_req(path="/api/v1/meetups/5/rsvp", data=rsvp)
        self.assertEqual(payload.status_code, 404) # not found
        
    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.db = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()

