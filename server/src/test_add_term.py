from server import app
from flask import url_for
import unittest
import json


class FlaskTodosTest(unittest.TestCase):
    def setUp(self):
        """Set up test application client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_missing_both_params(self):
        """Assert that requests missing both params say it's missing params"""

        response = self.app.post('/terms/new',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp_data_as_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(resp_data_as_json["message"],
                        "missing parameters: term, year")

    #def test_missing_



if __name__ == '__main__':
    unittest.main()