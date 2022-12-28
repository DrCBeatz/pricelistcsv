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

url = 'https://www.upcitemdb.com/'

driver = webdriver.Chrome('./chromedriver')

for product_model in product_list:
    driver.get(url)

    search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="searchinput"]')))
    
    search_input.clear()
    search_input.send_keys(f'{product_model}')
    search_input.send_keys(Keys.RETURN)

    try:
        upc_a_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='upclist col-xs-12']/ul/li[1]/div[@class='rImage']/a")))
        print(f'Product model: {product_model}; UPC: {upc_a_element.text}')
        df.append({'Product Model': product_model, 'UPC': upc_a_element.text}, ignore_index=True)
    except:
        print(f'Product model: {product_model}; UPC: Not found')
        df.append({'Product Model': product_model, 'UPC': 'Not found'}, ignore_index=True)
df.to_csv('upcitemdb_output.csv', index=False)
driver.quit()