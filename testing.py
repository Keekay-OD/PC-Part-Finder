import requests
from bs4 import BeautifulSoup




URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.findAll("div",{"class":"item-cell"})

brand = (containers,{"class":"item-info"})




