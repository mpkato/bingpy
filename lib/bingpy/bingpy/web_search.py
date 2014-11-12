# -*- coding: utf-8 -*-
import urllib2
from lxml import etree

class BingSearchElement:
    XMLNS_D = "{http://schemas.microsoft.com/ado/2007/08/dataservices}"
    def __init__(self, id = None, title = None, summary = None, url = None, displayurl = None):
        self.id = id
        self.title = title
        self.summary = summary
        self.url = url
        self.displayurl = displayurl

    def __str__(self):
        return "%s %s" % (self.title, self.url)

    @classmethod
    def parse(cls, elem):
        result = BingSearchElement()
        for e in elem:
            if e.tag == '%sID' % cls.XMLNS_D:
                result.id = e.text
            if e.tag == '%sTitle' % cls.XMLNS_D:
                result.title = e.text
            if e.tag == '%sDescription' % cls.XMLNS_D:
                result.summary = e.text
            if e.tag == '%sUrl' % cls.XMLNS_D:
                result.url = e.text
            if e.tag == '%sDisplayUrl' % cls.XMLNS_D:
                result.displayurl = e.text
        return result


DEFAULT_APIKEY = "dHkxSgCMQ+wTm5CxIW3fFOGKdWQH312/UhqVuCI96p0="
RESULT_MAX = 50
class BingSearch:
    APIURL = "https://api.datamarket.azure.com/Bing/Search/v1/Web"
    XMLNS = "{http://www.w3.org/2005/Atom}"

    def __init__(self, apikey = DEFAULT_APIKEY):
        self.apikey = apikey

    def _auth(self):
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.APIURL, self.apikey, self.apikey)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
  
    def _make_url(self, query, skip, market):
        return self.APIURL + "?Query='%s'&Market='%s'&$skip=%s" % (urllib2.quote(query), market, skip)  
  
    def search(self, query, num = RESULT_MAX, market = 'en-US'):
        result = []
        access_num = (num - 1) / RESULT_MAX + 1
        for i in range(access_num):
            result += self._search_original(query, i * RESULT_MAX, market)
        result = result[:min(len(result), num)]
        return result

    def _search_original(self, query, skip, market):
        url = self._make_url(query, skip, market)
        self._auth()
        result = []
        try:
            f = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print e
            return result
        context = etree.iterparse(f, events=('end',))
        for event, elem in context:
            if elem.tag == '%sentry' % self.XMLNS:
                for c in elem:
                    if c.tag == '%scontent' % self.XMLNS:
                        elem = BingSearchElement.parse(c[0])
                        result.append(elem)
        return result


if __name__ == '__main__':
    bing = BingSearch()
    res = bing.search('kyoto', 100)
    print len(res)
    for elem in res:
        print "ID:", elem.id
        print "Title:", elem.title
        print "Description:", elem.summary
        print "Url:", elem.url
        print "DisplayUrl:", elem.displayurl
    print len(set([r.url for r in res]))
