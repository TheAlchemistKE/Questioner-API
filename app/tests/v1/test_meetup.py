"""Module for Testing the Meetup Endpoint."""
import json

# Local Import
from .basecase import TestBaseCase as base

class TestMeetup(base):
    """Testing the Meetup Endpoints with valid input."""
    def setUp(self):
        base.setUp(self)

    def test_create_meetup(self):
        """Testing Creation of a Meetup."""
            
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "Meetup was created successfully.")

    def test_fetching_all_meetups(self):
        """Testing Fetching of all meetups."""
