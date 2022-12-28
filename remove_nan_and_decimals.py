import pandas as pd
import numpy as np
import re

df = pd.read_csv('output (50).csv')
print(df['Variant Barcode'])
df = df.replace(np.nan, '')
df['Variant Barcode'] = df['Variant Barcode'].astype(str).apply(lambda x: re.sub( r'\.0$', '', x) )
df['Variant SKU'] = df['Variant SKU'].astype(str).apply(lambda x: re.sub( r'\.0$', '', x) )
df.to_csv('output_no_nan.csv', index=False)
print(df['Variant SKU'])