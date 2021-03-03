# # from urllib.request import urlopen as uReq
# # from bs4 import BeautifulSoup as soup
# # from datetime import datetime, timedelta
# # from dateutil import parser
# # import pytz

# # my_url = "https://www.coindesk.com/category/business-news/legal"

# # # Opening up the website, grabbing the page
# # uFeedOne = uReq(my_url, timeout=5)
# # page_one = uFeedOne.read()
# # uFeedOne.close()

# # # html parser
# # page_soup1 = soup(page_one, "html.parser")

# # # grabs each publication block
# # containers = page_soup1.findAll("a", {"class": "stream-article"} )
# # print(len(containers))

# # for container in containers:
# #   ## get todays date.
# #   ## I have taken an offset as the site has older articles than today.
# #   today =  datetime.now() - timedelta(days=5)
# #   print(today)
# #   link = container.attrs['href']
# #   print(link)
# #   ## The actual datetime string is in the datetime attribute of the time tag.
# #   date_time = container.time['datetime']

# #   ## we will use the dateutil package to parse the ISO-formatted date.
# #   date = parser.parse(date_time)
# #   print(date)
# #   ## This date is UTC localised but the datetime.now() gives a "naive" date
# #   ## So we have to localize before comparison
# #   utc=pytz.UTC
# #   today = utc.localize(today)

#   # ## simple comparison
#   # if date >= today:
#   #     print("article date", date)
#   #     print("yesterday", today," \n")
#   #     publication_date = "published on " + container.time.text
#   #     title = container.h3.text.encode('utf-8')
#   #     description = "(CoinDesk)-- " +  container.p.text

#   #     print("link: " + link)
#   #     print("publication_date: " + publication_date)
#   #     print("title: ", title)
#   #     print("description: " + description)

from datetime import datetime 
import pytz 
  
# # get the standard UTC time  
# # UTC = pytz.utc 
  
# # it will get the time zone  
# # of the specified location 
IST = pytz.timezone('Asia/Kolkata') 
  
# # print the date and time in 
# # standard format 
# # print("UTC in Default Format : ",  
#       # datetime.now(UTC)) 
  
# # print("IST in Default Format : ",  
# #       datetime.now(IST)) 
  
# # print the date and time in  
# # specified format 
# # datetime_utc = datetime.now(UTC) 
# # print("Date & Time in UTC : ", 
# #       datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z')) 
  
datetime_ist = datetime.now(IST) 
m=datetime_ist.strftime('%H:%M')
print(typeOf(m))
# print(m) 
# import datetime as dt 
# import json

# today = dt.date.today()

# with open("datetrack.json",'r') as file:
#   temp=json.load(file)


# if(str(today)==temp['date']):
#   print("append")
# else:
#   print("new csv")
#   with open("datetrack.json",'w') as outfile:
#     json.dump({"date":str(today)},outfile)
