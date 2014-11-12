# -*- coding: utf-8 -*-
import urllib2
from lxml import etree

from web_search_element import WebSearchElement

class WebSearch:
    APIURL = "https://api.datamarket.azure.com/Bing/Search/v1/Web"
    XMLNS = "{http://www.w3.org/2005/Atom}"
    RESULT_MAX = 50

    def __init__(self, apikey):
        self.apikey = apikey

    def search(self, query, num, market = 'en-US'):
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
        self._basic_auth()
        f = urllib2.urlopen(url)
        try:
            result = self._parse_response(f)
        except Exception, e:
            raise e
        finally:
            f.close()
        return result

    def _make_url(self, query, skip, market):
        return self.APIURL + "?Query='%s'&Market='%s'&$skip=%s" % (urllib2.quote(query), market, skip)

    def _basic_auth(self):
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.APIURL, self.apikey, self.apikey)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

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
