from bs4 import BeautifulSoup
import urllib.request
import re
import csv



#DATE AND TIME 
today = datetime.now()
d2 = today.strftime("%B %d, %Y %H:%M")


#Website you will be scraping from
url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
workbook = "products.csv"
file = open(workbook, "w")
models = []
prices = []

#Finding All the data from within that tag
product_model = soup.findAll("a", attrs={"class": "item-title"})
product_price = soup.find_all("li", attrs={"class": "price-current"})


#Parsing the data from all the extra html

for a in product_model:
    models.append(a.getText())
for li in product_price:
    prices.append(li.getText().split('\n')[0].strip()[0:7])


#converting list from data to Dictionary

with open('products.csv', 'a') as f:
    dictionary = dict(zip(models, prices))
    field_names = ['Prices:''\n''Models']
    dict_writer = csv.DictWriter(file, fieldnames=field_names)
    writer = csv.writer(file)
    dict_writer.writeheader()
    
    #writing to CSV file 
    for key, value in dictionary.items():
        writer.writerow([key, value])
file.close()