"""
This module defines all the question endpoints
"""
import datetime
from flask import request, jsonify, make_response

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel
from app.api.v1.models.question_model import QuestionModel
from app.api.v1.models.user_model import UserModel

v1 = Blueprint('questionv1', __name__, url_prefix='/api/v1/')

# meetup_model = MeetupModel()
# question_model = QuestionModel()
# user_model = QuestionModel()

# """ This route creates a question """
# @v1.route("/questions/<int:questionId>", methods=['POST'])
# def create_question(questionId):
#     data = request.get_json()
    # meetups = meetup_model.get_items()
#     meetup_item = {
#         "title": data['title'],
#         "body": data['body'],
        # "id": len(meetups), # str(uuid.uuid4()),
#     }

#     # if question_model.write_question(meetup_item):
#     return jsonify({
#         "status": 201,
#         "message": "You have successfully posted a question",
#         "data": [{ **meetup_item }]
#     }), 201
#     # else:
#     #     return jsonify({
#     #         "status": 404,
#     #         "Error": "Meetup not found"
#     #     }), 404

#     # demo = {
#     #     "createdOn": "{}".format(datetime.datetime.now()),
#     #     "createdBy": 1,
#         # "meetup": 1,
#         # "title": "Python",
#         # "body": "Will we talk about data science with Python?",
#         # "votes": 2
#     # }

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