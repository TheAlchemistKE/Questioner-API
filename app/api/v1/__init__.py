"""Version 1 API module."""

# Third party imports
from flask_restplus import Api
from flask import Blueprint

# Local Imports
from .views.meetup_views import meetup_api
from .views.question_views import question_api
from .views.rsvp_views import rsvp_api

version1 = Blueprint('Questioner version 1', __name__, url_prefix="/api/v1")

api = Api(version1, version="1.0", title="Questioner REST API",
          description="This is backend of the Questioner Web app.", doc="/documentation")

api.add_namespace(meetup_api, path="/meetups")
api.add_namespace(question_api, path="/questions")
api.add_namespace(rsvp_api, path="/meetups/<int:meetup_id>/rsvps")
