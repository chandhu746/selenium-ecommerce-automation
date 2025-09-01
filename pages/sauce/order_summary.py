from selenium.webdriver.common.by import By
from pages.sauce.finishpage import FinishPage


class OrderSummaryPage:
    def __init__(self,driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME,"cart_item")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def get_item(self):
        names =[]
        for item in self.get_cart_items():
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            names.append(name)
        return names

    def get_item_prices(self):
        prices = []
        for item in self.get_cart_items():
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            prices.append(float(price.replace("$","")))
        return prices

    def get_summary_details(self):
        subtotal = self.driver.find_element(*self.subtotal_label).text
        tax = self.driver.find_element(*self.tax_label).text
        total = self.driver.find_element(*self.total_label).text
        return {"subtotal": subtotal, "tax": tax, "total": total}

    def finish_order(self):
        self.driver.find_element(*self.finish_button).click()
        return FinishPage(self.driver)