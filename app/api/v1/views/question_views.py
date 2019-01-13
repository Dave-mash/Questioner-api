"""
This module defines all the question endpoints
"""
from werkzeug.exceptions import NotFound, BadRequest
from datetime import datetime
from flask import request, jsonify, make_response

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel
from app.api.v1.models.question_model import QuestionModel
from app.api.v1.models.user_model import UserModel

v1 = Blueprint('questionv1', __name__, url_prefix='/api/v1/')

meetup_model = MeetupModel('meetup_db')
question_model = QuestionModel('question_db')
user_model = QuestionModel('user_db')

""" This route creates a question """
@v1.route("/<int:meetupId>/questions/", methods=['POST'])
def create_question(meetupId):
    data = request.get_json()
    meetups = meetup_model.get_items()
    meetup = [meetup for meetup in meetups if meetup['id'] == meetupId]

    if meetup:
        question = {
            "id": len(meetups),
            "meetup_id": meetupId,
            "createdOn": datetime.now(),
            "createdBy": data['createdBy'], # user_id
            "title": data['title'],
            "body": data['body']
        }

        question_model.save_question(question)
        return jsonify({
            "status": 201,
            "message": "You have successfully posted a question on {} meetup".format(meetup[0]['topic']),
            "data": [question]
        }), 201
    elif not meetup:
        raise NotFound('No meetup found or does\'nt exist!')

# @v1.route("/questions/<int:questionId>/upvote", methods=['PATCH'])
# def upvote_question(questionId):
#     data = request.get_json()

#     vote = {
#         "vote": data['vote']
#     }

#     return jsonify({
#         "status": 200,
#         "meetup": "{}".format(questionId),
#         "vote": data['vote']
#     }), 200

# @v1.route("/questions/<int:questionId>/downvote", methods=['PATCH'])
# def downvote_question(questionId):
#     data = request.get_json()

#     vote = {
#         "vote": data['vote']
#     }

#     return jsonify({
#         "status": 200,
#         "meetup": "{}".format(questionId),
#         "vote": data['vote']
#     }), 200