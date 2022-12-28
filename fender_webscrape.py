from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

site_url = 'https://dealer.fender.com/login'
username = ''
password = ''

product_list = [
        '2311100000',
        '2311000000',
        '378553506',
        '0234810000',
        '0990700100',
        '0239979002',
    ]

def main():
    df = pd.DataFrame(columns=['Product Name', 'Product Model', 'MAP Price', 'Dealer Cost', 'UPC', 'Product Description', 'Product Image URL'])
    driver = webdriver.Chrome('./chromedriver')
    driver.get(site_url)
    
    # login
    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="emailInput"]')))
    email_input.clear()
    email_input.send_keys(username)

    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="passwordInput"]')))    
    password_input.clear()
    password_input.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="submitLoginButton"]'))).click()

    # search products
    for product in product_list:
        search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="search-fld"]')))
        search_input.clear()
        search_input.send_keys(product)
        search_input.send_keys(Keys.RETURN)


        upc_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[name="imageView_upc"]')))
        upc = upc_span.text
        dealer_cost_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[name="imageView_dealerNet"]')))

        dealer_cost = dealer_cost_span.text.split('$')[1]

        try:
            map_price_span = driver.find_element(By.CSS_SELECTOR, 'span[name="imageView_map"]')
            map_price = map_price_span.text.split('$')[1]
        except:
            map_price = ''
        
        model_no_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[name="imageView_modelNo"]')))

        model_no = model_no_span.text

        product_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3[name="imageView_name"]')))
        print(f'Product Name: {product_name.text}')
        print(f'Product Model: {model_no}')
        print(f'Dealer Cost: {dealer_cost}')
        print(f'Product Price: {map_price}')
        print(f'UPC: {upc}')

        img_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-image-container']/img[1]")))
        image_url = img_element.get_attribute('src')
        print(image_url)
        # dealer cost (span) (USD): name="imageView_dealerNet"
        # MAP price (span) (CAD): name="imageView_map"
        # model#/sku: (span) name="imageView_modelNo"
        # product name: (H3) name="imageView_name"
        # description: (div) class="description-column" .show_more_box.div.div.p
        # image url: (div) class="product-image-container" .img.src
        
        try:
            description_element = driver.find_element(By.XPATH, "//div[@class='description-column']/show-more-box/div/div[1]")
            description = description_element.text
        except:
            description = 'No description available'
        
        print(f'Product Description: {description}')
        df = df.append({'Product Name': product_name.text, 'Product Model': model_no, 'MAP Price': map_price, 'Dealer Cost': dealer_cost, 'UPC': upc, 'Product Description': description, 'Product Image URL': image_url}, ignore_index=True)
    driver.quit()
    print(df)
    df.to_csv('fender_products.csv', index=False)

if __name__ == '__main__':
    main()
