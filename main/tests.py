import json

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.encoding import smart_str


class BasicTest(TestCase):
    def test_returns_json(self):
        r = self.client.get(reverse('expvar'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r['Content-Type'], 'application/json')
        json.loads(smart_str(r.content))


class CmdlineTest(TestCase):
    def test_cmdline(self):
        r = self.client.get(reverse('expvar'))
        d = json.loads(smart_str(r.content))
        self.assertIn('cmdline', d)
