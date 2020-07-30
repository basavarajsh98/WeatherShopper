"""
Scope:
1) Launch Chrome browser
2) Navigate to weathershopper page
3) Based on the temperature, click on the moisturizer/sunscreen button
4) add 2 cheapest products to cart
5) Verify if the cart has only 2 item(s)
6) Verify if the user is taken to redirected page(cart page)
5) Close the browser

"""
import time
from selenium import webdriver
from methods import aloe_almond, spf5030, add_to_cart


# create an instance of Chrome WebDRIVER
DRIVER = webdriver.Chrome()
# maximize the DRIVER window
DRIVER.maximize_window()
# navigate to weathershoppper page
DRIVER.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: Code to add products to cart
# Find the TEMPerature element
VALUE = DRIVER.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the TEMPerature VALUE
TEMP = int((VALUE.text)[:-2])
VALUE = VALUE.text
# Conditions for shopping moisturizer/sunscreen
if TEMP < 19:
    # find the 'Buy moisturizers' button
    DRIVER.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    PRICES = aloe_almond(DRIVER)
    # add the cheapest products to cart
    CART_ITEMS = add_to_cart(DRIVER, PRICES)
elif TEMP > 34:
    # find the 'Buy sunscreens' button
    DRIVER.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    PRICES = spf5030(DRIVER)
    # add the cheapest products to cart
    CART_ITEMS = add_to_cart(DRIVER, PRICES)
# Verify if the cart has only 2 item(s) and redirect, if yes
if CART_ITEMS == "2 item(s)":
    print("Redirecting to cart page")
    DRIVER.find_element_by_id("cart").click()
    # Wait for new page to load
    time.sleep(3)
else:
    print("Failed to redirect to cart page")
    DRIVER.quit()
#Verify if the user taken to cart
if DRIVER.current_url == "https://weathershopper.pythonanywhere.com/cart":
    print("Great! You're in your cart")
else:
    print('Oops! Something went wrong')
    DRIVER.quit()
