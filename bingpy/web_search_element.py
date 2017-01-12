# -*- coding: utf-8 -*-

class WebSearchElement:
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
        result = WebSearchElement()
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
