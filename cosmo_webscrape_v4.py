"""
Cosmo Webscrape v4

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

WAIT_TIME = 5 # seconds
HEADLESS = False

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
if HEADLESS:
    chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def main():
    # create empty dataframe
    df = pd.DataFrame(columns=['Product Name', 'Product Model', 'Product Price', 'UPC', 'Product Description', 'Product Image URL'])

    # output file name
    output_file = 'cosmo_webscrape_v4.csv'
    upc_df = pd.read_csv('missing_barcodes.csv')
    product_list = upc_df['SKU'].tolist()

    url = 'https://cosmomusic.ca'

    print('\n*** Cosmo Webscrape v4 ***\n')
    print(f'Finding Barcodes for {len(product_list)} products:')
    for product in product_list:
        print(f'\t{product}')
    print('\nLoading Chrome Driver...')
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    print(f'Opening {url} in Chrome browser...')
    driver.get(url)
    products_not_found = 0
    products_not_found_list = []

    for product_model in product_list:    
        # click magnifying glass icon to open search input
        print(f'\nSearching for product {product_model}...')
        search_button = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-header-search-trigger-target]'))).click()

        # click search input and enter product model
        search_input = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]')))
        search_input.clear()
        search_input.send_keys(product_model)
        search_input.send_keys(Keys.RETURN)

        # get search result elements
        search_result_elements = driver.find_elements(By.CSS_SELECTOR, "div[class='grid__cell grid__cell--50 grid__cell--25-at-medium']")

        # if no search results, print product not found
        if len(search_result_elements) == 0:
            print(f'Product {product_model} not found')
            products_not_found += 1
            products_not_found_list.append(product_model)
            continue
        # if only one search result, click on it
        elif len(search_result_elements) == 1:
            try:
                product_summary_link = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='product-summary__media-link']"))).click()
            except:
                print('Product not found')
        else:
            # if more than one search result, loop through each search result and click on the one that matches the product model
            try:
                print('clicking product link...')
                product_summary_name = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), ' {product_model} ')]"))).click()
            except:
                print(f'Product {product_model} not found, redirecting...')
                for i in range(len(search_result_elements) - 1):
                    print(f'Search results element: {search_result_elements[i]}')
                    search_result_elements[i].click()
                    product_info_list = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class='product-info__list']")))
                    elementList = product_info_list.find_elements(By.TAG_NAME, "li")
                    search_product_model = elementList[1].text.split(': ')[1]
                    if search_product_model == product_model:
                        print(f'Product {product_model} found')
                        break
                    else:
                        print(f'Product {product_model} does not match {search_product_model}, tried {i} times')
                        driver.back()

        # get product info list which contains UPC and search product model
        try:
            product_info_list = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class='product-info__list']")))
        except:
            print('timed out')

        elementList = product_info_list.find_elements(By.TAG_NAME, "li")
        
        search_product_model = elementList[1].text.split(': ')[1]

        if search_product_model != product_model:
            print(f'Product {product_model} does not match {search_product_model}, redirecting...')
            driver.back()
            for i in range(len(search_result_elements) - 1):
                search_result_elements = driver.find_elements(By.CSS_SELECTOR, "div[class='grid__cell grid__cell--50 grid__cell--25-at-medium']")
                search_result_elements[i].click()
                product_info_list = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class='product-info__list']")))
                elementList = product_info_list.find_elements(By.TAG_NAME, "li")
                search_product_model = elementList[1].text.split(': ')[1]
                if search_product_model == product_model:
                    print(f'Product {product_model} found\n')
                    break
                else:
                    driver.back()
            if i > len(search_result_elements) - 1:
                print(f'Product {product_model} not found')
                products_not_found += 1
                products_not_found_list.append(product_model)
                continue

        UPC = elementList[2].text.split(': ')[1]

        # Get product name, price, and image URL
        product_name = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1[class='product-info__name']"))).text.strip()
        product_price = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "*[class='product-prices__sell-price']"))).text
        
        product_image_url = driver.find_element(By.CSS_SELECTOR, "img[class='product-details__primary-image-link-image']").get_attribute("src")
        
        # get product description
        try:
            product_description = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='product-detail-container__description-body']"))).text
        except:
            product_description = 'No description available'

        # print results to console
        print('----------------------------------------')
        print(f'Product name: {product_name}')
        print(f'Product model: {product_model}')
        print(f'Product price: {product_price}')
        print(f'UPC: {UPC}')
        print(f'Product description: {product_description}')
        print(f'Product image URL: {product_image_url}')
        print('----------------------------------------\n')

        # add row to dataframe
        row = {'Product Name': product_name, 'Product Model': product_model, 'Product Price': product_price, 'UPC': UPC, 'Product Description': product_description, 'Product Image URL': product_image_url}
        df_new_row = pd.DataFrame([row])
        df = pd.concat([df, df_new_row], axis=0, ignore_index=True)

    # save dataframe to CSV file
    df.to_csv(output_file, index=False)
    print('Results saved to CSV file\n')

    print('Results:')
    print(df)

    print(f'Number of products found: {len(df)}\n')
    print(f'Number of products not found: {products_not_found}\n')
    if products_not_found > 0:
        print('Products not found:')
        for product in products_not_found_list:
            print(f'\t{product}')

    # close browser
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()