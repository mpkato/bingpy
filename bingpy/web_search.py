# -*- coding: utf-8 -*-
import requests
from .web_search_element import WebSearchElement

class WebSearch:
    APIURL = "https://api.cognitive.microsoft.com/bing/v5.0/search"
    RESULT_MAX = 50

    def __init__(self, apikey):
        self.apikey = apikey

    def search(self, query, num, market = 'en-US', safesearch='Off'):
        # retrieve 'num' Web search results by 'query' from 'market'
        access_num = (num - 1) // self.RESULT_MAX + 1
        result = []
        for i in range(access_num):
            # get RESULT_MAX search results
            result += self._search_original(query, self.RESULT_MAX,
                i*self.RESULT_MAX, market, safesearch)
        # truncate (redundant...)
        result = result[:min(len(result), num)]
        return result

    def _search_original(self, query, num, skip, market, safesearch):
        url = self._make_url(query, num, skip, market, safesearch)
        headers = {"Ocp-Apim-Subscription-Key": self.apikey}
        res = requests.get(url, headers=headers)
        result = self._parse_response(res)
        return result

    def _make_url(self, query, num, skip, market, safesearch):
        return (self.APIURL + "?q=%s&count=%s&offset=%s&mkt=%s&safesearch=%s"
            % (query, num, skip, market, safesearch))

    def _parse_response(self, res):
        result = []
        data = res.json()
        if "webPages" in data and "value" in data["webPages"]:
            for page in data["webPages"]["value"]:
                elem = WebSearchElement.parse(page)
                result.append(elem)
        return result
