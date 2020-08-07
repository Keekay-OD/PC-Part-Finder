from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json
import time
import sys

def main():
    searchbrand()
    


def searchbrand():
    keyVal = input("Enter a Brand Name eg:MSI, EVGA, ASUS: \n Search:")
    for i in range(0, len(dictionary), 1):
        if dictionary[i] == keyVal:
            print(dictionary)
			
    else:
        print('This GPU isnt on Newegg.com')
        menu()   
    
    
     
    
    
   
  


def showall():
    for x in dictionary:
        print (x,':')
        for y in dictionary[x]:
            print (y,':',dictionary)
    menu()





# Website you will be scraping from
url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96"

page = urllib.request.urlopen(url)      
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
workbook = "products.csv"
file = open(workbook, "w")
models = []
prices = []

# Finding All the data from within that tag
product_model = soup.findAll("a", attrs={"class": "item-title"})
product_price = soup.find_all("li", attrs={"class": "price-current"})


# Parsing the data from all the extra html

for a in product_model:
    models.append(a.getText()[0:90].strip())
for li in product_price:
    prices.append(li.getText().split('\n')[0].strip()[0:7])


# converting list from data to Dictionary
dictionary = dict(zip(models, prices))

#Writing Header
with open('products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Prices'])

    # Writing to CSV file/Json
    for key, value in dictionary.items():
        writer.writerow([key, value])
    with open('data.json','w',newline='') as fp:
        json.dump(dictionary,fp)
    
file.close()



main()



