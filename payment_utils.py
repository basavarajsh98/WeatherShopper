"""
This module contains the required methods for automation of
payment page of weathershopper application
"""
import random


def click_on_pay_with_card(driver):
    """proceed to payment"""
    driver.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()


def go_to_payment(driver):
    """switch to payment frame"""
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)


def generate_email():
    """generates a random email"""
    number = random.randrange(0, 100, 1)
    email = f"Internship_day_{number}@qxf2.com"
    return email


def enter_email(driver, email):
    """set the email input filed to generated email"""
    if ('@' in email) & ('.' in email) & ~(email.startswith("@", 0)):
        driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(email)


def enter_card_details(driver, ccn, exp, cvc):
    """set credit card number, valid till. cvc"""
    driver.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(ccn)
    driver.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys(exp)
    driver.find_element_by_xpath("//input[@placeholder='CVC']").send_keys(cvc)


def enter_zipcode(driver, zipcode):
    """set zipcode"""
    driver.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys(zipcode)


def want_me_to_remember(driver, remember, mobile):
    """remembers the payment details"""
    if remember.lower() in ["yes", "y"]:
        remember = driver.find_element_by_xpath("//div[@class='Checkbox-tick']").click()
        driver.find_element_by_xpath("//input[@inputmode='tel']").send_keys(mobile)


def click_on_pay(driver):
    """proceed to checkout"""
    driver.find_element_by_xpath("//button[@type='submit']").click()
