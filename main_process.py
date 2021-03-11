from datetime import datetime 
import json
import subprocess
import pytz
import os.path
import datetime as dt
from moneycontrolscrape import moneycontrolscrap
from yahoo_finance_for_each_company import yahoo
from news_finviz import fin

IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.now(IST) 
timern=datetime_ist.strftime('%H:%M')
today = dt.date.today()


save_path_m = '/home/mustansir/Web-Scrape/MoneyControlCSVs'       
filename_m = os.path.join(save_path_m,f"MONEYCONTROLNEWS_{today}.csv")

save_path_y = '/home/mustansir/Web-Scrape/YahooNewsCSVs'
filename_y = os.path.join(save_path_y,f"YAHOONEWS_{today}.csv")

save_path_f = '/home/mustansir/Web-Scrape/FinvizCSVs'
filename_f = os.path.join(save_path_f,f"FINVIZ_{today}.csv")

def moneycsvmake():
    f = open(filename_m,"w", encoding = 'utf-8')
    headers="Topic,Statement,Link,Date\n"
    f.write(headers)
    moneycontrolscrap(f)
    if(timern=="16:00"):
        f.close()

def yahoocsvmake():
    f = open(filename_y,"w", encoding = 'utf-8')
    headers="Topic,Statement,Link\n"
    f.write(headers)
    yahoo(f)
    if(timern=="16:00"):
        f.close()

def finvizcsvmake():
    f = open(filename_f,"w", encoding = 'utf-8')
    headers="statement,timestamp,link\n"
    f.write(headers)
    fin(f)
    if(timern=="16:00"):
        f.close()



with open("datetrack.json",'r') as file:
    temp=json.load(file)
if(str(today)==temp['date']):
    
    f=open(f'/home/mustansir/Web-Scrape/FinvizCSVs/FINVIZ_{today}.csv',"a",encoding = 'utf-8')
    fin(f)
    f=open(f'/home/mustansir/Web-Scrape/YahooNewsCSVs/YAHOONEWS_{today}.csv',"a",encoding = 'utf-8')
    yahoo(f)
    f=open(f'/home/mustansir/Web-Scrape/MoneyControlCSVs/MONEYCONTROLNEWS_{today}.csv',"a",encoding = 'utf-8')
    moneycontrolscrap(f)
else:
    print("new csv")
    with open("datetrack.json",'w') as outfile:
        json.dump({"date":str(today)},outfile)
    moneycsvmake()
    yahoocsvmake()
    finvizcsvmake()

    