"""Base Case for all tests."""
import unittest

# Local Import
from ... import create_app


class TestBaseCase(unittest.TestCase):
    """Base Testing Class."""
    def setUp(self):
        self.client = create_app(config_name="testing").test_client()
        self.content_type = "application/json"
        self.meetup_payload = {
            "location" : "Nairobi, Kenya",
            "images" : ["http://www.techsoupeurope.org/wp-content/uploads/2018/07/TheHeorsOfTech-1024x576.png", "https://d1.awsstatic.com/Developer%20Marketing/Events/AWS-Minorities-In-Tech-Site-Banner.77f8c4afbcb5a20525278c95764f1590e4252329.png"],
            "topic" : "Growing in Tech",
            "happeningOn" : "31/01/2019",
            "tags" : ["tech", "growth"]
        }

    def tearDown(self):
        self.client = None
        self.content_type = None
        self.meetup_payload = None
