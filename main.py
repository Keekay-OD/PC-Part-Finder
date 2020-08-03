from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json
import time
import sys

def main():
    login()

def login():
    print("-------------------------------------")
    print("This program Searches for the prices of the Latest GPU's on NewEgg.com")
    time.sleep(1)
    print("-------------------------------------")
    print('A copy of the latest prices and models has been saved as a CSV file')
    print("-------------------------------------")
    time.sleep(2)
    menu()

def menu():
    print("************MAIN MENU**************")
    time.sleep(1)
    print()

    choice = input("""
        1: Search By Brand
        2: Search By Price
        3: Search By Memory
        4: Search By Keyword
        5: Show All
        6: Quit/Log Out

        Please enter your choice: """)

    if choice == "1":
        searchbrand()
    elif choice == "2":
        searchprice()
    elif choice=="3":
        showall()
    elif choice=="4":
        sys.exit
    else:
        print("You must only select either 1,2, or 3.")
        print("Please try again")
        menu()


def showall():
    for x in dictionary:
        print (x)
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
    with open('data.json','w') as fp:
        json.dump(dictionary,fp)
    
file.close()


main()



