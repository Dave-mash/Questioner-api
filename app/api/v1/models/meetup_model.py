"""
This module defines the meetup model class and all it's methods
"""

from werkzeug.exceptions import NotFound
from datetime import datetime

from app.api.v1.models.base_model import BaseModel

class MeetupModel(BaseModel):
    """ add a meetup to the database """

    base_model = BaseModel("meetup_db")

    # Save meetup
    def save_meetup(self, meetup_item):
        try:
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
        except:
            raise NotFound('No data found')

    # # Edit meetup
    # def edit_meetup(self, updates, meetup_id):
    #     try:
    #         if updates and meetup_id:
    #             self.base_model.update_data(meetup_id, updates)
    #     except:
    #         raise NotFound('No data found')

    # # Delete meetup
    # def del_meetup(self, meetup_id):
    #     try:
    #         if meetup_id:
    #             self.base_model.delete_data(meetup_id)
    #     except:
    #         raise NotFound('No data found')

    # RSVP meetup
    def rsvp_meetup(self, rsvp_item):

        if rsvp_item:
            pass
        else:
            raise NotFound('No data found')
