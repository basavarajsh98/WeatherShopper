"""
This module contains the required methods for automation of
cart page of weathershopper application
"""
from utils.product_utils import take_me_to_product_page, min_price


def add_to_cart(driver, price):
    """adds the products to the cart and return number of items added"""
    for amount in price:
        driver.find_element_by_xpath(f"//*[contains(text(),'{amount}')]"
                                     f"/following-sibling::button").click()
    cart_items = driver.find_element_by_id("cart").text
    if cart_items == "2 item(s)":
        print("Added 2 items, redirecting to cart")
    else:
        print("Kindly add two items to proceed to cart")


def click_on_cart(driver):
    """go to cart page"""
    driver.find_element_by_id("cart").click()


def take_me_to_cart(driver):
    """takes from landing page to cart page"""
    items = take_me_to_product_page(driver)
    cheap_products = min_price(driver, items)
    add_to_cart(driver, cheap_products)
    click_on_cart(driver)
    return cheap_products


def verify_cart(driver, price):
    """ verifies the cart total"""
    flag = False
    total_expected = sum(price)
    total_actual = driver.find_element_by_xpath("//p[contains(@id,'total')]")
    total_actual = int(total_actual.text[-3:])
    if total_actual == total_expected:
        flag = True
    return flag
