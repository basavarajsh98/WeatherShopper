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
browser = webdriver.Chrome()
# maximize the browser window
browser.maximize_window()
# navigate to weathershoppper page
browser.get("https://weathershopper.pythonanywhere.com/")

# KEY POINT: Code to find temperature
# Find the temperature element
value = browser.find_element_by_xpath("//span[contains(@id,'temperature')]")
# Slice only the temperature value
temp = int((value.text)[:-2])
value = value.text
# Conditions for shopping moisturizer/sunscreen
if temp < 19:
    # find the 'Buy moisturizers' button
    browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]").click()
    # Wait for new page to load
    time.sleep(3)
    print(f"The weather seems cold ({value}), redirecting to moisturizers page")
    # Verify if the taken user is taken to moisturizer page
    if browser.current_url == "https://weathershopper.pythonanywhere.com/moisturizer":
        print("You're at the moisturizers page.")
    else:
        print("Oops! Redirecting failed")
elif temp > 34:
    # find the 'Buy sunscreens' button
    browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]").click()
    # Wait for new page to load
    time.sleep(3)
    print(f"The weather seems hot ({value}), redirecting to sunscreens page")
    # Verify if the taken user is taken to sunscreen page
    if browser.current_url == "https://weathershopper.pythonanywhere.com/sunscreen":
        print("You're at the sunscreens page.")
    else:
        print("Oops! Redirecting failed")

browser.quit()