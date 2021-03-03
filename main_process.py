import datetime as dt 
import json
import subprocess

def moneycsvmake():
        filename = f"MONEYCONTROLNEWS_{today}.csv"
        f = open(filename,"w", encoding = 'utf-8')
        headers="Topic,Statement,Link,Date\n"
        f.write(headers)
        subprocess.call(['python3', 'moneycontrolscrape.py'])
        if(time is already 4):
            f.close()

def yahoocsvmake():
    filename = f"YAHOONEWS_{today}.csv"
    f = open(filename,"w", encoding = 'utf-8')
    headers="Topic,Statement,Link\n"
    f.write(headers)
    subprocess.call(['python3', 'yahoo_finance_for_each_company.py'])
    if(time is already 4):
        f.close()

def finvizcsvmake():
    filename = "FINVIZ.csv"
    f = open(filename,"w", encoding = 'utf-8')
    headers="statement,timestamp,link\n"
    f.write(headers)
    subprocess.call(['python3', 'news_finviz.py'])
    if(time is already 4):
        f.close()


today = dt.date.today()

with open("datetrack.json",'r') as file:
    temp=json.load(file)
if(str(today)==temp['date']):
    subprocess.call(['python3', 'moneycontrolscrape.py'])
else:
    print("new csv")
    with open("datetrack.json",'w') as outfile:
        json.dump({"date":str(today)},outfile)
    
    