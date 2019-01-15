"""Auth Views."""
import json
from flask import Response
from flask_restplus import reqparse, Resource
from werkzeug.exceptions import NotFound