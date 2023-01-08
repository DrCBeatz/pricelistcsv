def main():
    import pandas as pd
    '''
    Script to remove substring from text field of pandas column
    '''
    product_list = 'products_export (69).csv'
    replace_column = 'Body (HTML)'
    remove_string = '<p><strong>Offer good from 10/21/22 to 12/31/22</strong></p>'
    output_file = 'string_removed5.csv'

    print(f"Reading file: {product_list}")
    try:
        df = pd.read_csv(product_list, dtype={'Variant SKU':str, 'Variant Barcode':str})
    except:
        print("Couldn't read .csv file")
    
    print("Replacing text...")
    try:
        df[replace_column] = df[replace_column].str.replace(remove_string, "")
    except:
        print("Couldn't replace text")

    try:
        df.to_csv(output_file, index=False)
    except:
        print("Couldn't write csv file")
        return(1)
    
    print(f"Saved file: {output_file}")

if __name__ == '__main__':
    main()
