"""
This script will scrape the following information from the Cosmo Music website:
    - Product Name
    - Product Model
    - Product Price
    - UPC
    - Product Description
    - Product Image URL    
The script will loop through a list of product models and output the information to a CSV file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd


def main():
    df = pd.DataFrame(columns=['Product Name', 'Product Model', 'Product Price', 'UPC', 'Product Description', 'Product Image URL'])
    product_list = [
            'TF1',
        ]

    url = 'https://www.stevesmusic.com/'

    for product_model in product_list:
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)

        # click magnifying glass icon to open search input
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="term"]'))).click()

        # click search input and enter product model
        search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="term"]')))
        search_input.clear()
        search_input.send_keys(product_model)
        search_input.send_keys(Keys.RETURN)


        # click link that contains product model
        product_summary_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{product_model}')]"))).click()

        # Get product name, price, and image URL
        product_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1[class='product-title']"))).text
        product_price = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='product-price']"))).text
        
        product_upc = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='product-specs']/h3[2]"))).text.split(':')[1]

        product_image_url = driver.find_element(By.CSS_SELECTOR, "a[id='Zoom-1']").get_attribute("href").split('?')[0]
        print(product_name, product_price, product_upc, product_image_url)
        # get product description
        try:
            product_description = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='product-desc '"))).text
        except:
            product_description = 'No description available'

        # print results to console
        print(f'Product name: {product_name}')
        print(f'Product model: {product_model}')
        print(f'Product price: {product_price}')
        print(f'UPC: {product_upc}')
        print(f'Product description: {product_description}')
        print(f'Product image URL: {product_image_url}')
        print('')

        # add row to dataframe
        df = df.append({'Product Name': product_name, 'Product Model': product_model, 'Product Price': product_price, 'UPC': product_upc, 'Product Description': product_description, 'Product Image URL': product_image_url}, ignore_index=True)

        # close browser window
        driver.close()

    # save dataframe to CSV file
    df.to_csv('steves_webscrape.csv', index=False)

    # close browser
    driver.quit()

if __name__ == '__main__':
    main()