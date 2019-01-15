"""
    User Models
    Author: Kelyn Paul Njeri.
"""

from .base_model import BaseModel


class AuthModel(BaseModel):
    """Models for meetup views."""

    def find_user_by_username(self, db, username):
        data_store = BaseModel.check_db(db)
        existing_user = [
            user for user in data_store if user["username"] == username]
        if existing_user:
            return "User already exists"

    def fetch_all_meetups(self):
        """Fetching all Meetup Records."""
        return BaseModel.retrieve_data(self, db="users")

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
