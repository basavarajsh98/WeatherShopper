def aloe_almond(browser):
    """
    Returns the price of the least expensive aloe and almond products
    """
    # find the products with aloe
    product_list_aloe = browser.find_elements_by_xpath("//*[contains(text(),'Aloe') or contains(text(),"
                                                       "'aloe')]/following-sibling::p")
    # find prices of the aloe products
    price_list_aloe = [product_list_aloe[i].text for i in range(len(product_list_aloe))]
    # slice only the price value
    price_only_aloe = [int(price[-3:]) for price in price_list_aloe]
    # find the least expensive aloe product
    cheap_aloe = min(price_only_aloe)

    # find the products with almond
    product_list_almond = browser.find_elements_by_xpath("//*[contains(text(),'Almond') or contains(text(),"
                                                         "'almond')]/following-sibling::p")
    # find prices of the almond products
    price_list_almond = [product_list_almond[i].text for i in range(len(product_list_almond))]
    # slice only the price value
    price_only_almond = [int(price[-3:]) for price in price_list_almond]
    # find the least expensive almond product
    cheap_almond = min(price_only_almond)
    return [cheap_aloe, cheap_almond]


def spf5030(browser):
    """
    Returns the price of the least expensive SPF50 and SPF30 products
    """
    # find the SP550 products
    product_list_SPF50 = browser.find_elements_by_xpath("//*[contains(text(),'SPF-50') or contains(text(),"
                                                        "'spf-50')]/following-sibling::p")
    # find prices of the SP550 products
    price_list_SPF50 = [product_list_SPF50[i].text for i in range(len(product_list_SPF50))]
    # slice only the price value
    price_only_SPF50 = [int(price[-3:]) for price in price_list_SPF50]
    # find the least expensive SPF50 item
    cheap_SPF50 = min(price_only_SPF50)

    # find the products with almond
    product_list_SPF30 = browser.find_elements_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),"
                                                        "'spf-30')]/following-sibling::p")
    # find prices of the almond products
    price_list_SPF30 = [product_list_SPF30[i].text for i in range(len(product_list_SPF30))]
    # slice only the price value
    price_only_SPF30 = [int(price[-3:]) for price in price_list_SPF30]
    # find the least expensive SPF30 item
    cheap_SPF30 = min(price_only_SPF30)
    return [cheap_SPF50, cheap_SPF30]


def add_to_cart(browser, prices):
    """
    adds the products to the cart and return number of items added
    """
    for i in prices:
        # find 'Add' element to add to cart
        browser.find_element_by_xpath(f"//*[contains(text(),{i})]/following-sibling::button").click()
    cart_items = browser.find_element_by_id("cart").text
    return cart_items
