import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd

pagesToGet= 1

upperframe=[]  
for page in range(1,pagesToGet+1):
    print('processing page :', page)
    url = 'https://in.finance.yahoo.com/topic/latestnews?page='+str(page)
    print(url)
    
    
    try:
        page=requests.get(url)                             
    
    except Exception as e:                                   
        error_type, error_obj, error_info = sys.exc_info()      
        print ('ERROR FOR LINK:',url)                          
        print (error_type, 'Line:', error_info.tb_lineno)     
        continue                                              
    time.sleep(2)   
    soup = BeautifulSoup(page.text,'html.parser')
    frame = []
    links = soup.find_all('li',attrs={'class':'js-stream-content Pos(r)'})
    filename = "YAHOOFINANCE.csv"
    f = open(filename,"w", encoding = 'utf-8')
    headers="Topic,Type,Statement,Link,Date\n"
    f.write(headers)

    for j in links:
        Topic = j.find("h3",attrs={'class':'Mb(5px)'}).text.strip()
        Type = j.find("div",attrs={'class':'Fz(12px) Fw(b) Tt(c) D(ib) Mb(6px) C($c-fuji-blue-1-a) Mend(9px) Mt(-2px)'}).text.strip() 
        Statement = j.find("p",attrs={'class':'Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(3,57px) LineClamp(3,51px)--sm1024 M(0)'}).strip()
        Link = 'www.in.finance.yahoo.com'
        Link += j.find("h3",attrs={'class':'Mb(5px)'}).find('a',attrs={'class':'js-content-viewer Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) not-isInStreamVideoEnabled wafer-destroyed'})['href'].strip()
        Date = j.find("div",attrs={'class':'C(#959595) Fz(11px) D(ib) Mb(6px)'}).find_all('span')
        frame.append((Topic,Type,Statement,Link,Date))
        f.write(Topic.replace(",","^")+","+Type+","+Statement.replace(",","^")+Link+","+Date.replace(",","^")+","+"\n")
    upperframe.extend(frame)
f.close()
data=pd.DataFrame(upperframe, columns=['Topic','Type','Statement','Link','Date'])
data.head()

'''Error stuck in'''
# processing page : 1
# https://in.finance.yahoo.com/topic/latestnews?page=1
# Traceback (most recent call last):
#   File "yahoofinance.py", line 34, in <module>
#     Topic = j.find("h3",attrs={'class':'Mb(5px)'}).text.strip()
# AttributeError: 'NoneType' object has no attribute 'text'