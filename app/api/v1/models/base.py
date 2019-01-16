"""
This module defines the base model class and all it's methods
"""

users_db = []
meetups_db = []
questions_db = []

class Base:

    def __init__(self, db_name=''):
        self.db_name = db_name

    def check_db(self):
        try:
            if isinstance(self.db_name, str):
                if self.db_name == "user_db":
                    self.db = users_db
                elif self.db_name == "meetup_db":
                    self.db = meetups_db
                elif self.db_name == "question_db":
                    self.db = questions_db
        except ValueError:
            return 'db name must be a string'

    # Save data
    def save_data(self, item):
        self.check_db()
        self.db.append(item)

    # Get all data
    def get_items(self):
        self.check_db()
        return self.db

    # Get data by id
    def get_item_by_id(self, item_id):
        self.check_db()
        item = [item for item in self.db if item_id == item['id']]
        return item
        
    # Update data
    def update_data(self, item_id, updates):
        self.check_db()
        item = [item for item in self.db if item_id == item.id]
        item[0].update(updates)

    # Delete data
    def delete_data(self, item_id):
        self.check_db()
        item = [item for item in self.db if item_id == item.id]
        del item

    def errorHandler(self, error):
        return error
