import json

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.encoding import smart_str

MEM_FIELDS = [
    'utime',
    'stime',
    'maxrss',
    'ixrss',
    'idrss',
    'isrss',
    'minflt',
    'majflt',
    'nswap',
    'inblock',
    'oublock',
    'msgsnd',
    'msgrcv',
    'nsignals',
    'nvcsw',
    'nivcsw',
]


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


class MemoryTest(TestCase):
    def test_memory(self):
        r = self.client.get(reverse('expvar'))
        d = json.loads(smart_str(r.content))
        self.assertIn('memory', d)
        m = d['memory']
        for f in MEM_FIELDS:
            self.assertIn(f, m)


class FindTest(TestCase):
    """ make sure it finds testapp.main.expvar.* """
    def test_main_expvar(self):
        r = self.client.get(reverse('expvar'))
        d = json.loads(smart_str(r.content))
        self.assertIn('example1', d)
        self.assertEqual(d['example1'], 42)


class ExtendTest(TestCase):
    def test_memory(self):
        r = self.client.get(reverse('expvar'))
        d = json.loads(smart_str(r.content))
        self.assertIn('memory', d)
        m = d['memory']
        self.assertIn('New', m)
        self.assertEqual(m['New'], 78)
