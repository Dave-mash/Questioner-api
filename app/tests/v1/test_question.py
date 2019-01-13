"""
This module tests the questions endpoint
Author: Dave
"""
import datetime
import unittest
import json
from app import create_app
from datetime import datetime

class TestQuestions(unittest.TestCase):
    db = []
    
    def setUp(self):
        """ Initializes app """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.question = {
            "id": len(self.db),
            "meetup_id": 1,
            "createdOn": str(datetime.now()),
            "createdBy": 1,
            "title": "Python",
            "body": "Will we talk about data science with Python?",
            "votes": 0
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
        self.db = []
        payload = self.post_req(path='api/v1/0/questions') # this part needs refactoring
        if self.db:
            self.assertEqual(payload.status_code, 201)
        else:
            self.assertTrue(self.db, False)
            self.assertEqual(payload.status_code, 404)
        # self.assertEqual(payload.json['message'], "You have successfully posted a question")

    # def test_upvote_question(self):
    #     """ Test that a user can upvote a question """
    #     upvote = {
    #         # "meetup": 1,
    #         # "title": "Django",
    #         # "body": "Introduction to Django",
    #         "votes": 2
    #     }

    #     payload = self.post_req(path='api/v1/questions/1/upvote', data=upvote)
    #     self.assertEqual(payload.status_code, 200)
    #     # self.assertEqual(payload.json['message'], "You have upvoted this question")
        
    # def test_downvote_question(self):
    #     """ Test that a user can downvote a question """
    #     downvote = {
    #         # "meetup": 1,
    #         # "title": "Flask",
    #         # "body": "Introduction to Flask",
    #         "votes": -2
    #     }

    #     payload = self.post_req(path='api/v1/questions/1/downvote', data=downvote)
    #     self.assertEqual(payload.status_code, 200)
    #     # self.assertEqual(payload.json['message'], "You have downvoted this question")

    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.db = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()
