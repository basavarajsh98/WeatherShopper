"""
This module contains the required methods for automation of
product page of weathershopper application
"""
from main_utils import get_temperature, click_on_buy


def get_product(temp):
    """returns the product and types of items depending on the temperature value"""
    product = ""
    items = list()
    if temp < 19:
        product = "moisturizer"
        items = ["Aloe", "Almond"]
    elif temp > 34:
        product = "sunscreen"
        items = ["SPF-30", "SPF-50"]
    return product, items


def take_me_to_product_page(driver):
    """takes from landing page to product page"""
    temperature = get_temperature(driver)
    product, items = get_product(temperature)
    click_on_buy(driver, product)
    return items


def min_price(driver, items):
    """Returns the price of the least expensive aloe and almond products"""
    price = list()
    for item in items:
        item_list = driver.find_elements_by_xpath(f"//*[contains(text(),'{item}') or "
                                                  f"contains(text(),'{item.lower()}')]"
                                                  f"/following-sibling::p")
        price_list = [item_list[i - 1].text for i in range(len(item_list))]
        price_only = [price[-3:] for price in price_list]
        price.append(int(min(price_only)))
    return price
