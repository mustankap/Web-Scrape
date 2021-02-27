import requests
import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time


url = f'https://in.investing.com/news/markets/stock-market'
print(url) 
for _ in range() 
try:
    page=requests.get(url)  
                                
except Exception as e:                                   
    error_type, error_obj, error_info = sys.exc_info()      
    print ('ERROR FOR LINK:',url)                          
    print (error_type, 'Line:', error_info.tb_lineno)     
                                                
time.sleep(1)   
soup = BeautifulSoup(page.text,'html.parser')

links = soup.find('ul',attrs={'class':'common-articles-list'})
print(links)




# if len(links) == 0:
#     continue
# else:
#     f.write(f'company :{tickers[i]}'+'\n')
# for j in links:
#     try:
#         Topic = j.find('a').text.strip()
#         #print(Topic)
#         Statement = j.find('p').text.strip()
#         #print(Statement)
#         Link = 'www.in.finance.yahoo.com/news/'
#         Link += j.find('h3').find('a')['href'].strip()
#         #print(Link)
#         # Date = j.find('div').find('span')
#         # print(Date.text)
#         frame.append((Topic,Statement,Link))
#         f.write(Topic.replace(",","^")+","+Statement.replace(",","^")+","+Link+"\n")
#     except Exception as e:
#         continue
# upperframe.extend(frame)
# f.write('\n')
# f.close()
# data=pd.DataFrame(upperframe, columns=['Topic','Statement','Link'])
# data.head()
            
    