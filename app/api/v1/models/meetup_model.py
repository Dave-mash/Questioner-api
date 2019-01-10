class MeetupModel():
    """ add user a meetup to the database """

    def __init__(self, logged=False):
        self.logged = logged,
        self.dup_email = None,
        self.dup_username = None,
        self.db = []

    def write_meetup(self, item):
        if item:
            dup_topic = [topic for topic in self.db if topic['topic'] == item['topic']]
            if not dup_topic:
                self.db.append(item)
            return False