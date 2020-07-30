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
from selenium import webdriver
from methods import aloe_almond, spf5030, add_to_cart, total, payment

# create an instance of Chrome Webdriver
DRIVER = webdriver.Chrome()
# maximize the DRIVER window
DRIVER.maximize_window()
# navigate to weathershoppper page
DRIVER.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: To make the payment
# Find the TEMPerature element
VALUE = DRIVER.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the TEMPerature VALUE
TEMP = int((VALUE.text)[:-2])
VALUE = VALUE.text
PRICES = 0
if TEMP < 19:
    # find the 'Buy moisturizers' button
    DRIVER.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    PRICES = aloe_almond(DRIVER)
elif TEMP > 34:
    # find the 'Buy sunscreens' button
    DRIVER.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    # find the cheapest products
    PRICES = spf5030(DRIVER)

# add the cheapest products to cart
CART_ITEMS = add_to_cart(DRIVER, PRICES)
# find cart element
DRIVER.find_element_by_id("cart").click()
# compare the displayed and calculated toal price
RATIO = total(DRIVER, PRICES)
# Verify the total amount and proceed to payment
if RATIO == 1:
    print("Total amount is verified. Redirecting to payment page")
    # redirect to payment page
    DRIVER.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()
    # Wait for new page to load
    time.sleep(3)
else:
    print("Oh! Total doesn't add up")
    DRIVER.quit()

# fill all the required details to make the payment
# payment(DRIVER, email, credit_card_number, expiry_date, CVC, zipcode, remember, mobile):
payment(DRIVER, 'weathershopperapp@qxf2.com',
        '4242424242424242', '0424', '425', '560054', 'N', '9562145587')
# wait for new page to load
time.sleep(5)

# Verify if the user is taken to checkout page
if DRIVER.current_url == "https://weathershopper.pythonanywhere.com/confirmation":
    print("Succesfully redirected to checkout page")
else:
    print('Oops! Something went wrong')
    DRIVER.quit()
# Verify if the payment was succesfull
if DRIVER.find_element_by_xpath("//h2[contains(.,'PAYMENT SUCCESS')]"):
    print("Payment Done")
else:
    print("Payment failed")
time.sleep(2)
DRIVER.close()
