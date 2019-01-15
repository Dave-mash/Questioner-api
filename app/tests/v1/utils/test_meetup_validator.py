"""
This module tests the meetup_validator endpoint
"""

import unittest
from app.api.v1.utils.question_validators import MeetupValidator

class TestQuestionsValidator(unittest.TestCase):

    def setUp(self):
        """ Initializes app """
        self.meetup = {
            "topic": "a meetup",
            "description": "this is a meetup",
            "tags": ['Django', 'Flask'],
            "happeningOn": "12-12-2019",
            "location": "Nairobi"
        }

    def test_meetup_data_exists(self):
        question = MeetupValidator('', '')
        self.assertEqual(question.data_exists(), 'You missed a required field')  

    def test_invalid_data(self):
        question = MeetupValidator('b', 'This is python')
        self.assertEqual(question.valid_topic(), 'Your topic is too short!')
        question = MeetupValidator('This is a long line of text testing whether this field should be less than 30 characters', 'This is python')
        self.assertEqual(question.valid_topic(), 'Your topic is too long!')

        question = MeetupValidator('Python', 'T')
        self.assertEqual(question.valid_description(), 'Your description is too short')

        question = MeetupValidator('Python', 'This is a meetup')
        self.assertEqual(question.valid_tags(), 'Have at least one tag')

        question = MeetupValidator('Python', 'This is a meetup', ['Django', 'Flask'], '12/12/2019')
        self.assertEqual(question.valid_date(), 'Date format should be YYYY-MM-DD')

        question = MeetupValidator('Python', 'This is a meetup', ['Django', 'Flask'], '12-12-2019', 'N')
        self.assertEqual(question.valid_location(), 'Enter a valid location!')
