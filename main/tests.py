from django.test import TestCase
from django.utils.encoding import smart_str
import json


class BasicTest(TestCase):
    def test_returns_json(self):
        r = self.client.get("/debug/vars")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r['Content-Type'], 'application/json')
        json.loads(smart_str(r.content))
