from tickers_for_yahoo import companies
import requests
import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
import pytz
from datetime import datetime

def yahoo(f):
    tickers = companies
    upperframe=[]
    for i in range(len(tickers)):
        url = f'https://in.finance.yahoo.com/quote/{tickers[i]}/news?p={tickers[i]}'
        print("Scraped :" + url)
        try:
            page=requests.get(url)  
            # print(page)                           
        except Exception as e:                                   
            error_type, error_obj, error_info = sys.exc_info()      
            print ('ERROR FOR LINK:',url)                          
            print (error_type, 'Line:', error_info.tb_lineno)     
            continue                                              
        time.sleep(1)   
        soup = BeautifulSoup(page.text,'html.parser')
        frame = []
        links = soup.find_all('li',attrs={'class':'js-stream-content Pos(r)'})
        if len(links) == 0:
            continue
        else:
            f.write(f'company :{tickers[i]}'+'\n')
        for j in links:
            try:
                Topic = j.find('a').text.strip()
                #print(Topic)
                Statement = j.find('p').text.strip()
                #print(Statement)
                Link = 'www.in.finance.yahoo.com/news/'
                Link += j.find('h3').find('a')['href'].strip()
                #print(Link)
                # Date = j.find('div').find('span')
                # print(Date.text)
                frame.append((Topic,Statement,Link))
                f.write(Topic.replace(",","^")+","+Statement.replace(",","^")+","+Link+"\n")
            except Exception as e:
                continue
        upperframe.extend(frame)
        f.write('\n')
    IST = pytz.timezone('Asia/Kolkata') 
    datetime_ist = datetime.now(IST) 
    timern=datetime_ist.strftime('%H:%M')
    if(timern=="16:00"):
        f.close()
    data=pd.DataFrame(upperframe, columns=['Topic','Statement','Link'])
    data.head()
            
    
