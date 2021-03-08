from datetime import datetime 
import json
import subprocess
import pytz
import os.path
import datetime as dt


IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.now(IST) 
timern=datetime_ist.strftime('%H:%M')
today = dt.date.today()
f = None

def moneycsvmake():
    save_path = '/home/mustansir/Web-Scrape/MoneyControlCSVs'       
    filename = os.path.join(save_path,f"MONEYCONTROLNEWS_{today}.csv")
    f = open(filename,"w", encoding = 'utf-8')
    headers="Topic,Statement,Link,Date\n"
    f.write(headers)
    subprocess.call(['python3', 'moneycontrolscrape.py'])
    if(timern=="16:00"):
        f.close()

def yahoocsvmake():
    save_path = '/home/mustansir/Web-Scrape/YahooNewsCSVs'
    filename = os.path.join(save_path,f"YAHOONEWS_{today}.csv")
    f = open(filename,"w", encoding = 'utf-8')
    headers="Topic,Statement,Link\n"
    f.write(headers)
    subprocess.call(['python3', 'yahoo_finance_for_each_company.py'])
    if(timern=="16:00"):
        f.close()

def finvizcsvmake():
    save_path = '/home/mustansir/Web-Scrape/FinvizCSVs'
    filename = os.path.join(save_path,f"FINVIZ_{today}.csv")
    f = open(filename,"w", encoding = 'utf-8')
    headers="statement,timestamp,link\n"
    f.write(headers)
    subprocess.call(['python3', 'news_finviz.py'])
    if(timern=="16:00"):
        f.close()
with open("datetrack.json",'r') as file:
    temp=json.load(file)
if(str(today)==temp['date']):
    subprocess.call(['python3', 'moneycontrolscrape.py'])
    subprocess.call(['python3', 'news_finviz.py'])
    subprocess.call(['python3', 'yahoo_finance_for_each_company.py'])
else:
    print("new csv")
    with open("datetrack.json",'w') as outfile:
        json.dump({"date":str(today)},outfile)
    moneycsvmake()
    yahoocsvmake()
    finvizcsvmake()

    