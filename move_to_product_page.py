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
from main_utils import get_temperature, get_product, click_on_buy


def product_page():
    """takes you to the product page"""

    # create webdriver instance of chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    # navigate to main page
    driver.get("https://weathershopper.pythonanywhere.com/")
    # get the temperature value on the main page
    temperature = get_temperature(driver)
    # find out which product to buy
    product = get_product(temperature)
    # go to product page
    click_on_buy(driver, product)
    time.sleep(3)
    # verify if the user is taken to product page
    if driver.current_url == f"https://weathershopper.pythonanywhere.com/{product}":
        print(f"You're at the {product} page.")
    else:
        print("Oops! Redirecting failed")
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    product_page()
