import requests
from bs4 import BeautifulSoup
# from pprint import pprint

product_search_url = "https://www.long-mcquade.com/?page=search&SearchTxt=ej16"
product_url = "https://www.long-mcquade.com/1545/Guitars/Strings/D-Addario/EJ16---Phosphor-Bronze-LIGHT-12-53.htm"

data = requests.get(product_url)

print(data.text)

my_data = []

html = BeautifulSoup(data.text, 'html.parser')

articles = html.select('a.post-card')

product_header_name = html.find(id="product-header-name")
print(f'Product title: {product_header_name.text}')

product_model = html.find(id="product-model")
print(f'Product model: {product_model.text}')

product_regular_price = html.find(id="product-regular-price")
print(f'Product regular price: ${product_regular_price.text}')

description_tab = html.find(id="Description-tab")
print(f'Product description: {description_tab.text}')

product_image = html.find(id="product-image")
print(f'image: {product_image}')