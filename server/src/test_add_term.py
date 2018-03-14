from flask import url_for
from server import app

import unittest
import json

class FlaskTodosTest(unittest.TestCase):
    def setUp(self):
        """Set up test application client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_missing_both_params(self):
        """Assert that requests missing both params response says
         request is missing both params"""

        response = self.app.post('/terms/new',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp_data_as_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(resp_data_as_json["message"],
                        "missing parameters: term, year")

    def test_missing_term_param(self):
        """Assert that requests missing just the term param
        response says request is missing term param"""

        response = self.app.post('/terms/new',
                                 data=json.dumps({"year":"2015"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp_data_as_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(resp_data_as_json["message"],
                         "missing parameter: term")

    def test_missing_year_param(self):
        """Assert that requests missing just the year param
        response says request is missing year param"""

        response = self.app.post('/terms/new',
                                 data=json.dumps({"term": "Fall"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp_data_as_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(resp_data_as_json["message"],
                         "missing parameter: year")

    def test_non_numeric_year_param(self):
        """Assert that requests having the year param be non numeric
        response says request has non-numeric year param"""

        response = self.app.post('/terms/new',
                                 data=json.dumps({"year": "s",
                                                  "term": "s"
                                                  }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        resp_data_as_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(resp_data_as_json["message"],
                         "must be integer: year")




if __name__ == '__main__':
    unittest.main()
