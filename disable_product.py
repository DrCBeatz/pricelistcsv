def main():
    # script to make csv of Shopify products inactive
    import pandas as pd
    import numpy as np

    product_list = 'products_export (23).csv'
    df = pd.read_csv(product_list, dtype={'Variant SKU':str, 'Variant Barcode':str})

    df['Title'] = np.where(df['Title'].notna(), "Unavailable - " + df['Title'],  df['Title'])

    df['Body (HTML)'] = np.where(df['Body (HTML)'].notna(), '<p><strong>Unfortunately this item is no longer available for purchase</strong></p> ' + df['Body (HTML)'],  df['Body (HTML)'])

    df.loc[df['Type'].notna(), 'Type'] = 'Unavailable'

    df.loc[df['Tags'].notna(), 'Tags'] = ''

    df.loc[df['Variant Inventory Policy'].notna(), 'Variant Inventory Policy'] = 'deny'

    df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()