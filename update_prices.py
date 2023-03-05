import pandas as pd
import numpy as np
import re

product_list_csv = 'fender_bass_products.csv'
upc_list_csv = 'fender_bass_output.csv'
output_file = 'fender_bass_products_updated.csv'
product_list = pd.read_csv(product_list_csv)
upc_list = pd.read_csv(upc_list_csv)

PRODUCT_LIST_SEARCH_FIELD = 'Variant SKU'
UPC_LIST_SEARCH_FIELD = 'Product Model'
PRODUCT_LIST_REPLACE_FIELD = 'Variant Price'
# UPC_LIST_REPLACE_FIELD = 'Price'
# UPC_LIST_REPLACE_FIELD = 'Product List Price'
UPC_LIST_REPLACE_FIELD = 'Product MAP Price'
# PRODUCT_LIST_REPLACE_FIELD_2 = 'Cost per item'
# UPC_LIST_REPLACE_FIELD_2 = 'Product Cost'

try:
    for _, upc_list_row in upc_list.iterrows():
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == upc_list_row[UPC_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD] = upc_list_row[UPC_LIST_REPLACE_FIELD]
            # product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == upc_list_row[UPC_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD_2] = upc_list_row[UPC_LIST_REPLACE_FIELD_2]

except:
    raise RuntimeError("Couldn't update product list")

try:
    product_list = product_list.replace(np.nan, '')
    product_list['Variant Barcode'] = product_list['Variant Barcode'].astype(str).apply(lambda x: re.sub( r'\.0$', '', x) )
    product_list['Variant SKU'] = product_list['Variant SKU'].astype(str).apply(lambda x: re.sub( r'\.0$', '', x) )
    product_list.to_csv(output_file, index=False)
    print(f'Output file "{output_file}" created')
except:
    raise RuntimeError("Couldn't save csv file")