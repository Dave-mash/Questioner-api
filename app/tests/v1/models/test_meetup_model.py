"""
This module contains tests for the base model
"""

import unittest
import json
from datetime import datetime
from app.api.v1.models.meetup import Meetup

class TestMeetups(unittest.TestCase):
    db = []
    
    def setUp(self):
        """ Initializes app """
        self.base_model = Meetup("meetup_db")
        self.meetup = {
            "id": len(self.db),
            "createdOn": self.base_model.now,
            "topic": "Python data structures",
            "description": "Deep dive into python",
            "location" : "Nairobi",
            "happeningOn" : "12-12-2018",
            "tags": ["Machine learning", "Neural networks"],
        }

    def test_save_meetup(self):
        self.base_model.save_meetup(self.meetup)
        meetup = self.base_model.get_item_by_id(self.meetup['id'])
        self.assertEqual(meetup, [self.meetup])

    def test_delete_meetup(self):
        meetup = { **self.meetup }



