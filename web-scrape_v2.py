import requests
from bs4 import BeautifulSoup
# from pprint import pprint

product = 'EJ16'
product_SKUs = ['EJ16', 'EJ11', 'EJ27N']



product_search_url = "https://www.long-mcquade.com/?page=search&SearchTxt=ej16"
product_url = "https://www.long-mcquade.com/1545/Guitars/Strings/D-Addario/EJ16---Phosphor-Bronze-LIGHT-12-53.htm"

search_data = requests.get(product_search_url)

search_html = BeautifulSoup(search_data.text, 'html.parser')

# soup = BeautifulSoup(html) 
for tag in search_html.find_all('a',{"class":"products-item-link"}): 
    if 'Model: EJ16' in tag.text:
    # if tag.find('Model: EJ16'):
        print (tag.text.split(' '))


# print(search_data.text)
# print(search_html)

# print(search_html.find_all("a", class_="products-item-link"))

# print(search_html.find_all(class_="Model"))

# print(search_html.find('EJ16'))

# data = requests.get(product_url)

# print(data.text)

# my_data = []

# html = BeautifulSoup(data.text, 'html.parser')

# html.select('products-item-link')

# # articles = html.select('a.post-card')

# product_header_name = html.find(id="product-header-name")
# print(f'Product title: {product_header_name.text}')

# product_model = html.find(id="product-model")
# print(f'Product model: {product_model.text}')

# product_regular_price = html.find(id="product-regular-price")
# print(f'Product regular price: ${product_regular_price.text}')

# description_tab = html.find(id="Description-tab")
# print(f'Product description: {description_tab.text}')

# product_image = html.find(id="product-image")
# print(f'image: {product_image}')