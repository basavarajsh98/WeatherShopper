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
from product_utils import take_me_to_product_page, min_price
from cart_utils import add_to_cart, click_on_cart


def cart_page():
    """takes you to the cart page"""

    # create webdriver instance and navigate to main page
    driver = webdriver.Chrome()
    driver.maximize_window()
    # navigate to main page
    driver.get("https://weathershopper.pythonanywhere.com/")
    # go to product page depending on the temperature
    items = take_me_to_product_page(driver)
    time.sleep(3)
    # find the least expensive products
    cheap_products = min_price(driver, items)
    # add them to cart
    add_to_cart(driver, cheap_products)
    # go to cart
    click_on_cart(driver)
    time.sleep(3)
    # Verify if the user taken to cart
    if driver.current_url == "https://weathershopper.pythonanywhere.com/cart":
        print("Great! You're in your cart")
    else:
        print('Oops! Something went wrong')
        driver.quit()


if __name__ == "__main__":
    cart_page()
