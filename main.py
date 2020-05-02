import requests
from bs4 import BeautifulSoup

import prettify


URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div",{"class":"item-info"})
prices = soup.findAll("ul",{"class":"price    "})

for container in containers:
        model = container.findAll("a",{"class":"item-title"})
        product_model = model[0].text

#for price in prices:
      #  price = prices.findAll("ul",{"class":"price-current-label"})
      #  product_price = price[0].text


        
        
        print(product_model)
        #print(len(product_model))
       # print(product_price)
  
