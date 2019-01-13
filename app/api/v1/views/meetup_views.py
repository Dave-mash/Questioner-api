"""
This module defines all the user endpoints
"""

import uuid
import datetime
from flask import request, jsonify, make_response
from werkzeug.exceptions import NotFound

# local imports
from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.meetup_model import MeetupModel

v1 = Blueprint('meetupv1', __name__, url_prefix='/api/v1/')

meetup_model = MeetupModel('meetup_db')

""" This route performs a get request to fetch all meetups """
@v1.route("/meetups/", methods=['GET'])
def get_all_meetups():
    meetups = meetup_model.get_items()

    return make_response(jsonify({
        "meetups": meetups
    }), 200)

""" This route posts a meetup """
@v1.route("/meetups/", methods=['POST'])
def post_a_meetup():
    data = request.get_json()
    meetups = meetup_model.get_items()

    meetup = {
        "topic": data['topic'],
        "description": data['description'],
        "location": data['location'],
        "happeningOn": data['happeningOn'],
        "tags": data['tags'],
        "id": len(meetups), # str(uuid.uuid4()),
    }

    meetup_model.save_data(meetup)

    return jsonify({
        "status": 201,
        "message": "You have successfully posted a meetup",
        "data": [{
            "topic": data['topic'],
            "location": data['location'],
            "happeningOn": data['happeningOn'],
            "tags": data['tags']
        }],
        "meetups": meetups
    }), 201

""" This route fetches a specific meetup """
@v1.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    meetup = meetup_model.get_item_by_id(meetupId)

    if meetup:
        return jsonify({
            "status": 200,
            "data": meetup
        }), 200
    else:
        raise NotFound('Meetup not found!')

# """ This route posts RSVPS on meetups """
# @v1.route("/meetups/<int:meetupId>/rsvp", methods=['POST'])
# def post_RSVP(meetupId):
#     data = request.get_json()

#     rsvp = {
#         "id": meetupId,
#         "topic": data['topic'],
#         "status": data['status']
#     }

#     return jsonify({
#         "status": 201,
#         "data": rsvp
#     }), 201

# """ This route upvotes a question """
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

# """ This route downvotes a question """
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