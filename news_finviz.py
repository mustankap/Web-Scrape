from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import pandas as pd
import pytz
from datetime import datetime

def fin(f):
    url = 'https://finviz.com/news.ashx'

    req = Request(url = url, headers={'user-agent':'my-app'})
    response = urlopen(req)
    html = BeautifulSoup(response,'html')
    news = html.find(id='news')
    rows = news.find_all('tr')
    frame = []
    upperframe = []

    for row in rows:
        try:
            statement = row.find('a').text.strip()
            timestamp = row.find('td',attrs = {'class':'nn-date'}).text.strip()
            link = row.find('a')['href'].strip()
            frame.append((timestamp,statement,link))
            f.write(statement.replace(",","^")+","+timestamp.replace(",","^")+","+link+"\n")
            
        except Exception as e:
            continue
    
    print("Scraped : "+url )
    upperframe.extend(frame)
    IST = pytz.timezone('Asia/Kolkata') 
    datetime_ist = datetime.now(IST) 
    timern=datetime_ist.strftime('%H:%M')
    if(timern=="16:00"):
        f.close()
    data=pd.DataFrame(upperframe, columns=['timestamp','statement','link'])
    data.head()
