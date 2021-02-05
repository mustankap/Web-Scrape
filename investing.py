import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd

pagesToGet= 1

upperframe=[]  
for page in range(1,pagesToGet+1):
    print('processing page :', page)
    url = 'https://in.investing.com/equities/india/?page='+str(page)
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
    links = soup.find_all("li",attrs={'class':'common-articles-item js-article-item'})
    filename = "INVESTING.csv"
    f = open(filename,"w", encoding = 'utf-8')
    headers="Topic,Statement,Source,Link,Date\n"
    f.write(headers)

    for j in links:
        Topic = j.find('div',attrs={'class':'content'}).find('h3',attrs={'class':'title'}).text.strip()
        Statement = j.find('p',attrs={'class':'summery'}).strip()
        Source = j.find('li',attrs={'class':'details-item is-darker'}).strip()
        Link = 'www.in.investing.com'
        Link += j.find('h3',attrs={'class':'title'}).find('a',attrs={'class':'link'})['href'].strip()
        Date = j.find('li',attrs={'class':'details-item'}).find('time').text.strip()
        frame.append((Topic,Statement,Source,Link,Date))
        f.write(Topic.replace(",","^")+","+Statement.replace(",","^")+","+Source+","+Link+","+Date.replace(",","^")+","+"\n")
    upperframe.extend(frame)
f.close()
data=pd.DataFrame(upperframe, columns=['Topic','Statement','Source','Link','Date'])
data.head()

'''Error stuck in'''
# processing page : 1
# https://in.investing.com/equities/india/?page=1
#  no error but csv page is blank