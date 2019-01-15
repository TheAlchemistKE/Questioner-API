"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response
from flask_restplus import reqparse, Resource
from werkzeug.exceptions import NotFound, BadRequest


# Local Imports
from ..models.rsvp_model import RsvpModel
from ..utils.serializer import RsvpDataTransferObject
from ..utils.validator import Validator

rsvp_api = RsvpDataTransferObject.rsvp_namespace

parser = reqparse.RequestParser()
# Meetup Arguments
parser.add_argument("meetup", type=int ,required=True, help="Please enter meetup location.")
parser.add_argument("user", type=int ,required=True, help="Please enter meetup image.")
parser.add_argument("response", type=str, help="Please enter meetup image.")

rsvp_request_model = RsvpDataTransferObject.rsvp_request_model

@rsvp_api.route('')
class Rsvp(Resource):
    @rsvp_api.expect(rsvp_request_model, validate=True)
    def post(self, meetup_id):
        """Creating an RSVP to an event."""
        request_data = parser.parse_args()
        user_id = request_data["user"]
        meetup_id = request_data["meetup"]
        response = request_data["response"]

        find_user = RsvpModel.find_by_id(self, db="users", id=user_id)
        find_meetup = RsvpModel.find_by_id(self, db="meetups", id=meetup_id)
        if find_user == "Record doesn't exist." and find_meetup =="Record doesn't exist.":
            error_response = dict(
                status=404,
                error="User/Meetup does not exist.",
                message="Enter a valid user id."
            )
            error = NotFound()
            error.data = error_response
            return error
        else:
            username = find_user[0]["username"]
            meetup_name = find_meetup[0]["topic"]
            
            rsvp_payload = dict(
                user=user_id,
                username=username,
                meetup=meetup_id,
                meetup_name=meetup_name,
                response=response  
            )
            check_payload = Validator.check_input_for_null_entry(data=rsvp_payload)
            if check_payload:
                rsvp = RsvpModel.create_rsvp(self, data=rsvp_payload)
                response_payload = dict(
                    status=201,
                    data=rsvp
                )
                response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
                return response
            error_payload = dict(
                status=400,
                error="Null fields.",
                message="Fields cannot be empty or spaces."
            )
            error_resp = Response(json.dumps(error_payload), status=400, mimetype="application/json")
            return error_resp
        


