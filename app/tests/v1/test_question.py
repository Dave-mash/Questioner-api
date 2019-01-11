"""
This module tests the questions endpoint
Author: Dave
"""
import datetime
import unittest
import json
from app import create_app

class TestQuestions(unittest.TestCase):
    db = []
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.question = {
            "title": "Python",
            "body": "Will we talk about data science with Python?"
        }

    def post_req(self, path='api/v1/questions', data={}):
        """ This function utilizes the test client to send POST requests """
        data = data if data else self.question
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

    def test_create_question(self):
        """ Test that a user can create a question """
    
        payload = self.post_req(path='api/v1/questions/0') # this part needs refactoring
        self.assertEqual(payload.status_code, 201)
        self.assertEqual(payload.json['message'], "You have successfully posted a question")

    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.db = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()
