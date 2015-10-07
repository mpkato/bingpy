bingpy
======

Python Bing Search API (2014)

[python3 branch](https://github.com/mpkato/bingpy/tree/python3) includes bingpy for python3 thanks to [Tomtomgo](https://github.com/Tomtomgo)

Install
------
```bash
pip install bingpy
```

OR

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
