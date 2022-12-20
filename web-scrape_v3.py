import requests
from bs4 import BeautifulSoup
import pandas as pd
from product_skus import PRODUCT_SKUS

product_SKUs = PRODUCT_SKUS.split()

columns = ['model', 'brand', 'title', 'price', 'description', 'url', 'image' ]

output_file = 'products5.csv'

df = pd.DataFrame(columns=columns)

def main():
    for product in product_SKUs:

        product_search_url = f'https://www.long-mcquade.com/?page=search&SearchTxt={product}'

        search_data = requests.get(product_search_url)

        search_html = BeautifulSoup(search_data.text, 'html.parser')

        for tag in search_html.find_all('a',{"class":"products-item-link"}):
            if f'Model: {product}\t' in tag.text:

                product_url = tag.get('href')
                print(product)
                print(product_url)

                product_data = requests.get(product_url)

                product_html = BeautifulSoup(product_data.text, 'html.parser')

                product_brand = product_html.find(id="product-brand")
                print(f'Product brand: {product_brand.text}')

                product_header_name = product_html.find(id="product-header-name")
                print(f'Product title: {product_header_name.text}')

                product_model = product_html.find(id="product-model")
                print(f'Product model: {product_model.text}')

                product_regular_price = product_html.find(id="product-regular-price")
                print(f'Product regular price: ${product_regular_price.text}')

                description_tab = product_html.find(id="Description-tab")
                print(f'Product description: {description_tab.decode_contents()}')

                product_image = product_html.find(id="product-image-lg")
                print(f'image: {product_image["href"].split("?alt")[0]}jpg')

                # columns = ['model', 'brand', 'title',  'price', 'description', 'url', 'image' ]
                # .decode_contents() get python unicode string from html while .encode_contents() get utf-8 string from html
                df.loc[len(df.index)] = [product_model.text, product_brand.text.strip(), product_header_name.text, product_regular_price.text, description_tab.text.strip(), product_url, (product_image["href"].split("?alt")[0])]

    df.to_csv(output_file, index=False)
if __name__ == '__main__':
    main()