"""
    Validation Module
    Author: Kelyn Paul Njeri
"""
from flask_restplus import Namespace, fields


class MeetupDataTransferObject:
    """Meetup Validators."""
    meetup_namespace = Namespace(
        "Meetup Endpoint",
        description="Responsible for creating, fetching, editing and deleting meetups."
    )

    meetup_request_model = meetup_namespace.model("Meetup Request Model", {
        "location": fields.String(description="The meetup location."),
        "images": fields.String(description="The URLs to the images of the meetup."),
        "topic": fields.String(description="The name of the meetup."),
        "happeningOn": fields.Date(description="The date when the event will take place."),
        "Tags": fields.String(description="The meetup category.")

    })

class QuestionDataTransferObject:
    """Question Validators."""
    question_namespace = Namespace(
        "Question Endpoint",
        description="Responsible for creating, fetching, editing and deleting questions."
    )
    question_request_model = question_namespace.model("Question Request Model", {
        "user": fields.Integer(description="The user's id."),
        "meetup": fields.Integer(description="The meetup's ID."),
        "title": fields.String(description="The question's title."),
        "body": fields.String(description="The question's description.")

    })

