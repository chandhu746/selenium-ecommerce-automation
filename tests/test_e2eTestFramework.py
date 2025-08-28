import json
import pytest
from utils.read_config import load_test_data
from pages.login_page import LoginPage
from utils.logger import get_logger
import  sys,os

logger = get_logger(__name__)
test_list=load_test_data()
# service_obj = Service("C:\\Users\\mchan\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# test_data_path ='../config/config.json'
# with open(test_data_path) as f:
#     test_data=json.load(f)
#     test_list=test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    logger.info(f"Running test for {test_list_item['base_url']} with product {test_list_item['productName']}")

    driver.get(test_list_item["base_url"]+"/loginpagePractise/")
    loginPage = LoginPage(driver)

    shop_page_var = loginPage.login(test_list_item["username"],test_list_item["userPassword"])
    shop_page_var.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page_var.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.entering_delivery_address("ind")
    checkout_confirmation.validate_order()

    logger.info("Test completed successfully...")



