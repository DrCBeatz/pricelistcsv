import shutil
from compress import compress
import pandas as pd
from replace import nth_repl_all
import fileinput

def replace_file_text(string1, string2):
    with fileinput.FileInput(output_file, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(string1, string2), end='')
    return

df = pd.read_csv('banjo_label.csv', dtype={'Variant SKU':str, 'Variant Barcode':str, 'Variant Price':str, 'Variant Compare At Price':str})

sale = False
if sale == False:
    source_file = 'template_reg.xml'
else:
    source_file = 'template_sale.xml'

output_file = "label.xml"
lbx_files = ['label.xml', 'prop.xml', 'Object0.bmp']

title_string = """[TITLE]"""
shutil.copyfile(source_file, output_file)

i = 0

def main():
    new_title = nth_repl_all(df.iloc[i]['Title'], " ", "\n", 2)
    replace_file_text('[SKU]', df.iloc[i]['Variant SKU'])
    replace_file_text('[VENDOR]', df.iloc[i]['Vendor'])
    replace_file_text(title_string, new_title)
    if sale:
        replace_file_text('[reg-pr]',str(df.iloc[i]['Variant Compare At Price']))
        replace_file_text('[sale-pr]', str(df.iloc[i]['Variant Price']))
    else:
        replace_file_text('[reg-pr]', str(df.iloc[i]['Variant Price']))
    replace_file_text('010101010101', str(df.iloc[i]['Variant Barcode']))
    upc_length = len(str(df.iloc[i]['Variant Barcode']))
    replace_file_text('lengths="12"', f'lengths="{str(upc_length)}"')

    compress(lbx_files)

if __name__ == '__main__':
    main()