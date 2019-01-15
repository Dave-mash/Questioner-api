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
            "meetup_id": 0,
            "createdOn": str(datetime.now()),
            "createdBy": 1,
            "title": "Python",
            "body": "Will we talk about data science with Python?",
            "votes": 0
        }
        self.meetup = {
            "happeningOn" : "12/12/2018",
            "location" : "Nairobi",
            "tags": ["Machine learning", "Neural networks"],
            "topic": "Python data structures",
            "description": "Deep dive into python programming",
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
        self.post_req()
        question = [que for que in self.db if que['meetup_id'] == 0]
        payload = self.post_req(path='api/v1/0/questions/0', data=question[0])
        self.assertEqual(payload.status_code, 201)

        question2 = [que for que in self.db if que['meetup_id'] == 0]
        payload = self.post_req(path='api/v1/5/questions', data=question2[0])
        self.assertEqual(payload.status_code, 404)

    def test_create_question_invalid_input(self):
        """ Test that a can't post a question with invalid input """

        # Non-existing data
        question = { **self.question }
        question['title'] = ''
        payload = self.post_req(path='api/v1/0/questions/0', data=question)
        self.assertEqual(payload.status_code, 422)

        # Invalid description
        question2 = { **self.question }
        question2['body'] = ''
        payload = self.post_req(path='api/v1/0/questions/0', data=question2)
        self.assertEqual(payload.status_code, 422)
        
        # Invalid description
        question2 = { **self.question }
        question2['body'] = 'r'
        payload = self.post_req(path='api/v1/0/questions/0', data=question2)
        self.assertEqual(payload.status_code, 422)
        

    # def test_upvote_question(self):
    #     """ Test that a user can upvote a question """
    #     self.post_req(path='api/v1/meetups', data=self.meetup)
    #     self.post_req()
    #     payload = self.client.patch('/api/v1/questions/0/upvote')
    #     self.assertEqual(payload.status_code, 200)
        
    # def test_downvote_question(self):
    #     """ Test that a user can downvote a question """

    #     payload = self.client.patch('api/v1/questions/0/downvote')
    #     self.assertEqual(payload.status_code, 200)
        
    def tearDown(self):
        """ This function destroys all objects created during testing """
        self.db = []
        self.app.testing = False
        self.app = None


if __name__ == "__main__":
    unittest.main()
