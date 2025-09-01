from attr.filters import exclude
from selenium.webdriver.common.by import By

from pages.sauce.cartPage import CartPage


class Products:

    def __init__(self,driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME,"inventory_item")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")



    def get_all_products(self):

        products =self.driver.find_elements(*self.inventory_item)
        print(f"Found {len(products)} products")
        return products


    def add_products_with_conditions(self,max_price,exclude=None):
        products = self.get_all_products()

        for product in products:
            title = product.find_element(By.CLASS_NAME,"inventory_item_name").text
            description = product.find_element(By.CLASS_NAME,"inventory_item_desc").text
            price =product.find_element(By.CLASS_NAME,"inventory_item_price").text
            price_value = float(price.replace("$",""))

            if price_value <= max_price and (exclude is None or exclude.lower() not in title.lower()):
                print(f"Adding {title} with price {price_value}")
                product.find_element(By.TAG_NAME, "button").click()
            else:
                print(f"Skipped {title} - ${price_value} (too expensive products)")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        cartPage_var = CartPage(self.driver)
        return cartPage_var


