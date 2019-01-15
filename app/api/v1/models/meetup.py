"""
This module defines the meetup model class and all it's methods
"""

from datetime import datetime

from app.api.v1.models.base import Base

class Meetup(Base):
    """ add a meetup to the database """

    base_model = Base("meetup_db")

    # Save meetup
    def save_meetup(self, meetup_item):
        if meetup_item:
            meetup = {
                "id": meetup_item['id'],
                "createdOn": datetime.now(),
                "topic": meetup_item['topic'],
                "description": meetup_item['description'],
                "location": meetup_item['location'],
                "happeningOn": meetup_item['happeningOn'],
                "tags": meetup_item['tags']
            }
            self.base_model.save_data(meetup)
        else:
            self.errorHandler('No data found')

    # Update meetup
    def update_meetup(self, updates, meetup_id):
        try:
            if updates and meetup_id:
                self.base_model.update_data(meetup_id, updates)
        except:
            self.errorHandler('No data found')

    # Delete meetup
    def del_meetup(self, meetup_id):
        try:
            if meetup_id:
                self.base_model.delete_data(meetup_id)
        except:
            self.errorHandler('No data found')

    # RSVP meetup
    def rsvp_meetup(self, id, meetup_title):

        if meetup_title:
            user = {
                "rsvps": [meetup_title]
            }
            self.update_meetup(user, id)
        else:
            self.errorHandler('No data found')

