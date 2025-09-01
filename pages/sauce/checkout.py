from selenium.webdriver.common.by import By

from pages.sauce.order_summary import OrderSummaryPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.first_name = (By.ID,"first-name")
        self.last_name =(By.ID,"last-name")
        self.postal_code = (By.ID,"postal-code")
        self.checkout_button = (By.ID,"continue")


    def checkout(self,first_name,last_name,post_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(post_code)


    def proceed_to_finish(self):
        self.driver.find_element(*self.checkout_button).click()
        return OrderSummaryPage(self.driver)