"""Version 1 API module."""

# Third party imports
from flask_restplus import Api
from flask import Blueprint

# Local Imports
from .views.meetup_views import meetup_api

version1 = Blueprint('Questioner version 1', __name__, url_prefix="/api/v1")

api = Api(version1, version="1.0", title="Questioner REST API", description="This is backend of the Questioner Web app.")

api.add_namespace(meetup_api, path="/meetups")
