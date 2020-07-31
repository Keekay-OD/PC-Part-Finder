import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div", {"class": "item-cell"})


workbook = "products.csv"
file = open(workbook, "w", newline='')

today = datetime.now()
d2 = today.strftime("%B %d, %Y %H:%M")

headers = "This list was updated last on: " + d2 + "\n" "\n"


file.write(headers)

models = []
prices = []

with file:

    for container in containers:
        product_model = container.find("a", attrs={"class": "item-title"}).get_text()
        product_price = container.find("li", attrs={"class": "price-current"}).get_text().strip()[0:7]
        models.append(product_model)
        prices.append(product_price)

    #for i in models:
            
        file.write(product_model + "\n " + product_price)


#print(product_price)

file.close()
