import requests
from bs4 import BeautifulSoup

import prettify


URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("a",{"class":"item-title"})
prices = soup.findAll("li",{"class":"price-current"})

for container in containers:
        model = container.findAll("a",{"class":"item-title"})
        product_model = containers[0].text 

for price in prices:
       #price = prices.find("li",{"class":"price-current"})
       product_price = prices[0].text


        
print(product_model)
print(product_price)
  
