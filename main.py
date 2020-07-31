import requests
from bs4 import BeautifulSoup
import csv




URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div", {"class": "item-cell"})

#model = soup.findAll("div",{"class":"item-info"})




workbook = "products.csv"
file = open(workbook, "w", newline='')

row = 0 
col = 0 

with file:
        headers = ['Brand', 'Model', 'Price\n']
        #writer = csv.DictWriter(file, fieldnames = headers)

        #writer.writeheader()

        for container in containers:
                        models = []
                        prices = []
                        # print(model_container)
                        product_model = container.find("a", attrs={"class": "item-title"}).text
                        product_price = container.find("li", attrs={"class": "price-current"}).text
                        models.append(product_model)
                        prices.append(product_price)
           
                        
                        

        
                        
                        
                         

                        #file.write(product_model)
        #writer.writerow({'Brand' , models})
print("This is the length of the list :", len(product_model))
print(models)
print(prices)


file.close()


