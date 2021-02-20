from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime

def login (user, password):
    print ('Starting the browser...')
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys(user)
    password_input.send_keys(password + Keys.RETURN)
    
    print("Logging success")
    print("user: " + user)
    print("password: " + password)

    print("Getting Inventory list")
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    print("Adding all products to the cart")
    for item in inventory_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        print("adding product to cart:" + title)
        item.find_element(By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']").click()

    print("Go to cart container page")
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link fa-layers fa-fw']").click()
    
    print("Get all products in the cart")
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    
    print("Removing all products from the cart")
    for item in cart_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        print("removing product from cart:" + title)
        button = item.find_element(By.CSS_SELECTOR, "button[class='btn_secondary cart_button']").click()

    print("Done!")

login('standard_user', 'secret_sauce')