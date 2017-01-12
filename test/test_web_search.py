import bingpy
import os

class TestWebSearch(object):

    def test_search(self):
        query = "ABC"
        apikey = os.environ["BING_API_KEY_V5"]
        ws = bingpy.WebSearch(apikey)
        res = ws.search(query, 10)
        assert len(res) == 10
        res = ws.search(query, 51)
        assert len(res) == 51
