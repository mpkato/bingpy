import unittest
import nose
import os
import sys
sys.path.append(os.path.dirname(__file__) + '/../lib/bingpy3/bingpy3/')
from web_search import WebSearch

class WebSearchTestCase(unittest.TestCase):
    def setUp(self):
        # Please execute `echo "APIKEY = 'YOUR_API_KEY'" > test/apikey.py`
        # before conducting this test
        from apikey import APIKEY
        self.web = WebSearch(APIKEY)

    def test_10_search(self):
        res = self.web.search("test", 10)
        self.assertEqual(10, len(res))
        for r in res:
            self.assertGreaterEqual(len(r.title), 0)
            self.assertGreaterEqual(len(r.url), 0)
            self.assertTrue(r.url.startswith("http"))

    def test_60_search(self):
        res = self.web.search("test", 60)
        self.assertEqual(60, len(res))
        for r in res:
            self.assertGreaterEqual(len(r.title), 0)
            self.assertGreaterEqual(len(r.url), 0)
            self.assertTrue(r.url.startswith("http"))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
