bingpy3
======

## Python 3 version of [mpkato's bingpy](https://github.com/mpkato/bingpy).


Install
------


```bash
pip install git+https://github.com/tomtomgo/bingpy3.git
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
