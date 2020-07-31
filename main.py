import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div", {"class": "item-cell"})

#model = soup.findAll("div",{"class":"item-info"})




filename = "products.csv"
file = open(filename, "w", newline='')



with file:
        headers = ['Brand', 'Model', 'Price\n']
        writer = csv.DictWriter(file, fieldnames = headers)

        writer.writeheader()

        for container in containers:
                        models = []
                        # print(model_container)
                        product_model = container.find("a", attrs={"class": "item-title"}).text
                        models.append(product_model)

                        print("Brand: " + product_model )

                        #file.write(product_model)
        writer.writerow(product_model)

file.close()


