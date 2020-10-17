from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json
import time
import sys
from difflib import get_close_matches
from wtforms.validators import url


def main1():
    pass  # Website you will be scraping from


url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
workbook = "products.csv"
file = open(workbook, "w")
models = []
prices = []
product_model = soup.findAll("a", attrs={"class": "item-title"})
product_price = soup.find_all("li", attrs={"class": "price-current"})
   # Parsing the data from all the extra html
for a in product_model:
    models.append(a.getText()[0:90].strip())
    for li in product_price:
        prices.append(li.getText().split('\n')[0].strip()[0:7])
   
dictionary = dict(zip(models, prices))

with open('products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Prices'])
    for key, value in dictionary.items():
        writer.writerow([key, value])
        with open('data.json', 'w', newline='') as fp:
            json.dump(dictionary, fp)    

    file.close()     # F   inding All the data from within that tag
       
   











