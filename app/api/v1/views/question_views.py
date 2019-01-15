"""
This module defines all the question endpoints
"""
from werkzeug.exceptions import NotFound, BadRequest
from datetime import datetime
from flask import request, jsonify, make_response

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup import Meetup
from app.api.v1.models.question import Question
from app.api.v1.models.user import User

v1 = Blueprint('questionv1', __name__, url_prefix='/api/v1/')

meetup_model = Meetup('meetup_db')
question_model = Question('question_db')
user_model = User('user_db')

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
            "body": data['body'],
            "votes": 0
        }

        if question_model.save_question(question) == 'No data found':
            return make_response(jsonify({
                "error": 'No data found'
            }), 404)
        else:
            question_model.save_question(question)
    else:
        return make_response(jsonify({
            "error": "No meetup found"
        }), 404)

    return jsonify({
        "status": 201,
        "message": "You have successfully posted a question on {} meetup".format(meetup[0]['topic']),
        "data": [question],
        "question": question_model.get_items()
    }), 201

""" This route upvotes a question """
@v1.route("/questions/<int:questionId>/upvote", methods=['PATCH'])
def upvote_question(questionId):

    questions = question_model.get_items()
    question = [que for que in questions if que['id'] == questionId]

    if question_model.upvote_question(questionId) == 'Question not found or does\'nt exist':
        return make_response(jsonify({
            "error": "Question not found or does\'nt exist"
        }), 404)
    else:
        question_model.upvote_question(questionId)
        
    if question:
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "meetup": "{}".format(questionId),
                "title": question[0]['title'],
                "body": question[0]['body'],
                "votes": question[0]['votes']
            }],
            "message": "You have successfully upvoted"
        }), 200)
    else:
        return make_response(jsonify({
            "error": "question does not exist"
        }), 404)

""" This route downvotes a question """
@v1.route("/questions/<int:questionId>/downvote", methods=['PATCH'])
def downvote_question(questionId):

    questions = question_model.get_items()
    question = [que for que in questions if que['id'] == questionId]

    if question_model.downvote_question(questionId) == 'Question not found or does\'nt exist':
        return make_response(jsonify({
            "error": "Question not found or does\'nt exist"
        }), 404)
    else:
        question_model.downvote_question(questionId)
        
    if question:
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "meetup": "{}".format(questionId),
                "title": question[0]['title'],
                "body": question[0]['body'],
                "votes": question[0]['votes']
            }],
            "message": "You have successfully downvoted"
        }), 200)
    else:
        return make_response(jsonify({
            "error": "question does not exist"
        }), 404)

@v1.route("/questions/<int:questionId>/delete", methods=['DELETE'])
def delete_question(questionId):

    if question_model.del_question(questionId) == 'No data found':
        return make_response(jsonify({
            "error" "No data found"
        }), 404)
    else:
        return make_response(jsonify({
            "status": 200,
            "message": "You have deleted this question"
        }), 200)
