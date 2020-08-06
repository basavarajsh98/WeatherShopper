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
from cart_utils import take_me_to_cart, verify_cart
from payment_utils import click_on_pay_with_card, go_to_payment, generate_email, enter_email
from payment_utils import enter_card_details, enter_zipcode, want_me_to_remember, click_on_pay


def checkout_page():
    """takes you to the checkout page"""

    # create webdriver instance of chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    # navigate to main page
    driver.get("https://weathershopper.pythonanywhere.com/")

    # find the least expensive products and add to cart
    cheap_products = take_me_to_cart(driver)
    # verify the cart items and total price
    result = verify_cart(driver, cheap_products)
    if result:
        print("Total amount is verified. Redirecting to payment page")
        click_on_pay_with_card(driver)
    else:
        print("Oh! Total doesn't add up")
        driver.quit()
    # wait for page to load
    time.sleep(5)
    # switch to payment frame
    go_to_payment(driver)
    # enter payment details
    email = generate_email()
    enter_email(driver, email)
    enter_card_details(driver, "4242424242424242", "824", "956")
    enter_zipcode(driver, "560054")
    want_me_to_remember(driver, "Y", "8456321456")
    click_on_pay(driver)
    time.sleep(7)

    # Verify if the user is taken to checkout page
    if driver.current_url == "https://weathershopper.pythonanywhere.com/confirmation":
        print("Succesfully redirected to checkout page")
        if driver.find_element_by_xpath("//h2[contains(.,'PAYMENT SUCCESS')]"):
            print("Payment Done")
        else:
            print("Payment failed")
    else:
        print('Oops! Something went wrong')
        driver.quit()

    time.sleep(5)
    driver.close()


if __name__ == "__main__":
    checkout_page()
