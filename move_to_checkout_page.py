"""
Scope:
1) Launch Chrome browser
2) Navigate to weathershopper page
3) Based on the temperature, click on the moisturizer/sunscreen button
4) add 2 cheapest products to cart
5) Redirect to cart and pay with card
6) Fill all the details and proceed with the payment
5) Close the browser
"""
import time
from methods import aloe_almond, spf5030, add_to_cart, total, payment
from selenium import webdriver

# create an instance of Chrome Webdriver
browser = webdriver.Chrome()
# maximize the browser window
browser.maximize_window()
# navigate to weathershoppper page
browser.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: To make the payment
# Find the temperature element
value = browser.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the temperature value
temp = int((value.text)[:-2])
value = value.text
global prices
if temp < 19:
    # find the 'Buy moisturizers' button
    browser.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    prices = aloe_almond(browser)
elif temp > 34:
    # find the 'Buy sunscreens' button
    browser.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    prices = spf5030(browser)

# add the cheapest products to cart
cart_items = add_to_cart(browser, prices)
# find cart element
browser.find_element_by_id("cart").click()
# compare the displayed and calculated toal price
ratio = total(browser, prices)
# Verify the total amount and proceed to payment
if ratio == 1:
    print("Total amount is verified. Redirecting to payment page")
    # redirect to payment page
    browser.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()
    # Wait for new page to load
    time.sleep(3)
else:
    print("Oh! Total doesn't add up")
    browser.quit()

# fill all the required details to make the payment
# payment(browser, email, credit_card_number, expiry_date, CVC, zipcode, remember, mobile):
payment(browser, 'weathershopperapp@qxf2.com', '4242424242424242', '0424', '425', '560054', 'N', '9562145587')
# wait for new page to load
time.sleep(5)

# Verify if the user is taken to checkout page
if browser.current_url == "https://weathershopper.pythonanywhere.com/confirmation":
    print("Succesfully redirected to checkout page")
else:
    print('Oops! Something went wrong')
    browser.quit()
# Verify if the payment was succesfull
if browser.find_element_by_xpath("//h2[contains(.,'PAYMENT SUCCESS')]"):
    print("Payment Done")
else:
    print("Payment failed")
time.sleep(2)
browser.close()