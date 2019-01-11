import uuid
from app.api.v1.models.meetup_model import MeetupModel

class QuestionModel():
    """ add user a meetup to the database """

    def __init__(self):
        self.db = []

    def write_question(self, item):
        if item:
            item['id'] = len(self.db)# uuid.uuid4(),
            self.db.append(item)
        return False