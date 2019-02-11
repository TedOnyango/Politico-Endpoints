
from app import createapp
import unittest
import json

from app.api.v1.models.partymodels import PARTIES

class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.client = self.app.test_client()
        self.party1 = {
            "name": "Part Theo",
            "logoUrl": ""
        }
        self.partytodelete = {
            "name": "Party 230",
            "logoUrl": ""
        }
        self.invalidparty = {
            "_id": 1
        }
    def test_view_parties(self):
        response = self.client.get("api/v1/parties")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["data"], [])
        self.assertEqual(result["status"], 200)

    def test_edit_party(self):
        res = self.client.patch("/api/v1/parties/{}/name".format(0),
                                    data=json.dumps({
                                        "name": "New Name"
                                    }), content_type="application/json")
        self.assertEqual(res.status_code, 404 )
    
    def test_delete_party(self):
        self.client.post(
                "api/v1/parties", data=json.dumps(self.partytodelete), content_type="application/json")
        res = self.client.delete(
                "/api/v1/parties/{}".format(0), content_type="application/json")
        self.assertEqual(res.status_code, 404)

    def test_create_party(self):
        res = self.client.post("api/v1/offices", data=json.dumps({
            "name": "dsd",
            "hqAdress": "The Place",
            "id": 12,
            "logoUrl": "logo/party"
        }), content_type="application/json")
        result = json.loads(res.data.decode("utf-8"))
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'Must provide id, name and type')
