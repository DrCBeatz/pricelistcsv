def main():
    # script to make csv of Shopify products inactive
    import pandas as pd

    product_list = 'products_export (20).csv'
    df = pd.read_csv(product_list, dtype={'Variant SKU':object, 'Variant Barcode':object})

    df['Title'] = "Unavailable - " + df['Title']
    df['Body (HTML)'] = '<p><strong>Unfortunately this item is no longer available for purchase</strong></p> ' + df['Body (HTML)']
    df['Type'] = 'Unavailable'
    df['Tags'] = ''
    df['Variant Inventory Policy'] = 'deny'

    df.to_csv('output.csv')

if __name__ == '__main__':
    main()