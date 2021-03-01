import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd

pagesToGet= 1
companies = []
upperframe=[]  
for page in range(1,pagesToGet+1):
    print('processing page to get tickers :')
    url = 'https://in.investing.com/indices/s-p-cnx-nifty-components'
    print(url)
    
    
    try:
        page=requests.get(url)                             # this might throw an exception if something goes wrong.
    
    except Exception as e:                                   # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()      # get the exception information
        print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
        print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
        continue                                              #ignore this page. Abandon this and go back.
    time.sleep(2)   
    soup = BeautifulSoup(page.text,'html.parser')
    frame = []
    links = soup.find_all('a',attrs={'class':'js-instrument-page-link'})
    print(links)
    # for j in links:
    #     ticker = j.find('a').text.strip()
    #     companies.append(ticker)
#print(companies)