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

#DATE AND TIME 
today = datetime.now()
d2 = today.strftime("%B %d, %Y %H:%M")

headers = "This list was updated last on: " + d2 + "\n" "\n"
file.write(headers)

titles = ['Model:']
titless = ['Price:']






models = []
prices = []

with file:

    for container in containers:
        product_model = container.find("a", attrs={"class": "item-title"}).get_text()
        product_price = container.find("li", attrs={"class": "price-current"}).get_text().strip()[0:7]
        models.append(product_model)
        prices.append(product_price)

    
        for row in models:
            for col in row:
                print("%10s"%col),
            print('\n')
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([product_model])
        writer.writerow([product_price])
        

#CSV FUNCTIONS         



file.close()

#file.write(product_model + "\n " + product_price)




