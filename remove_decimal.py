def main():
    # script to decimal points from UPC and SKU fields
    import pandas as pd
    # import numpy as np

    product_list = 'products_export (18).csv'
    df = pd.read_csv(product_list, dtype={'Variant SKU':object, 'Variant Barcode':object})
    # df = pd.read_csv(product_list)


    # df['Variant SKU'] = df['Variant SKU'].astype(int, errors='ignore')
    # df['Variant Barcode'] = df['Variant Barcode'].astype(int, errors='ignore')

    df['Title'] = "Unavailable - " + df['Title']
    df['Body (HTML)'] = '<p><strong>Unfortunately this item is no longer available for purchase</strong></p> ' + df['Body (HTML)']
    df['Type'] = 'Unavailable'
    df['Tags'] = ''
    df['Variant Inventory Policy'] = 'deny'

    df.to_csv('output.csv')

if __name__ == '__main__':
    main()