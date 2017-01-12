bingpy
======

Python Bing Search API (2017)

Designed for Python 3
and Bing Web Search API in Cognitive Services (version 5).

Install
------
```bash
pip install git+https://github.com/mpkato/bingpy@v5
```

Usage
------
Get your API Key at
https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api

```python
import bingpy
web = bingpy.WebSearch("YOUR_API_KEY")
pages = web.search("kyoto", 20)
for page in pages:
    print page.title
```
