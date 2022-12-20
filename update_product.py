def main():
    import pandas as pd

    PRODUCT_LIST = 'products_export (51).csv'
    PRICE_LIST = 'products5.csv'
    PRODUCT_LIST_SEARCH_FIELD = 'Variant SKU'
    PRICE_LIST_SEARCH_FIELD = 'model'
    PRODUCT_LIST_REPLACE_FIELD = 'Variant Price'
    PRICE_LIST_REPLACE_FIELD = 'Price'

    ['brand', 'title', 'price', 'description']
    OUTPUT_FILENAME = 'output.csv'

    try:
        product_list = pd.read_csv(PRODUCT_LIST)
    except:
        raise RuntimeError("Couldn't load product list .csv")

    try:
        price_list = pd.read_csv(PRICE_LIST)
    except:
        raise RuntimeError("Couldn't load price list .csv")

    try:
        for _, price_list_row in price_list.iterrows():
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], 'Vendor'] = price_list_row['brand']
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], 'Title'] = price_list_row['title']
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], 'Variant Price'] = price_list_row['price']
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], 'Body (HTML)'] = price_list_row['description']

    except:
        raise RuntimeError("Couldn't update product list")

    try:
        product_list.to_csv(OUTPUT_FILENAME)
    except:
        raise RuntimeError("Couldn't generate output .csv file")


if __name__ == '__main__':
    main()
