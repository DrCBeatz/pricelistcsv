def main():
    # script to make csv of Shopify products inactive
    import pandas as pd

    product_list = 'products_export_10.csv'
    df = pd.read_csv(product_list)

    df['Body (HTML)'] += ' <p><strong>Offer valid until December 31st 2022</strong></p>'

    df.to_csv('output.csv')

if __name__ == '__main__':
    main()