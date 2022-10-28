import fileinput
import shutil
from compress import compress
import pandas as pd

df = pd.read_csv('output.csv')

df.loc
source_file = 'template.xml'
output_file = "label.xml"
lbx_files = ['label.xml', 'prop.xml', 'Object0.bmp']

title_string = """[TITLE


]"""
shutil.copyfile(source_file, output_file)

def replace_file_text(string1, string2):
    with fileinput.FileInput(output_file, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(string1, string2), end='')
    return

def main():
    # title = str(df.iloc[0]['Title']).replace(' ', '\n')
    title = str(df.iloc[0]['Title'])
    replace_file_text('[SKU]', df.iloc[0]['Variant SKU'])
    replace_file_text('[VENDOR]', df.iloc[0]['Vendor'])
    replace_file_text(title_string, title)
    replace_file_text('[regular-price]', str(df.iloc[0]['Variant Compare At Price']))
    replace_file_text('[sale-price]', str(df.iloc[0]['Variant Price']))
    replace_file_text('010101010101', str(df.iloc[0]['Variant Barcode']))
    upc_length = len(df.iloc[0]['Variant Barcode'])
    replace_file_text('lengths="12"', f'lengths="{str(upc_length)}"')

    compress(lbx_files)

if __name__ == '__main__':
    main()