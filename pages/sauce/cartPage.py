from selenium.webdriver.common.by import By
from pages.sauce.checkout import CheckoutPage

class CartPage:


    def __init__(self,driver):
        self.driver = driver
        self.cart_list = (By.CLASS_NAME,"cart_list")
        self.cart_items = (By.CLASS_NAME,"cart_item")


    def get_cart_items(self):
        cart_list = self.driver.find_element(*self.cart_list)
        return cart_list.find_elements(*self.cart_items)

    def get_item_names(self):
        items = self.get_cart_items()
        names=[]
        for item in items:
            name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
            names.append(name)
        return names

    def get_item_prices(self):
        items = self.get_cart_items()
        prices = []
        for item in items:
            price_text = item.find_element(By.CLASS_NAME,"inventory_item_price").text
            price_value = float(price_text.replace("$",""))
            prices.append(price_value)
        return prices

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID,"checkout").click()
        check_var  = CheckoutPage(self.driver)
        return check_var

