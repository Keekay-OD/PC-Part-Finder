from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json
import time
import sys
from difflib import get_close_matches


def main():
    searchbrand()
    


def searchbrand():
    keyVal = input("Enter a Brand Name eg:MSI, EVGA, ASUS: \n Search:")
    if keyVal == 'ALL':
        for key in dictionary.keys():
            print ('Name: {} Price: {}'.format(dictionary[key]))

    if keyVal in dictionary:
        print ('{} has {} years old.'.format(keyVal, dictionary[keyVal]))
    else:
    # you can to create a new registry or show error warning message here.
        print('Not found {}.'.format(keyVal))

    
   
   
   
   
   
   # keyVal = input("Enter a Brand Name eg:MSI, EVGA, ASUS: \n Search:")
  #  for key, val in dictionary.items():
  #      if keyVal in keyVal:
      #      x = {key:val}
   #         print("Found a match! {}".format(x))
   #         break
  #      else:
   #         print("Nothing found")
    
     
    
    
   
  


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



