"""
Scope:
1) Launch Chrome browser
2) Navigate to weathershopper page
3) Based on the temperature, click on the moisturizer/sunscreen button
4) Verify user is taken to respective redirect pages
5) Close the browser

"""
import time
from selenium import webdriver

# create an instance of Chrome Webdriver
DRIVER = webdriver.Chrome()
# maximize the DRIVER window
DRIVER.maximize_window()
# navigate to weathershoppper page
DRIVER.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: Code to find TEMPerature
# Find the TEMPerature element
VALUE = DRIVER.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the TEMPerature VALUE
TEMP = int((VALUE.text)[:-2])
VALUE = VALUE.text
# Conditions for shopping moisturizer/sunscreen
if TEMP < 19:
    # find the 'Buy moisturizers' button
    DRIVER.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    print(f"The weather seems cold ({VALUE}), redirecting to moisturizers page")
    # Verify if the taken user is taken to moisturizer page
    if DRIVER.current_url == "https://weathershopper.pythonanywhere.com/moisturizer":
        print("You're at the moisturizers page.")
    else:
        print("Oops! Redirecting failed")
elif TEMP > 34:
    # find the 'Buy sunscreens' button
    DRIVER.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    print(f"The weather seems hot ({VALUE}), redirecting to sunscreens page")
    # Verify if the taken user is taken to sunscreen page
    if DRIVER.current_url == "https://weathershopper.pythonanywhere.com/sunscreen":
        print("You're at the sunscreens page.")
    else:
        print("Oops! Redirecting failed")
time.sleep(3)
DRIVER.quit()
