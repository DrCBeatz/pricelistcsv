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
        'SM57-LC',
        'SM58-LC',
        'PX-S1100',
    ]
    url = 'https://cosmomusic.ca'

    for product_model in product_list:
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)

        # click magnifying glass icon to open search input
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-header-search-trigger-target]'))).click()

        # click search input and enter product model
        search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]')))
        search_input.clear()
        search_input.send_keys(product_model)
        search_input.send_keys(Keys.RETURN)


        # click link that contains product model
        product_summary_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), ' {product_model} ')]"))).click()

        # Get product name, price, and image URL
        product_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1[class='product-info__name']"))).text
        product_price = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "*[class='product-prices__sell-price']"))).text
        product_image_url = driver.find_element_by_css_selector("img[class='product-details__primary-image-link-image']").get_attribute("src")

        # get product description
        try:
            product_description = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='product-detail-container__description-body']"))).text
        except:
            product_description = 'No description available'

        # get product info list which contains UPC
        product_info_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class='product-info__list']")))
        elementList = product_info_list.find_elements_by_tag_name("li")
        UPC = elementList[2].text.split(': ')[1]

        # print results to console
        print(f'Product name: {product_name}')
        print(f'Product model: {product_model}')
        print(f'Product price: {product_price}')
        print(f'UPC: {UPC}')
        print(f'Product description: {product_description}')
        print(f'Product image URL: {product_image_url}')
        print('')

        # add row to dataframe
        df = df.append({'Product Name': product_name, 'Product Model': product_model, 'Product Price': product_price, 'UPC': UPC, 'Product Description': product_description, 'Product Image URL': product_image_url}, ignore_index=True)

        # close browser window
        driver.close()

    # save dataframe to CSV file
    df.to_csv('cosmo_webscrape.csv', index=False)

    # close browser
    driver.quit()

if __name__ == '__main__':
    main()