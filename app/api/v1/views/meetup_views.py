"""
This module defines all the user endpoints
"""

import uuid
import datetime
from flask import request, jsonify, make_response

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel

v1 = Blueprint('meetupv1', __name__, url_prefix='/api/v1/')

meetup_model = MeetupModel()

""" This route performs a get request to fetch all meetups """
@v1.route("/meetups/", methods=['GET'])
def get_all_meetups():
    return make_response(jsonify({
        "meetups": meetup_model.db
    }), 200)

""" This route posts a meetup """
@v1.route("/meetups/", methods=['POST'])
def post_a_meetup():
    data = request.get_json()
    # datetime.datetime.now()
    meetup = {
        "title": data['title'],
        "body": data['body'],
        "location": data['location'],
        "happeningOn": data['happeningOn'],
        "tags": data['tags']
    }
    meetup_model.write_meetup(meetup)
    return jsonify({
        "status": 201,
        "message": "You have successfully posted a meetup",
        "data": [{
            "title": data['title'],
            "location": data['location'],
            "happeningOn": data['happeningOn'],
            "tags": data['tags']
        }]
    }), 201

""" This route fetches a specific meetup """
@v1.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    meetup = [meetup for meetup in meetup_model.db if meetup['id'] == meetupId]

    if meetup:
        return jsonify({
            "status": 200,
            "data": [meetup[0]]
        }), 200

""" This route posts RSVPS on meetups """
@v1.route("/meetups/<int:meetupId>/rsvp", methods=['POST'])
def post_RSVP(meetupId):
    data = request.get_json()

    return jsonify({
        "status": 201,
        "title": data['title'],
        "meetup": "{}".format(meetupId),
        "message": "You have successfully posted an RSVP"
    }), 201

# @v1.route("/questions/<int:questionId>/upvote", methods=['PATCH'])
# def upvote_question(questionId):
#     data = request.get_json()

#     return jsonify({
#         "status": 201,
#         "message": "You have upvoted this question",
#         "data": [{
#             "meetup": "{}".format(questionId),
#             # "title": data['title'],
#             # "body": data['body'],
#             "votes": "{}".format(data['votes'])
#         }]
#     }), 201

# @v1.route("/questions/<int:questionId>/downvote", methods=['PATCH'])
# def downvote_question(questionId):
#     data = request.get_json()

#     return jsonify({
#         "status": 201,
#         "message": "You have downvoted this question",
#         "data": [{
#             "meetup": "{}".format(questionId),
#             # "title": data['title'],
#             # "body": data['body'],
#             "votes": "{}".format(data['votes'])
#         }]
#     }), 201