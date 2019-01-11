"""
    Meetup Models
    Author: Kelyn Paul Njeri.
"""
from datetime import datetime
import json


class Meetup:
    """Models for meetup views."""

    meetups = []

    def __init__(self, location, images, topic, happening_on, tags):
        """Meetup class constructor."""
        self.meetup_id = len(Meetup.meetups) + 1
        self.created_on = str(datetime.now())
        self.location = location
        self.images = images
        self.topic = topic
        self.happening_on = happening_on
        self.tags = tags

    def create_new_meetup(self):
        """Creating new meetup."""
        new_meetup = dict(
            id=self.meetup_id,
            createdOn=self.created_on,
            location=self.location,
            images=self.images,
            topic=self.topic,
            happeningOn=self.happening_on,
            Tags=self.tags,
        )
        self.meetups.append(new_meetup)
        return new_meetup

    def fetch_all_meetups(self):
        """Fetching all Meetup Records."""
        return Meetup.meetups

    @staticmethod
    def fetch_single_meetup(meetup_id):
        """Fetching a specific meetup."""
        meetups = Meetup.meetups
        single_meetup = [meetup for meetup in meetups if meetup["id"] == meetup_id]
        if single_meetup:
            return single_meetup
        else:
            return "Meetup does not exist. Please create one."

    @staticmethod
    def create_an_rsvp(user_id, meetup_id, response):
        rsvps = []
        new_rsvp = dict(
            id=len(rsvps) + 1,
            user=user_id,
            meetup=meetup_id,
            status=response
        )
        rsvps.append(new_rsvp)
        return new_rsvp

