"""
This module defines the question model class and all it's methods
"""

from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
import uuid

from app.api.v1.models.meetup_model import MeetupModel
from app.api.v1.models.base_model import BaseModel

class QuestionModel(MeetupModel):
    """ add a question to the database """

    base_model = BaseModel("question_db")

    # Save data
    def save_question(self, question_item):
        if question_item:
            question = {
                "id": question_item['id'],
                "meetup": question_item['meetup_id'],
                "createdBy": question_item['createdBy'],
                "title": question_item['title'],
                "body": question_item['body'],
                "votes": question_item['votes']
            }
            self.base_model.save_data(question)
        else:
            raise BadRequest('No data found')

    # Edit data
    def edit_question(self, updates, question_id):
        try:
            if updates and question_id:
                self.base_model.update_data(question_id, updates)
        except:
            raise BadRequest('No data found')

    # Delete data
    def del_question(self, question_id):
        try:
            if question_id:
                self.base_model.delete_data(question_id)
        except:
            raise BadRequest('No data found')

    # upvote question
    def upvote_question(self, questionId):
        questions = self.base_model.get_items()
        question = [que for que in questions if que['id'] == questionId]

        if question:
            question[0]['votes'] += 1
        else:
            raise NotFound('Question not found or does\'nt exist')

    # downvote question
    def downvote_question(self, questionId):
        questions = self.base_model.get_items()
        question = [que for que in questions if que['id'] == questionId]

        if question:
            question[0]['votes'] -= 1
        else:
            raise NotFound('Question not found or does\'nt exist')

