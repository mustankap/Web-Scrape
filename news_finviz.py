from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://finviz.com/news.ashx'

req = Request(url = url, headers={'user-agent':'my-app'})
response = urlopen(req)
html = BeautifulSoup(response,'html')
news = html.find(id='news')
rows = news.find_all('tr')

frame = []
upperframe = []
filename = "FINVIZ.csv"
f = open(filename,"w", encoding = 'utf-8')
headers="statement,timestamp,link\n"
f.write(headers)

for row in rows:
    try:
        statement = row.find('a').text.strip()
        timestamp = row.find('td',attrs = {'class':'nn-date'}).text.strip()
        # print(timestamp)
        link = row.find('a')['href'].strip()
        # print(link)
        frame.append((timestamp,statement,link))
        f.write(statement.replace(",","^")+","+timestamp.replace(",","^")+","+link+"\n")
    except Exception as e:
        continue
    # timestamp= row.td.text
    # print(timestamp+"  "+title)
upperframe.extend(frame)
f.close()
# data=pd.DataFrame(upperframe, columns=['timestamp','statement','link'])
# data.head()
