import fileinput
filename = 'template.xml'

def replace_file_text(string1, string2):
    with fileinput.FileInput("template.xml", inplace=True, backup='.bak') as file:
        for line in file:
           print(line.replace(string1, string2), end='')
    return

replace_file_text('SKU', '01234')
replace_file_text('VENDOR', 'JIFFY')
replace_file_text('DESCRIPTION', 'MY COOL PRODUCT')
replace_file_text('[regular-price]', '99.99')
replace_file_text('[sale-price]', '79.99')
replace_file_text('lengths="12"', 'lengths="10"')
replace_file_text('010101010101', '0123456789')