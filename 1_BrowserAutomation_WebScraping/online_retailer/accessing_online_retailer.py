import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")  # MSFT for Microsoft, APPL for Apple etc
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

# Making it int here since the link wont work with a float value
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

# We don't need to use Selenium here, since the download button has a link. We also notice that the ticker, start and end dates change when we change the values. Hence we can make the link a f string and added required input fields here.
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} # Need to use this so that the website lets us scrape the data

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)