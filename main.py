import requests
from bs4 import BeautifulSoup

import prettify


URL = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

container = soup.find_all('div', class_ = 'item-container')
#print(soup.a)
print(container.a[title])