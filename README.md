# WebSearch

This is a python package that gets search results on Bing, Google and Yahoo.

# Requirements

* Chrome
* Selenium
* BeautifulSoup4

# Install

## WebSearch
### using pip

```
pip install WebSearch
```

### from repository

```
git clone https://github.com/nabehide/WebSearch.git
cd WebSearch
python setup.py install
```

## chromedriver

Download chromedriver from [official site](http://chromedriver.chromium.org/downloads).

# Usage

### example script

```
import WebSearch


bing = WebSearch.Bing(driverPath="./chromedriver", headless=False)
# google = WebSearch.Google(driverPath="./chromedriver", headless=False)
# yahoo = WebSearch.Yahoo(driverPath="./chromedriver", headless=False)

bing.open()  # open browser
result = bing.search(query="query")
bing.close()  # close browser
```

### output

```
result = {
    number: {
        "title": "***",
        "url": "***",
    }
}
```
