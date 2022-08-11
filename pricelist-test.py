def main():
    import pandas as pd

    PRODUCT_LIST = 'shopify-productlist1.csv'
    PRICE_LIST = 'updated_pricelist.csv'
    PRODUCT_LIST_SEARCH_FIELD = 'Variant Barcode'
    PRICE_LIST_SEARCH_FIELD = 'UPC'
    PRODUCT_LIST_REPLACE_FIELD = 'Variant Price'
    PRICE_LIST_REPLACE_FIELD = 'Price'

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
            product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD] = price_list_row[PRICE_LIST_REPLACE_FIELD]
    except:
        raise RuntimeError("Couldn't update product list")

    try:
        product_list.to_csv(OUTPUT_FILENAME)
    except:
        raise RuntimeError("Couldn't generate output .csv file")
        

if __name__ == '__main__':
    main()
