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
from methods import aloe_almond, spf5030, add_to_cart
from selenium import webdriver

# create an instance of Chrome Webdriver
browser = webdriver.Chrome()
# maximize the browser window
browser.maximize_window()
# navigate to weathershoppper page
browser.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: Code to add products to cart
# Find the temperature element
value = browser.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the temperature value
temp = int((value.text)[:-2])
value = value.text
# Conditions for shopping moisturizer/sunscreen
if temp < 19:
    # find the 'Buy moisturizers' button
    browser.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    prices = aloe_almond(browser)
    # add the cheapest products to cart
    cart_items = add_to_cart(browser, prices)
elif temp > 34:
    # find the 'Buy sunscreens' button
    browser.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    prices = spf5030(browser)
    # add the cheapest products to cart
    cart_items = add_to_cart(browser, prices)
# Verify if the cart has only 2 item(s) and redirect, if yes
if cart_items == "2 item(s)":
    print("Redirecting to cart page")
    browser.find_element_by_id("cart").click()
    # Wait for new page to load
    time.sleep(3)
else:
    print("Failed to redirect to cart page")

browser.quit()
