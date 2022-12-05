import requests
import shutil
import pandas as pd
import os

input_file = 'products4.csv'
output_file = 'products_imgs.zip'

df = pd.read_csv(input_file)

for i in range(len(df.index)):
    model = df.iloc[i]['model']
    img_url = df.iloc[i]['image']
    file_name = f'{model}.jpg'
    print(model, img_url)
    res = requests.get(img_url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
            print('Image downloaded: ', file_name)
    else:
        print('Image could not be downloaded')

os.system(f'rm {output_file}')
os.system(f'zip {output_file} *.jpg')
os.system("rm *.jpg")