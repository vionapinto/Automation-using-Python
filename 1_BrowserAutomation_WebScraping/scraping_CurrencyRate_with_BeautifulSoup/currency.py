from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    #print(url) # check if the URL is working
    
    content = requests.get(url).text # source code
    #print(content) #printing out the source code
    
    soup = BeautifulSoup(content, 'html.parser') # the source code is in html, so here we tell beautiful soup to use the html parser.
    
    rate = soup.find("span", class_="ccOutputRslt").get_text() # inspected inr to usd amount went inside span and checked the class

    #print(rate) # --> 0.012085 USD (trying to get float, we dont need last 4 positions ie upto the space)

    rate = float(rate[:-4])

    return rate
    
current_rate = get_currency('INR','USD')
print(current_rate)