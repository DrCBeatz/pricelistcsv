def main():
    # script to append text to product description
    import pandas as pd
    import numpy as np
    import zipfile
    from bs4 import BeautifulSoup as bs
    import lxml

    path_to_zip_file = 'FENDER ACOUSTASONIC 15 summer sale.lbx'
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall()
    content = []
    # Read the XML file
    with open("label.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs(content, "lxml")
    # result = bs_content.find("pt:data")
    result =  bs_content.findAll("pt:data")
    print(result)
    # print(pd.__version__)
    # df = pd.read_xml('label.xml', dtype={'Variant SKU':str, 'Variant Barcode':str})
    # print(df)



    # df['Handle'] = np.where(df['Handle'].notna(), df['Handle'] + "-USED",  df['Handle'])
    # df['Title'] = np.where(df['Title'].notna(), "Previously Rented - " + df['Title'],  df['Title'])

    # df['Body (HTML)'] = np.where(df['Body (HTML)'].notna(), "<p><strong>Previously rented - very good condition</strong></p>" + df['Body (HTML)'],  df['Body (HTML)'])


    # df['Variant SKU'] = np.where(df['Variant SKU'].notna(), df['Variant SKU'] + "-USED", df['Variant SKU'])
    # df['Variant Compare At Price'] = np.where(df['Variant Price'].notna(), df['Variant Price'], df['Variant Compare At Price'])
    # df['Variant Price'] = np.where(df['Variant Price'].notna(), df["Variant Price"] * 0.8, df['Variant Price'])
    # df = df.round({"Variant Price":2})

    # df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()