class MeetupModel():
    """ add user a meetup to the database """

    def __init__(self, logged=False):
        self.logged = logged,
        self.dup_email = None,
        self.dup_username = None,
        self.db = []

    def write_meetup(self, item):
        if item:
            # user = [user for user in user_model.db if user['email'] == item['email']]
            # if user and user.logged:
            self.db.append(item)
            return self.db
            # else:
                # return {"Error": "You are not logged in"}