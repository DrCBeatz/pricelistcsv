def main():
    # script to append text to product description
    import pandas as pd

    product_list = 'products_export (13).csv'
    df = pd.read_csv(product_list)

    df['Body (HTML)'] += ' <p><strong>Offer good from 10/21/22 to 12/31/22</strong></p>'

    df.to_csv('output.csv')

if __name__ == '__main__':
    main()