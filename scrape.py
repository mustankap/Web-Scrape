import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd

#url of the page that we want to Scarpe
#+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
URL = 'https://www.politifact.com/factchecks/list/?page='+str(page)
#Use the browser to get the URL. This is a suspicious command that might blow up.
page = requests.get(url)
