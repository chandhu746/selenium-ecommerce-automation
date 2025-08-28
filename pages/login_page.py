from selenium.webdriver.common.by import By
from pages.shop_page import ShopPage

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.user_pass = (By.ID,"password")
        self.sign_button = (By.ID,"signInBtn")



    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.user_pass).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page_var = ShopPage(self.driver)
        return shop_page_var
