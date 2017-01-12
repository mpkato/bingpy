# -*- coding: utf-8 -*-
import requests
from lxml import etree

from web_search_element import WebSearchElement

class WebSearch:
    APIURL = "https://api.cognitive.microsoft.com/bing/v5.0/search"
    RESULT_MAX = 50

    def __init__(self, apikey):
        self.apikey = apikey

    def search(self, query, num, market = 'en-US', safesearch='Off'):
        # retrieve 'num' Web search results by 'query' from 'market'
        # compute the number of Web accesses
        access_num = (num - 1) / self.RESULT_MAX + 1
        result = []
        for i in range(access_num):
            # get RESULT_MAX search results
            result += self._search_original(query, i * self.RESULT_MAX, market)
        # truncate (redundant...)
        result = result[:min(len(result), num)]
        return result

    def _search_original(self, query, skip, market):
        url = self._make_url(query, skip, market)
        header = {"Ocp-Apim-Subscription-Key": self.apikey}
        self._basic_auth()
        f = urllib2.urlopen(url)
        try:
            result = self._parse_response(f)
        except Exception as e:
            raise e
        finally:
            f.close()
        return result

    def _make_url(self, query, num, skip, market, safesearch):
        return (self.APIURL + "?q=%s&count=%s&offset=%s&mkt=%s&safesearch=%s"
            % (urllib2.quote(query), num, skip, market, safesearch))

    def _parse_response(self, f):
        result = []
        context = etree.iterparse(f, events=('end',))
        for event, elem in context:
            if elem.tag == '%sentry' % self.XMLNS:
                for c in elem:
                    if c.tag == '%scontent' % self.XMLNS:
                        elem = WebSearchElement.parse(c[0])
                        result.append(elem)
        return result

if __name__ == '__main__':
    import os
    ws = WebSearch(os.environ["BING_API_KEY_V5"])
    ws.search("hoge", 100)
