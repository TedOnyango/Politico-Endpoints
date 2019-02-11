from app import createapp
import unittest
import json

from app.api.v1.models.officemodels import OFFICES



class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.client = self.app.test_client()
        self.office1 = {
            "type": "Member of Paliament",
            "name": "MP Nairobi"
        }
        self.erroroffice = {
        }
    # tear down test

    def tearDown(self):
        """Final cleanup after tests run"""
        self.app.testing = False

class TestOfficesEndPoints(RoutesBaseTest):

    def test_view_all_offices(self):
        response = self.client.get("api/v1/offices")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["data"], [{
            "name": "dsd",
            "type": "trtr",
            "id": 23
        }])
        self.assertEqual(result["status"], 200)

    def test_view_specific_undefined_office(self):
        response = self.client.get("api/v1/offices/12")
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result["status"], 404)

    def test_create_office(self):
        res = self.client.post("api/v1/offices", data=json.dumps({
            "name": "dsd",
            "type": "trtr",
            "id": 23
        }), content_type="application/json")
        result = json.loads(res.data.decode("utf-8"))
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{'id': 23, 'name': 'dsd', 'type': 'trtr'}])



    def test_create_office_with_bad_request(self):
        res = self.client.post("api/v1/offices", data=json.dumps({
            "name": "dsd",
            "type": "trtr"
        }), content_type="application/json")
        result = json.loads(res.data.decode("utf-8"))
        self.assertEqual(result["status"], 400)
        self.assertEqual(result['error'], 'Must provide id, name and type')
    
    def test_edit_office_not_found(self):
        response = self.client.get("api/v1/offices")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"], [{'id': 23, 'name': 'dsd', 'type': 'trtr'}])

    
