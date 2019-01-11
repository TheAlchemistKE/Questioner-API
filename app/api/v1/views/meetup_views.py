"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response
from flask_restplus import reqparse, Resource


# Local Imports
from ..models.meetup_model import Meetup
from ..utils.serializer import MeetupDataTransferObject

meetup_api = MeetupDataTransferObject.meetup_namespace

parser = reqparse.RequestParser()
# Meetup Arguments
parser.add_argument("location", type=str ,required=True, help="Please enter meetup location.")
parser.add_argument("image1", required=True, help="Please enter meetup image.")
parser.add_argument("image2", help="Please enter meetup image.")
parser.add_argument("image3", help="Please enter meetup image.")
parser.add_argument("topic", type=str ,required=True, help="Please enter meetup topic.")
parser.add_argument("happening_on", type=str ,required=True, help="Please enter meetup date.")
parser.add_argument("tag1", required=True, help="Please enter meetup tag.")
parser.add_argument("tag2", required=True, help="Please enter meetup tag.")
parser.add_argument("tag3", required=True, help="Please enter meetup tag.")

meetup_request_model = MeetupDataTransferObject.meetup_request_model

@meetup_api.route('', '/upcoming')
class MeetupList(Resource):
    """Meetup endpoint."""
    @meetup_api.expect(meetup_request_model, validate=True)
    def post(self):
        """Performing a POST request."""
        request_data = parser.parse_args()
        location = request_data["location"]
        image1 = request_data["image1"]
        image2 = request_data["image2"]
        image3 = request_data["image3"]
        topic = request_data["topic"]
        happening_on = request_data["happening_on"]
        tag1 = request_data["tag1"]
        tag2 = request_data["tag2"]
        tag3 = request_data["tag3"]

        images = [image1, image2, image3]
        tags = [tag1, tag2, tag3]

        new_meetup = Meetup(location, images, topic, happening_on, tags)
        create_meetup = new_meetup.create_new_meetup()
        response_payload = dict(
            status=201,
            message="Meetup was created successfully.",
            data=create_meetup
        )
        response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
        return response


    def get(self):
        """Fetching All Meetups"""
        meetups = Meetup.fetch_all_meetups(self)
        response_payload = {
            "status": 200,
            "data": meetups
        }
        response = Response(json.dumps(response_payload), status=200, mimetype="application/json")
        return response

@meetup_api.route('/<int:meetup_id>')
class SingleMeetup(Resource):
    """Deals with operations on single meetup record."""
    def get(self, meetup_id):
        """Getting a specific meetup"""
        meetup = Meetup.fetch_single_meetup(meetup_id)
        response_payload = {
            "status": 200,
            "data": meetup
        }
        response = Response(json.dumps(response_payload), status=200, mimetype="application/json")
        return response

