# -*- coding: utf-8 -*-

class WebSearchElement:
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
        id = elem["id"]
        title = elem["name"]
        summary = elem['snippet']
        displayurl = elem["displayUrl"]
        url = elem["url"]
        result = WebSearchElement(id, title, summary, url, displayurl)
        return result
