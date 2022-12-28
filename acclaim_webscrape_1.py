from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

df = pd.DataFrame(columns=['Product Model', 'UPC'])

product_list = [
            'TRBX305 CAR',
            'TRBX305 WH',
            'TRBX304 CAR',
            'CO-C5-CE',
'C1M',
'Scarlett 2i2 MKII',
'SCARLETT-4I4-3RD-GEN',
'CLARETT-4PRE-USB',
'MR1-RD',
'MR1-BK',
'MR1-LBU',
'MR1-YW',
'MR1-GN',
'MR1-PK',
'MR1-PP',
'MR1-OR',
'MP1690-NA',
'MP1690',
'MP1511F-WRD',
'MP1511F-BK',
'MP1511F-OD',
'MP1434',
'MP3802-RD',
'MP-TDC-BK',
'MP-TDC-RD',
'MP-TDC-WH',
'MP-AG',
'MP-CL',
'MP-DTBL',
'MP-EGGS-BL',
'MP-EGGS-YW',
'MP-EGGS-OR',
'MP-EGGS-GN',
'MP-EGGS-PP',
'MP-EGGS-RD',
'MP-TR6',
'MP-TR7',
'MP-TR8',
'MP-CB4',
'MP-CB5',
'MP-CB6',
'MP-CB8',
'MP-CB9',
'MP-SBH',
'MP-SBL',
'MP-SBBH',
'MP-BBL',
'MP-DDC-RD',
'MP-DDC-BK',
'MP-DDC-WH',
'MP1601-BK',
'MP-MA-RD',
'MP-SSG',
]

url = 'https://www.acclaim-music.com'

div_class = 'pull-right col-xs-6 text-right'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

for product_model in product_list:
    search_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="ubersearch"]')))
    
    product_model = product_model.strip()    
    
    search_input.clear()
    search_input.send_keys(f'{product_model}')
    search_input.send_keys(Keys.RETURN)

    try:
        product_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), ' {product_model} ')]"))).click()
    except:
        print(f'Product {product_model} not found')
        continue

    try:
        upc_div = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='col-md-5 col-xs-12 product-card']/div[6]")))
        upc = upc_div.text.split('\n')[1].strip()
    except:
        upc = 'UPC not found'
    df = df.append({'Product Model': product_model, 'UPC': upc}, ignore_index=True)    
    
    print(f'Product Model: {product_model} UPC: {upc}')

df.to_csv('acclaim_upcs.csv', index=False)
driver.quit()