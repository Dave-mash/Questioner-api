import uuid

class MeetupModel():
    """ add user a meetup to the database """

    def __init__(self, logged=False):
        self.logged = logged
        self.db = []

    def write_meetup(self, item):
        if item:
            dup_topic = [topic for topic in self.db if topic['topic'] == item['topic']]
            if not dup_topic:
                item['id'] = len(self.db)# uuid.uuid4(),
                self.db.append(item)
                return item['id']
            return False