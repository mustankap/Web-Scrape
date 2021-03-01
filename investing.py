import requests
import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time

pages_to_get = 5

nifty50=['axis-bank',
'mundra-port-special-eco.-zone',
'asian-paints',
'bajaj-auto',
'bajaj-finance',
'bajaj-finserv-limited',
'bharat-petroleum',
'bharti-airtel',
'britannia-industries',
'cipla',
'coal-india',
'divis-laboratories',	
'dr-reddys-laboratories',	
'eicher-motors',	
'gail-(india)',
'grasim-industries',
'hcl-technologies',
'hdfc-bank-ltd',
'hdfc-standard-life',
'hero-motocorp',
'hindalco-industries',
'hindustan-unilever',
'housing-development-finance',	
'icici-bank-ltd',
'itc',	
'indian-oil-corporation',	
'indusind-bank',	
'infosys',	
'jsw-steel',	
'kotak-mahindra-bank',	
'larsen---toubro',
'mahindra---mahindra',
'maruti-suzuki-india',	
'ntpc',
'nestle',	
'oil---natural-gas-corporation',
'power-grid-corp.-of-india',	
'reliance-industries',
'state-bank-of-india',	
'sbi-life-insurance',	
'shree-cements',	
'sun-pharma-advanced-research',	
'tata-consultancy-services',
'tata-motors-ltd',	
'tata-steel',
'tech-mahindra',
'titan-industries',
'united-phosphorus',
'ultratech-cement',	
'wipro-ltd']

for i in nifty50:
    url = f'https://in.investing.com/equities/{i}-news'
    print(url) 
    for _ in range(pages_to_get+1): 
        try:
            page=requests.get(url)  
                                        
        except Exception as e:                                   
            error_type, error_obj, error_info = sys.exc_info()      
            print ('ERROR FOR LINK:',url)                          
            print (error_type, 'Line:', error_info.tb_lineno)     
        time.sleep(1)   
        soup = BeautifulSoup(page.text,'html.parser')
        links = soup.find('li',attrs={'class':'common-articles-item'})
        print(len(links))
     




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
            
    