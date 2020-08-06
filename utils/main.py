"""
This module contains the required methods for automation of main page of weathershopper application
"""


def get_temperature(driver):
    """returns the temperature on the landing page"""
    temp = driver.find_element_by_xpath("//span[contains(@id,'temperature')]")
    # Slice only the temperature value
    temp = int(temp.text[:-2])
    return temp


def get_product(temp):
    """returns the product and types of items depending on the temperature value"""
    product = ""
    if temp < 19:
        product = "moisturizer"
    elif temp > 34:
        product = "sunscreen"
    return product


def click_on_buy(driver, product):
    """go to product page based on the temperature value"""
    print(f"The weather seems cold, redirecting to {product} page")
    driver.find_element_by_xpath(f"//button[contains(.,'Buy {product}s')]").click()
