def main():
    # script to append text to product description
    import pandas as pd
    import numpy as np

    product_list = 'products_export (25).csv'
    df = pd.read_csv(product_list, dtype={'Variant SKU':str, 'Variant Barcode':str})

    df['Handle'] = np.where(df['Handle'].notna(), df['Handle'] + "-USED",  df['Handle'])
    df['Title'] = np.where(df['Title'].notna(), "Previously Rented - " + df['Title'],  df['Title'])

    df['Body (HTML)'] = np.where(df['Body (HTML)'].notna(), "<p><strong>Previously rented - good condition</strong></p>" + df['Body (HTML)'],  df['Body (HTML)'])


    df['Variant SKU'] = np.where(df['Variant SKU'].notna(), df['Variant SKU'] + "-USED", df['Variant SKU'])
    df['Variant Barcode'] = np.where(df['Variant SKU'].notna(), df['Variant SKU'], df['Variant Barcode'])
    df['Variant Compare At Price'] = np.where(df['Variant Price'].notna(), df['Variant Price'], df['Variant Compare At Price'])
    df['Variant Price'] = np.where(df['Variant Price'].notna(), df["Variant Price"] * 0.8, df['Variant Price'])
    df = df.round({"Variant Price":2})

    df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()