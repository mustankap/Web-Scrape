import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
import pytz
from datetime import datetime 

def moneycontrolscrap(f):
    pagesToGet= 1
    upperframe=[]  
    for page in range(1,pagesToGet+1):
        print('processing page :', page)
        url = 'https://www.moneycontrol.com/news/business/stocks/?page='+str(page)
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
        links = soup.find_all('li',attrs={'class':'clearfix'})
        

        for j in links:
            try:
                Topic = j.find('h2').find('a')['title'].strip()
                Statement = j.find('p').text.strip()
                iLnk = 'www.moneycontrol.com'
                Link += j.find('h2').find('a')['href'].strip()
                Date = j.find('span').text.strip()
                #frame.append((Topic,Statement,Link,Date))
                f.write(Topic.replace(",","^")+","+Statement.replace(",","^")+","+Link+","+Date.replace(",","^")+"\n")
            except Exception as e:
                continue
        upperframe.extend(frame)
    IST = pytz.timezone('Asia/Kolkata') 
    datetime_ist = datetime.now(IST) 
    timern=datetime_ist.strftime('%H:%M')
    if(timern=="16:00"):
        f.close()
    data=pd.DataFrame(upperframe, columns=['Topic','Statement','Link','Date'])
    data.head()
    return 
