import pandas as pd

csv_files = [
    'cordoba_guitars.csv',
    'focusrite.csv',
    'mahalo.csv',
    'mano_percussion.csv',
]
df2 = pd.DataFrame(columns=['SKU'])

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        if not pd.isna(row['Variant SKU']) and pd.isna(row['Variant Barcode']):
            print(f"'{row['Variant SKU']}',")
            df2 = df2.append({'SKU': row['Variant SKU']}, ignore_index=True)            
        else:
            continue

df2.to_csv('missing_barcodes.csv', index=False)