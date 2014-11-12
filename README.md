bingpy
======

Python Bing Search API (2014)

Install
------
```bash
pip install git+https://github.com/mpkato/bingpy.git
```

Usage
------
Get your API Key at https://datamarket.azure.com/dataset/bing/search

```python
from bingpy import WebSearch
web = WebSearch("YOUR_API_KEY")
pages = web.search("kyoto", 20)
for page in pages:
    print page.title
```
